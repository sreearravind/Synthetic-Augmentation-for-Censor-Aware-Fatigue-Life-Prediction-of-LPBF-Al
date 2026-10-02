#!/usr/bin/env python3
"""Exploratory source/outcome ablations on frozen exact study holdouts.

These are diagnostics. Selecting a variant by these test scores would reuse
the held-out studies and invalidate a later confirmatory comparison.
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

from fit_weibull_exact_baseline import fit, rows, score_one, write_rows
from fit_weibull_graph_assisted import adapted_graph


VARIANTS = ('exact_only','zhang_only','glodez_only',
            'graph_failures_only','graph_runouts_only','both_graph_sources')


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def selected_graph(r, variant):
    if variant=='exact_only':return False
    if variant=='zhang_only':return r['source_key']=='Zhang_2022'
    if variant=='glodez_only':return r['source_key']=='Glodez_2020'
    if variant=='graph_failures_only':return r['event_failure']=='1'
    if variant=='graph_runouts_only':return r['event_failure']=='0'
    if variant=='both_graph_sources':return True
    raise ValueError(variant)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--root',type=Path,default=Path('.'))
    ap.add_argument('--baseline',type=Path,default=None)
    ap.add_argument('--output',type=Path,default=None)
    a=ap.parse_args()
    exact_path=a.root/'data/cohorts/smooth_core_66.csv'
    graph_path=a.root/'data/graph_digitized/independent_sources_26_approximate.csv'
    membership_path=a.root/'data/validation/record_membership_2026-10-02.csv'
    if not exact_path.exists():
        exact_path=a.root/'no_author_dependency/smooth_core_66.csv'
        graph_path=a.root/'graph_digitized/graph_approximate_26.csv'
        membership_path=a.root/'validation/record_membership_2026-10-02.csv'
    frozen=json.loads((membership_path.parent/'input_hashes_2026-10-02.json').read_text())['input_sha256']
    assert sha(exact_path)==frozen['smooth'] and sha(graph_path)==frozen['graph']
    exact=rows(exact_path);graph=rows(graph_path)
    membership=[r for r in rows(membership_path) if r['analysis']=='graph_assisted_exact_LOSO']
    assert len(exact)==66 and len(graph)==26 and len(membership)==276
    exact_by={'EXACT:'+r['record_id']:r for r in exact}
    graph_by={'GRAPH:'+r['source_key']+':'+r['record_id']:r for r in graph}
    baseline=a.baseline or a.root/'results/exact_weibull_baseline'
    if not baseline.exists():baseline=a.root/'validation/baseline_E0'
    e0={r['held_out_study']:r for r in rows(baseline/'fold_metrics_E0_3.csv')}
    out=a.output or a.root/'results/graph_tradeoff_diagnostic'
    out.mkdir(parents=True,exist_ok=True)

    source_summary=[]
    for study in ('Wu_2021','Romano_2018','Chen_2024','Zhang_2022','Glodez_2020'):
        if study in ('Zhang_2022','Glodez_2020'):
            items=[r for r in graph if r['source_key']==study]
            stress=[float(r['stress_amp_MPa']) for r in items]
            ev=[int(r['event_failure']) for r in items]
            cycles=[float(r['cycles_for_censor_model']) for r in items]
            tier='graph_approximate'
        else:
            items=[r for r in exact if r['study_id']==study]
            stress=[float(r['stress_amplitude_MPa']) for r in items]
            ev=[int(r['failure_event_1']) for r in items]
            cycles=[float(r['cycles_failure_or_bound']) for r in items]
            tier='source_table_exact'
        source_summary.append(dict(study_id=study,tier=tier,n=len(items),
                                   failures=sum(ev),runouts=len(ev)-sum(ev),
                                   stress_ratio_R=';'.join(sorted({r['stress_ratio_R'] for r in items})),
                                   stress_amp_min_MPa=min(stress),stress_amp_max_MPa=max(stress),
                                   min_failure_cycles=int(min(c for c,e in zip(cycles,ev) if e)),
                                   max_failure_cycles=int(max(c for c,e in zip(cycles,ev) if e)),
                                   runout_bounds_cycles=';'.join(str(int(c)) for c,e in zip(cycles,ev) if not e)))

    metrics=[];parameters=[]
    for variant in VARIANTS:
        selected={key:adapted_graph(r,0,0) for key,r in graph_by.items()
                  if selected_graph(r,variant)}
        for study in ('Wu_2021','Romano_2018','Chen_2024'):
            m=[r for r in membership if r['fold_id']=='E1_'+study]
            tr=[exact_by[r['record_key']] for r in m
                if r['role']=='train' and r['tier']=='source_table_exact_smooth']
            te=[exact_by[r['record_key']] for r in m if r['role']=='test']
            train=tr+[selected[k] for k in sorted(selected)]
            assert {r['study_id'] for r in te}=={study}
            assert not {r['study_id'] for r in tr}&{study}
            assert len(te)==int(e0[study]['test_n'])
            sol,_=fit(train)
            losses=[];failed=[];censored=[];errors=[]
            for r in te:
                n=float(r['cycles_failure_or_bound']);ev=int(r['failure_event_1'])
                _,median,nll,failpart,censorpart,_=score_one(sol.x,float(r['stress_amplitude_MPa']),n,ev)
                assert math.isfinite(nll)
                losses.append(nll)
                if ev:
                    failed.append(failpart)
                    errors.append(abs(median-math.log10(n)))
                else:censored.append(censorpart)
            total_fail=sum(failed);total_cens=sum(censored)
            metrics.append(dict(variant=variant,held_out_study=study,
                                train_exact_n=len(tr),train_graph_n=len(selected),
                                train_graph_fail=sum(int(r['failure_event_1']) for r in selected.values()),
                                train_graph_runout=sum(1-int(r['failure_event_1']) for r in selected.values()),
                                test_n=len(te),test_fail=len(failed),test_runout=len(censored),
                                mean_censored_NLL=sum(losses)/len(te),
                                failure_density_NLL_sum=total_fail,
                                runout_survival_NLL_sum=total_cens,
                                failure_only_MAE_log10_cycles=sum(errors)/len(errors),
                                delta_mean_NLL_vs_E0=sum(losses)/len(te)-float(e0[study]['mean_censored_NLL_log10_density']),
                                delta_failure_NLL_sum_vs_E0=total_fail-float(e0[study]['total_failure_density_NLL']),
                                delta_runout_NLL_sum_vs_E0=total_cens-float(e0[study]['total_runout_survival_NLL'])))
            alpha,beta,logk=map(float,sol.x)
            parameters.append(dict(variant=variant,held_out_study=study,
                                   alpha_log10_scale_at_100MPa=alpha,
                                   beta_log10_scale_per_stress_doubling=beta,
                                   weibull_shape_k=math.exp(logk),
                                   optimizer_success=bool(sol.success),
                                   beta_at_constraint=int(beta<=-11.999999 or beta>=-0.000001),
                                   k_at_constraint=int(logk<=-3.999999 or logk>=2.999999)))
    assert len(metrics)==len(parameters)==18
    for r in metrics:
        if r['variant']=='exact_only':
            assert abs(r['delta_mean_NLL_vs_E0'])<1e-8
    write_rows(out/'source_summary_5.csv',source_summary)
    write_rows(out/'ablation_fold_metrics_18.csv',metrics)
    write_rows(out/'ablation_parameters_18.csv',parameters)
    meta={'purpose':'Exploratory source and outcome decomposition; do not select model or graph weights by held-out score',
          'variants':list(VARIANTS),
          'input_sha256':{'smooth':sha(exact_path),'graph':sha(graph_path),
                          'membership':sha(membership_path),'E0_metrics':sha(baseline/'fold_metrics_E0_3.csv')},
          'software_versions':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__},
          'model':'same stress-only Weibull AFT, optimization bounds and exact held-out rows as E0/E1',
          'graph_failure_only_and_runout_only':'selection on outcome solely for mechanism diagnosis, never a proposed training protocol'}
    (out/'run_metadata_diagnostic.json').write_text(json.dumps(meta,indent=2)+'\n')
    print(json.dumps({'metrics':metrics,'parameters':parameters,'sources':source_summary,'output':str(out)},allow_nan=False))


if __name__=='__main__':
    main()
