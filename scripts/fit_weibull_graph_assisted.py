#!/usr/bin/env python3
"""Frozen E1 paired study holdouts with approximate graph data in training.

This reuses the exact E0 Weibull model, objective, bounds, and held-out IDs.
Graph perturbations are deterministic reading scenarios, not confidence limits.
"""

import argparse
import csv
import hashlib
import json
import math
import platform
from pathlib import Path

import numpy as np
import scipy

from fit_weibull_exact_baseline import fit, rows, score_one, write_rows


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def adapted_graph(r, stress_position, life_position):
    assert r['stress_ratio_R'] == '0' and r['stress_metric'] == 'sigma_max'
    assert r['event_failure'] in ('0','1')
    low=float(r['sigma_max_read_low_MPa'])/2
    mid=float(r['stress_amp_MPa'])
    high=float(r['sigma_max_read_high_MPa'])/2
    assert low<=mid+0.06 and mid<=high+0.06 and abs(2*mid-float(r['stress_max_MPa']))<=0.11
    stress={-1:low,0:mid,1:high}[stress_position]
    ev=int(r['event_failure'])
    if ev:
        life={-1:10**float(r['log10N_read_low']),
              0:float(r['cycles_plotted_approx']),
              1:10**float(r['log10N_read_high'])}[life_position]
    else:
        life=float(r['cycles_for_censor_model'])
    assert stress>0 and life>0
    return dict(record_id='GRAPH:'+r['source_key']+':'+r['record_id'],
                study_id=r['source_key'],stress_amplitude_MPa=stress,
                cycles_failure_or_bound=life,failure_event_1=ev,
                stress_ratio_R='0')


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--root',type=Path,default=Path('.'),help='Repository root')
    ap.add_argument('--baseline',type=Path,default=None,help='Exact E0 results directory')
    ap.add_argument('--output',type=Path,default=None)
    a=ap.parse_args()
    exact_path=a.root/'data/cohorts/smooth_core_66.csv'
    graph_path=a.root/'data/graph_digitized/independent_sources_26_approximate.csv'
    membership_path=a.root/'data/validation/record_membership_2026-10-02.csv'
    if not exact_path.exists():
        exact_path=a.root/'no_author_dependency/smooth_core_66.csv'
        graph_path=a.root/'graph_digitized/graph_approximate_26.csv'
        membership_path=a.root/'validation/record_membership_2026-10-02.csv'
    hash_path=membership_path.parent/'input_hashes_2026-10-02.json'
    hashes=json.loads(hash_path.read_text(encoding='utf-8'))['input_sha256']
    assert digest(exact_path)==hashes['smooth'] and digest(graph_path)==hashes['graph']
    exact=rows(exact_path);graph=rows(graph_path)
    assert len(exact)==66 and len(graph)==26
    exact_by_key={'EXACT:'+r['record_id']:r for r in exact}
    graph_by_key={'GRAPH:'+r['source_key']+':'+r['record_id']:r for r in graph}
    assert len(exact_by_key)==66 and len(graph_by_key)==26
    membership=[r for r in rows(membership_path) if r['analysis']=='graph_assisted_exact_LOSO']
    assert len(membership)==276
    baseline=a.baseline or a.root/'results/exact_weibull_baseline'
    if not baseline.exists():
        baseline=a.root/'validation/baseline_E0'
    e0_preds=rows(baseline/'heldout_predictions_E0_66.csv')
    e0_metrics={r['fold_id'].removeprefix('E0_'):r for r in rows(baseline/'fold_metrics_E0_3.csv')}
    e0_by_id={r['record_id']:r for r in e0_preds}
    assert len(e0_by_id)==66 and len(e0_preds)==66
    out=a.output or a.root/'results/graph_assisted_weibull'
    out.mkdir(parents=True,exist_ok=True)

    scenarios=[(f'S{s:+d}_L{l:+d}',s,l,False) for s in (-1,0,1) for l in (-1,0,1)]
    scenarios.append(('CENTER_without_Z05',0,0,True))
    preds=[];metrics=[];coeffs=[];paired=[];record_deltas=[]
    exact_studies=['Wu_2021','Romano_2018','Chen_2024']
    for label,spos,lpos,drop_z05 in scenarios:
        graph_adapt={key:adapted_graph(r,spos,lpos) for key,r in graph_by_key.items()
                     if not (drop_z05 and key=='GRAPH:Zhang_2022:Z05')}
        for study in exact_studies:
            fold_id='E1_'+study
            members=[r for r in membership if r['fold_id']==fold_id]
            train_exact=[exact_by_key[r['record_key']] for r in members
                         if r['role']=='train' and r['tier']=='source_table_exact_smooth']
            test=[exact_by_key[r['record_key']] for r in members if r['role']=='test']
            graph_keys={r['record_key'] for r in members if r['role']=='train' and r['tier']=='graph_approximate'}
            assert graph_keys==set(graph_by_key)
            train=train_exact+[graph_adapt[k] for k in sorted(graph_keys) if k in graph_adapt]
            assert {r['record_id'] for r in test}=={r['record_id'] for r in exact if r['study_id']==study}
            assert not ({r['study_id'] for r in train}&{r['study_id'] for r in test})
            assert len(train)==(len(train_exact)+(25 if drop_z05 else 26))
            sol,_=fit(train)
            alpha,beta,logk=map(float,sol.x)
            coeffs.append(dict(scenario=label,fold_id=fold_id,train_n=len(train),
                               train_exact_n=len(train_exact),train_graph_n=len(train)-len(train_exact),
                               train_fail=sum(int(r['failure_event_1']) for r in train),
                               train_runout=sum(1-int(r['failure_event_1']) for r in train),
                               alpha_log10_scale_at_100MPa=alpha,
                               beta_log10_scale_per_stress_doubling=beta,
                               weibull_shape_k=math.exp(logk),
                               training_negative_log_likelihood=float(sol.fun),
                               optimizer_success=bool(sol.success),
                               beta_at_constraint=int(beta<=-11.999999 or beta>=-0.000001),
                               k_at_constraint=int(logk<=-3.999999 or logk>=2.999999)))
            fold_pred=[]
            for r in test:
                base=e0_by_id[r['record_id']]
                assert base['fold_id']=='E0_'+study
                assert int(base['event_failure'])==int(r['failure_event_1'])
                assert int(base['cycles_or_bound'])==int(r['cycles_failure_or_bound'])
                assert float(base['stress_amplitude_MPa'])==float(r['stress_amplitude_MPa'])
                ev=int(r['failure_event_1']);life=float(r['cycles_failure_or_bound'])
                stress=float(r['stress_amplitude_MPa'])
                mu,med,nll,fail_term,cens_term,_=score_one(sol.x,stress,life,ev)
                assert math.isfinite(nll)
                item=dict(scenario=label,fold_id=fold_id,record_id=r['record_id'],
                          study_id=study,event_failure=ev,cycles_or_bound=int(life),
                          stress_amplitude_MPa=stress,stress_ratio_R=float(r['stress_ratio_R']),
                          predicted_log10_weibull_scale=mu,predicted_log10_median_life=med,
                          censored_negative_log_likelihood=nll,
                          failure_density_NLL_component=fail_term if ev else '',
                          runout_survival_NLL_component=cens_term if not ev else '')
                fold_pred.append(item)
                if label=='S+0_L+0':
                    preds.append(item)
                    e0nll=float(base['censored_negative_log_likelihood'])
                    e0median=float(base['predicted_log10_median_life'])
                    observed=math.log10(life) if ev else None
                    record_deltas.append(dict(record_id=r['record_id'],fold_id=fold_id,
                        event_failure=ev,E0_NLL=e0nll,E1_NLL=nll,E1_minus_E0_NLL=nll-e0nll,
                        E0_failure_absolute_log10_error=abs(e0median-observed) if ev else '',
                        E1_failure_absolute_log10_error=abs(med-observed) if ev else '',
                        E1_minus_E0_failure_absolute_error=(abs(med-observed)-abs(e0median-observed)) if ev else ''))
            failure=[p for p in fold_pred if p['event_failure']==1]
            mean_nll=sum(p['censored_negative_log_likelihood'] for p in fold_pred)/len(fold_pred)
            mae=sum(abs(p['predicted_log10_median_life']-math.log10(p['cycles_or_bound'])) for p in failure)/len(failure)
            total_cens=sum(p['runout_survival_NLL_component'] for p in fold_pred if not p['event_failure'])
            metrics.append(dict(scenario=label,fold_id=fold_id,held_out_study=study,
                                train_exact_n=len(train_exact),train_graph_n=len(train)-len(train_exact),
                                test_n=len(test),test_fail=len(failure),test_runout=len(test)-len(failure),
                                mean_censored_NLL_log10_density=mean_nll,
                                failure_only_MAE_log10_cycles=mae,
                                total_runout_survival_NLL=total_cens))
            if label=='S+0_L+0':
                e0=e0_metrics[study]
                paired.append(dict(held_out_study=study,test_n=len(test),
                    test_fail=len(failure),test_runout=len(test)-len(failure),
                    E0_mean_censored_NLL=float(e0['mean_censored_NLL_log10_density']),
                    E1_mean_censored_NLL=mean_nll,E1_minus_E0_mean_NLL=mean_nll-float(e0['mean_censored_NLL_log10_density']),
                    E0_failure_only_MAE=float(e0['failure_only_MAE_log10_cycles']),
                    E1_failure_only_MAE=mae,E1_minus_E0_failure_MAE=mae-float(e0['failure_only_MAE_log10_cycles']),
                    E0_runout_survival_NLL=float(e0['total_runout_survival_NLL']),
                    E1_runout_survival_NLL=total_cens))

    assert len(metrics)==len(coeffs)==30 and len(preds)==len(record_deltas)==66 and len(paired)==3
    write_rows(out/'heldout_predictions_E1_center_66.csv',preds)
    write_rows(out/'paired_record_deltas_E0_E1_66.csv',record_deltas)
    write_rows(out/'paired_fold_metrics_E0_E1_3.csv',paired)
    write_rows(out/'scenario_fold_metrics_E1_30.csv',metrics)
    write_rows(out/'scenario_parameters_E1_30.csv',coeffs)
    meta={'inputs_sha256':{str(exact_path.relative_to(a.root)):digest(exact_path),
                           str(graph_path.relative_to(a.root)):digest(graph_path),
                           str(membership_path.relative_to(a.root)):digest(membership_path),
                           'E0_heldout_predictions':digest(baseline/'heldout_predictions_E0_66.csv'),
                           'E0_fold_metrics':digest(baseline/'fold_metrics_E0_3.csv')},
          'software_versions':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__},
          'model':'Exactly E0 Weibull AFT stress-only shape and fixed optimization bounds',
          'graph_stress':'R=0: stress amplitude = graph maximum stress / 2; stored center is rounded',
          'graph_failure_life':'center plotted approximate cycles; lower/upper from recorded log10 reading bounds',
          'graph_runout':'paper-supported survival bound fixed across scenarios; only stress changes',
          'uncertainty_scenarios':'3x3 common-direction lower/center/upper stress and failure life across graph rows; not a confidence interval',
          'additional_scenario':'central graph rows excluding flagged Zhang Z05',
          'test_rule':'unchanged exact E0 test rows; no graph or synthetic record in test'}
    (out/'run_metadata_E1.json').write_text(json.dumps(meta,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'paired':paired,'scenario_metrics':metrics,'coefficients':coeffs,'output':str(out)},allow_nan=False))


if __name__=='__main__':
    main()
