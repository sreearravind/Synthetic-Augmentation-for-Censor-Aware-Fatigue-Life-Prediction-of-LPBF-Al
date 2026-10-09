#!/usr/bin/env python3
"""Exploratory exact-fold sensitivity to 53 new graph-derived failures.

Uses locked M1 model, tau=.25 and frozen exact train/test membership. New
graph sources contribute fractional failure log likelihood under their own
integrated study intercept. External reserved sources are never opened.
"""
import argparse
import csv
import hashlib
import json
import math
import platform
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np
import scipy
from scipy.optimize import minimize
from scipy.special import logsumexp

from fit_m1_source_aware import (CHECK_NODES, FIT_NODES, FOLDS,
    conditional_logterms, median_m1, prediction_checks,
    quadrature, read_csv, write_csv)

TAU=.25
CASES=[("cap5_center",5.,"center","both"),
       ("cap2p5_center",2.5,"center","both"),
       ("cap10_center",10.,"center","both"),
       ("cap5_low_low",5.,"low","both"),
       ("cap5_high_high",5.,"high","both"),
       ("cap5_only_Muhammad",5.,"center","Muhammad_2023"),
       ("cap5_only_Fernandes",5.,"center","Fernandes_2024")]

def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()

def weighted_groups(exact, graph):
    groups=defaultdict(list)
    for r in exact+graph:groups[r["study_id"]].append(r)
    out=[]
    for source,rr in sorted(groups.items()):
        out.append((source,np.array([r["stress_amplitude_MPa"] for r in rr],float),
                    np.array([r["cycles_failure_or_bound"] for r in rr],float),
                    np.array([r["failure_event_1"] for r in rr],int),
                    np.array([r.get("weight",1.) for r in rr],float)))
    return out

def objective(params, grouped, nodes):
    points, logweights=quadrature(nodes)
    ans=0.
    for _,stress,cycles,event,weight in grouped:
        terms=conditional_logterms(params,stress,cycles,event,TAU*points)
        if terms is None:return 1e300
        ans-=float(logsumexp(logweights+np.sum(weight[:,None]*terms,axis=0)))
    return ans if math.isfinite(ans) else 1e300

def fit(train_exact,graph,control):
    groups=weighted_groups(train_exact,graph)
    starts=[np.asarray(control,float),np.array([control[0],-1.,-.5]),
            np.array([control[0],-3.,.5])]
    bounds=((0.,12.),(-12.,0.),(-4.,3.))
    solutions=[minimize(objective,start,args=(groups,FIT_NODES),method="L-BFGS-B",
                        bounds=bounds,options={"maxiter":3000,"ftol":1e-12,"maxls":50}) for start in starts]
    valid=[s for s in solutions if s.success and np.isfinite(s.fun) and s.fun<1e299]
    if not valid:raise RuntimeError("No converged weighted fit: "+str([s.message for s in solutions]))
    sol=min(valid,key=lambda s:s.fun)
    delta=abs(sol.fun-objective(sol.x,groups,CHECK_NODES))
    if delta>1e-5:raise RuntimeError("Quadrature instability "+str(delta))
    if sol.x[1]>=-1e-6 or sol.x[1]<=-11.999999 or sol.x[2]<=-3.999999 or sol.x[2]>=2.999999:
        raise RuntimeError("Bound hit "+str(sol.x))
    return sol,delta

def graph_rows(src,cap,reading,selection):
    selected=[r for r in src if selection=="both" or r["source"]==selection]
    sizes=Counter(r["source"] for r in selected)
    result=[]
    for r in selected:
        stress=float(r["stress_amplitude_"+("mpa" if reading=="center" else reading+"_mpa")])
        logn=float(r["log10_cycles"+("" if reading=="center" else "_"+reading)])
        if not (stress>0 and 3<=logn<=9):raise ValueError("out of range "+r["record_id"])
        result.append(dict(record_id="GRAPH:"+r["record_id"],study_id=r["source"],
            stress_amplitude_MPa=stress,cycles_failure_or_bound=10**logn,
            failure_event_1=1,weight=min(1.,cap/sizes[r["source"]])))
    return result

def score(params,test):
    stress=np.array([float(r["stress_amplitude_MPa"]) for r in test])
    cycles=np.array([float(r["cycles_failure_or_bound"]) for r in test])
    ev=np.array([int(r["failure_event_1"]) for r in test])
    pred,delta=prediction_checks(params,TAU,stress,cycles,ev)
    nll=-pred
    median=np.array([median_m1(params,TAU,s) for s in stress])
    return pred,nll,median,delta

def main():
    ap=argparse.ArgumentParser()
    for arg in ("exact","manifest","graph","baseline_fits","baseline_scores","out"):
        ap.add_argument("--"+arg.replace("_","-"),type=Path,required=True)
    a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=True)
    if sha(a.exact)!="29aff38de63880dbfbaf65d3b876b81bd5afabfaaaac1615e2e503fbfa661a30":raise ValueError("Exact hash changed")
    if sha(a.manifest)!="0df2fdec2399cae1c76c202a323691431bdc96bb9eb31fa278f6b307ac84eb91":raise ValueError("Manifest hash changed")
    exact=read_csv(a.exact);graph=read_csv(a.graph);manifest=read_csv(a.manifest)
    assert len(exact)==66 and len(graph)==53 and len({r["record_id"] for r in graph})==53
    assert {r["source"] for r in graph}=={"Muhammad_2023","Fernandes_2024"}
    assert all(r["event"]=="1" and r["censoring"]=="failure"
               and r["training_role"]=="candidate_training_only" for r in graph)
    assert all(r["source"] not in {"Strauss_Lowisch_2024","Kempf_2022","Hamidi_Nasab_2019"} for r in graph)
    basefits={(r["fit"],float(r["tau"])):r for r in read_csv(a.baseline_fits)}
    basescores={(r["fold"],float(r["tau"])):r for r in read_csv(a.baseline_scores)}
    by_id={r["record_id"]:r for r in exact}
    metrics=[];parameters=[];predictions=[]
    for fold in FOLDS:
        members=[r for r in manifest if r["analysis"]=="primary_exact_LOSO" and r["fold_id"]==fold]
        train=[by_id[r["record_key"].removeprefix("EXACT:")] for r in members if r["role"]=="train"]
        test=[by_id[r["record_key"].removeprefix("EXACT:")] for r in members if r["role"]=="test"]
        assert len(members)==66 and {r["study_id"] for r in test}=={fold.removeprefix("E0_")}
        assert not ({r["study_id"] for r in train} & {r["study_id"] for r in test})
        control=basefits[(fold,TAU)]
        base_params=np.array([float(control["alpha"]),float(control["beta"]),
                              math.log(float(control["weibull_shape_k"]))])
        base_pred,base_nll,base_median,_=score(base_params,test)
        saved=basescores[(fold,TAU)]
        assert abs(base_nll.mean()-float(saved["m1_mean_nll"]))<1e-9
        event=np.array([int(r["failure_event_1"]) for r in test])
        baseline_mae=np.mean(abs(base_median[event==1]-np.log10([float(r["cycles_failure_or_bound"]) for r in test if int(r["failure_event_1"])])))
        for label,cap,reading,selection in CASES:
            rows=graph_rows(graph,cap,reading,selection)
            assert not ({r["study_id"] for r in rows}&{r["study_id"] for r in test})
            solution,obj_delta=fit(train,rows,base_params)
            pred,nll,median,pred_delta=score(solution.x,test)
            deltas=nll-base_nll
            mae=np.mean(abs(median[event==1]-np.log10([float(r["cycles_failure_or_bound"]) for r in test if int(r["failure_event_1"])])))
            effective=Counter()
            for r in rows:effective[r["study_id"]]+=r["weight"]
            metrics.append(dict(case=label,fold=fold,tau=TAU,exact_train_n=len(train),graph_train_n=len(rows),
                graph_source_effective_weight_Muhammad=round(effective["Muhammad_2023"],4),
                graph_source_effective_weight_Fernandes=round(effective["Fernandes_2024"],4),
                exact_test_n=len(test),fail_n=int(event.sum()),runout_n=int(len(test)-event.sum()),
                baseline_mean_nll=float(base_nll.mean()),augmented_mean_nll=float(nll.mean()),
                augmented_minus_baseline_mean_nll=float(deltas.mean()),
                baseline_failure_mean_nll=float(base_nll[event==1].mean()),
                augmented_failure_mean_nll=float(nll[event==1].mean()),
                failure_mean_nll_change=float(deltas[event==1].mean()),
                baseline_runout_mean_nll=float(base_nll[event==0].mean()) if (event==0).any() else "",
                augmented_runout_mean_nll=float(nll[event==0].mean()) if (event==0).any() else "",
                runout_mean_nll_change=float(deltas[event==0].mean()) if (event==0).any() else "",
                baseline_failure_median_MAE=float(baseline_mae),augmented_failure_median_MAE=float(mae),
                failure_median_MAE_change=float(mae-baseline_mae)))
            parameters.append(dict(case=label,fold=fold,tau=TAU,
                alpha=float(solution.x[0]),beta=float(solution.x[1]),shape_k=float(math.exp(solution.x[2])),
                objective=float(solution.fun),quadrature_objective_delta_161_321=float(obj_delta),
                predictive_max_log_delta_161_321=float(pred_delta),optimizer_success=bool(solution.success)))
            for i,r in enumerate(test):
                predictions.append(dict(case=label,fold=fold,record_id=r["record_id"],event=int(event[i]),
                    exact_test_stress_amplitude_MPa=float(r["stress_amplitude_MPa"]),
                    exact_test_cycles_or_bound=float(r["cycles_failure_or_bound"]),
                    baseline_nll=float(base_nll[i]),augmented_nll=float(nll[i]),
                    augmented_minus_baseline_nll=float(deltas[i]),
                    baseline_median_log10_cycles=float(base_median[i]),
                    augmented_median_log10_cycles=float(median[i])))
            print(label,fold,"delta",round(float(deltas.mean()),4),"failure",round(float(deltas[event==1].mean()),4),"runout",round(float(deltas[event==0].mean()),4) if (event==0).any() else "NA",flush=True)
    assert len(metrics)==len(parameters)==21 and len(predictions)==462
    write_csv(a.out/"fold_metrics_21.csv",metrics)
    write_csv(a.out/"fit_parameters_21.csv",parameters)
    write_csv(a.out/"paired_exact_record_predictions_462.csv",predictions)
    meta=dict(status="exploratory previously inspected exact folds; not confirmatory",
              fixed_model="M1 study-marginal Weibull AFT, fixed tau=0.25",hypothetical_graph_likelihood="fractional per-row log likelihood inside study offset integral",
              graph_source_total_caps=[2.5,5,10],primary_diagnostic_cap=5,
              reading_scenarios="center, joint low/low, joint high/high; reading bounds not confidence intervals",
              train_rule="frozen exact train studies plus two graph-only source groups; candidate graph failures only",
              test_rule="66 unchanged exact outcomes, three already inspected leave-study-out folds",
              no_new_external_test=True,no_synthetic_data=True,
              input_sha256={"exact":sha(a.exact),"manifest":sha(a.manifest),"graph53":sha(a.graph),
                            "baseline_fits":sha(a.baseline_fits),"baseline_scores":sha(a.baseline_scores)},
              software={"python":platform.python_version(),"numpy":np.__version__,"scipy":scipy.__version__})
    (a.out/"run_metadata.json").write_text(json.dumps(meta,indent=2)+"\n")
    print("Output",a.out,flush=True)

if __name__=="__main__":main()
