#!/usr/bin/env python3
"""Training-only, source-aware synthetic feasibility probe; never an experiment.

Wu is the sole anchor with a defensible source-wide 1e7 stop in this cohort.
The Romano 8,889,311 bound belongs to one specimen and is not propagated
as a cohort-wide stopping policy; Chen provides no observed runout bound.
"""
import argparse
import csv
import hashlib
import json
import math
import platform
from collections import Counter
from pathlib import Path

import numpy as np
import scipy

from fit_m1_source_aware import FOLDS, FIT_NODES, conditional_logterms, quadrature, prediction_checks, read_csv, write_csv
from source_aware_new_graph_tier_sensitivity import fit, graph_rows, score, sha

STOP_WU=10_000_000
SEEDS=(13,29,47,71,101)
CAPS=(2.,5.)
DRAW_N=20

def posterior_nodes(params, exact_wu):
    points, logweights=quadrature(FIT_NODES)
    stress=np.array([float(r["stress_amplitude_MPa"]) for r in exact_wu])
    life=np.array([float(r["cycles_failure_or_bound"]) for r in exact_wu])
    events=np.array([int(r["failure_event_1"]) for r in exact_wu])
    terms=conditional_logterms(params,stress,life,events,.25*points)
    lp=logweights+terms.sum(axis=0)
    p=np.exp(lp-lp.max());p/=p.sum()
    return .25*points,p

def generated(fold,seed,params,wu):
    rng=np.random.default_rng(seed)
    b,p=posterior_nodes(params,wu)
    source_offset=float(rng.choice(b,p=p)) # one offset per source replicate, not one per row
    source_stress=np.array([float(r["stress_amplitude_MPa"]) for r in wu])
    k=math.exp(float(params[2]));result=[];ledger=[]
    for i in range(DRAW_N):
        stress=float(rng.choice(source_stress))
        latent_z=float(params[0]+params[1]*math.log2(stress/100)+source_offset+
                       math.log10(rng.exponential())/k)
        if not math.isfinite(latent_z) or not 0<=latent_z<=12:
            raise RuntimeError("Simulated latent log-life outside feasibility guard")
        latent_cycles=10**latent_z
        event=int(latent_cycles<=STOP_WU)
        cycles=latent_cycles if event else STOP_WU
        rid=f"SYN:{fold}:seed{seed}:{i:02d}"
        result.append(dict(record_id=rid,study_id="Wu_2021",stress_amplitude_MPa=stress,
                           cycles_failure_or_bound=cycles,failure_event_1=event))
        ledger.append(dict(record_id=rid,source="Wu_2021",fold=fold,seed=seed,
                           synthetic=True,training_only=True,stress_amplitude_MPa=stress,
                           latent_log10_cycles=latent_z,observed_cycles_or_bound=cycles,
                           failure_event_1=event,stop_cycles=STOP_WU,
                           sampled_source_offset_log10=source_offset))
    return result,ledger

def main():
    ap=argparse.ArgumentParser()
    for key in ("exact","manifest","graph","base_parameters","base_metrics","out"):
        ap.add_argument("--"+key.replace("_","-"),type=Path,required=True)
    a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=True)
    if sha(a.exact)!="29aff38de63880dbfbaf65d3b876b81bd5afabfaaaac1615e2e503fbfa661a30":raise ValueError("Exact hash changed")
    if sha(a.manifest)!="0df2fdec2399cae1c76c202a323691431bdc96bb9eb31fa278f6b307ac84eb91":raise ValueError("Manifest hash changed")
    exact=read_csv(a.exact);graph=read_csv(a.graph);manifest=read_csv(a.manifest)
    assert len(exact)==66 and len(graph)==53
    baseline={r["fold"]:r for r in read_csv(a.base_parameters) if r["case"]=="cap5_center"}
    baseline_metrics={r["fold"]:r for r in read_csv(a.base_metrics) if r["case"]=="cap5_center"}
    assert len(baseline)==len(baseline_metrics)==3
    by_id={r["record_id"]:r for r in exact}
    scores=[];ledger_all=[];preds=[]
    for fold in FOLDS:
        members=[r for r in manifest if r["analysis"]=="primary_exact_LOSO" and r["fold_id"]==fold]
        train=[by_id[r["record_key"].removeprefix("EXACT:")] for r in members if r["role"]=="train"]
        test=[by_id[r["record_key"].removeprefix("EXACT:")] for r in members if r["role"]=="test"]
        assert len(members)==66 and {r["study_id"] for r in test}=={fold.removeprefix("E0_")}
        assert not {r["study_id"] for r in train}&{r["study_id"] for r in test}
        base=baseline[fold]
        base_params=np.array([float(base["alpha"]),float(base["beta"]),math.log(float(base["shape_k"]))])
        pred0,nll0,med0,_=score(base_params,test)
        assert abs(float(nll0.mean())-float(baseline_metrics[fold]["augmented_mean_nll"]))<1e-9
        graphtrain=graph_rows(graph,5.,"center","both")
        exact_wu=[r for r in train if r["study_id"]=="Wu_2021"]
        if exact_wu:
            assert len(exact_wu)==41
            assert {int(r["cycles_failure_or_bound"]) for r in exact_wu if r["failure_event_1"]=="0"}=={STOP_WU}
        # No Romano global stop is inferred from its single 8,889,311 runout.
        for seed in SEEDS:
            if exact_wu:synthetic,ledger=generated(fold,seed,base_params,exact_wu)
            else:synthetic,ledger=[],[]
            ledger_all.extend(ledger)
            for cap in CAPS:
                weighted=[dict(r,weight=cap/DRAW_N) for r in synthetic]
                if not weighted:
                    params=base_params;obj_delta=0.;status="no_eligible_training_source"
                else:
                    fitted,obj_delta=fit(train,graphtrain+weighted,base_params)
                    params=fitted.x;status="fit"
                pred,nll,med,pred_delta=score(params,test)
                events=np.array([int(r["failure_event_1"]) for r in test])
                change=nll-nll0
                scores.append(dict(fold=fold,seed=seed,cap=cap,eligibility=status,
                    exact_train_n=len(train),graph_train_n=len(graphtrain),synthetic_train_n=len(weighted),
                    synthetic_effective_weight=sum(r["weight"] for r in weighted),
                    synthetic_fail=sum(r["failure_event_1"] for r in weighted),
                    synthetic_runout=len(weighted)-sum(r["failure_event_1"] for r in weighted),
                    test_n=len(test),test_fail=int(events.sum()),test_runout=int(len(test)-events.sum()),
                    base_mean_nll=float(nll0.mean()),synthetic_mean_nll=float(nll.mean()),
                    synthetic_minus_base_mean_nll=float(change.mean()),
                    failure_mean_nll_change=float(change[events==1].mean()),
                    runout_mean_nll_change=float(change[events==0].mean()) if (events==0).any() else "",
                    objective_delta_161_321=obj_delta,predictive_delta_161_321=pred_delta))
                for i,r in enumerate(test):
                    preds.append(dict(fold=fold,seed=seed,cap=cap,record_id=r["record_id"],
                        event=int(events[i]),base_nll=float(nll0[i]),synthetic_nll=float(nll[i]),
                        synthetic_minus_base_nll=float(change[i]),
                        base_median_log10=float(med0[i]),synthetic_median_log10=float(med[i])))
                print(fold,"seed",seed,"cap",cap,"syn",len(weighted),"delta",round(float(change.mean()),4),flush=True)
    assert len(scores)==30 and len(preds)==660 and len(ledger_all)==200
    assert all(r["record_id"].startswith("SYN:") for r in ledger_all)
    assert not {r["record_id"] for r in ledger_all}&set(by_id)
    write_csv(a.out/"synthetic_feasibility_scores_30.csv",scores)
    write_csv(a.out/"synthetic_training_episodes_200.csv",ledger_all)
    write_csv(a.out/"paired_exact_predictions_660.csv",preds)
    meta=dict(status="exploratory parametric-bootstrap self-distillation, not a novel algorithm or independent evidence",
              generator="posterior training-source offset; empirical training stress; Weibull latent life; Wu documented stop at 1e7",
              no_source_wide_stop_for_Romano="single first-exposure bound 8,889,311 not generalized",
              no_stop_for_Chen="no censored observation in frozen exact cohort",
              only_Wu_generates="therefore held-out Wu fold has no synthetic rows and is a zero-change control",
              graphical_training="53 failures, both graph sources capped at five effective contributions each",
              tau=.25,seeds=list(SEEDS),synthetic_rows_per_eligible_source=DRAW_N,
              synthetic_caps=list(CAPS),no_synthetic_test_rows=True,no_external_test=True,
              input_hashes={"exact":sha(a.exact),"manifest":sha(a.manifest),"graph53":sha(a.graph),
                            "base_parameters":sha(a.base_parameters),"base_metrics":sha(a.base_metrics)},
              software={"python":platform.python_version(),"numpy":np.__version__,"scipy":scipy.__version__})
    (a.out/"run_metadata.json").write_text(json.dumps(meta,indent=2)+"\n")
    print("done",a.out)

if __name__=="__main__":main()
