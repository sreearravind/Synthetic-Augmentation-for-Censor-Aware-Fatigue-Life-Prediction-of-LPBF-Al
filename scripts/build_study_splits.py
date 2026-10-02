#!/usr/bin/env python3
"""Freeze study-level validation membership; this script never fits a model."""

import argparse
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path


def read_csv(path):
    with path.open(newline='', encoding='utf-8') as handle:
        return list(csv.DictReader(handle))


def write_csv(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', newline='', encoding='utf-8') as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--root', type=Path, default=Path('.'), help='Repository root')
    parser.add_argument('--output', type=Path, default=None, help='Output directory')
    args = parser.parse_args()
    root = args.root
    sources = {
        'smooth': root / 'data/cohorts/smooth_core_66.csv',
        'confirmed': root / 'data/cohorts/confirmed_outcomes_75.csv',
        'graph': root / 'data/graph_digitized/independent_sources_26_approximate.csv',
    }
    # Accept the local extraction tree when generating before a repo checkout.
    if not sources['smooth'].exists():
        sources = {
            'smooth': root / 'no_author_dependency/smooth_core_66.csv',
            'confirmed': root / 'no_author_dependency/confirmed_outcomes_75.csv',
            'graph': root / 'graph_digitized/graph_approximate_26.csv',
        }
    raw = {key: read_csv(path) for key, path in sources.items()}
    assert (len(raw['smooth']), len(raw['confirmed']), len(raw['graph'])) == (66, 75, 26)
    smooth_ids = {r['record_id'] for r in raw['smooth']}
    assert len(smooth_ids) == 66
    assert smooth_ids.issubset({r['record_id'] for r in raw['confirmed']})
    notch = [r for r in raw['confirmed'] if r['record_id'] not in smooth_ids]
    assert len(notch) == 9 and all(r['study_id'] == 'Chen_2024' and
                                    r['stress_basis'] == 'local maximum at notch' for r in notch)

    def exact(row, tier):
        assert row['failure_event_1'] in ('0', '1')
        assert (row['failure_event_1'] == '1') == (row['bound_operator'] == '=')
        return dict(record_key='EXACT:' + row['record_id'], study_id=row['study_id'],
                    tier=tier, event_failure=int(row['failure_event_1']),
                    cycles_or_bound=int(row['cycles_failure_or_bound']),
                    stress_ratio_R=row['stress_ratio_R'])

    def graph(row):
        assert row['event_failure'] in ('0', '1')
        assert row['precision_tier'] in ('graph_approximate', 'stress_exact_life_graph_approximate')
        return dict(record_key='GRAPH:' + row['source_key'] + ':' + row['record_id'],
                    study_id=row['source_key'], tier='graph_approximate',
                    event_failure=int(row['event_failure']),
                    cycles_or_bound=int(row['cycles_for_censor_model']),
                    stress_ratio_R=row['stress_ratio_R'])

    exact66 = [exact(r, 'source_table_exact_smooth') for r in raw['smooth']]
    graph26 = [graph(r) for r in raw['graph']]
    notch9 = [exact(r, 'source_table_exact_notch') for r in notch]
    all75 = exact66 + notch9
    assert len({r['record_key'] for r in exact66 + graph26 + notch9}) == 101

    folds = []
    membership = []
    exact_studies = ['Wu_2021', 'Romano_2018', 'Chen_2024']
    graph_studies = ['Zhang_2022', 'Glodez_2020']

    def add_fold(fold_id, analysis, universe, roles, interpretation):
        assert set(roles) == {r['study_id'] for r in universe}
        counts = Counter()
        study_roles = {}
        for row in universe:
            role = roles[row['study_id']]
            counts[(role, 'total')] += 1
            counts[(role, 'failure')] += row['event_failure']
            counts[(role, 'runout')] += 1-row['event_failure']
            study_roles[row['study_id']] = role
            membership.append(dict(fold_id=fold_id, analysis=analysis,
                                   record_key=row['record_key'], study_id=row['study_id'],
                                   tier=row['tier'], role=role,
                                   event_failure=row['event_failure'],
                                   cycles_or_bound=row['cycles_or_bound'],
                                   stress_ratio_R=row['stress_ratio_R']))
        assert counts[('train', 'total')] and counts[('test', 'total')]
        folds.append(dict(fold_id=fold_id, analysis=analysis,
                          train_studies=';'.join(s for s in roles if roles[s] == 'train'),
                          test_studies=';'.join(s for s in roles if roles[s] == 'test'),
                          excluded_studies=';'.join(s for s in roles if roles[s] == 'exclude'),
                          train_n=counts[('train', 'total')],
                          train_fail=counts[('train', 'failure')],
                          train_runout=counts[('train', 'runout')],
                          test_n=counts[('test', 'total')],
                          test_fail=counts[('test', 'failure')],
                          test_runout=counts[('test', 'runout')],
                          excluded_n=counts[('exclude', 'total')],
                          interpretation=interpretation))

    for held in exact_studies:
        add_fold('E0_' + held, 'primary_exact_LOSO', exact66,
                 {s: 'test' if s == held else 'train' for s in exact_studies},
                 'Independent exact-data source holdout; paired with E1')
    for held in exact_studies:
        add_fold('E1_' + held, 'graph_assisted_exact_LOSO', exact66 + graph26,
                 {**{s: 'test' if s == held else 'train' for s in exact_studies},
                  **{s: 'train' for s in graph_studies}},
                 'Same exact test IDs as E0; graph tier augments training only')
    for held in graph_studies:
        add_fold('X0_' + held, 'external_graph_test', exact66 + graph26,
                 {**{s: 'train' for s in exact_studies},
                  **{s: 'test' if s == held else 'exclude' for s in graph_studies}},
                 'Unseen R=0 approximate test; domain-shift diagnostic only')
    # Chen notched specimens are outside the smooth core but share its study.
    # Use a distinct role for Chen R5 rows to avoid treating the source as new.
    universe_n = exact66 + notch9
    for row in universe_n:
        role = 'test' if row['tier'] == 'source_table_exact_notch' else 'train'
        membership.append(dict(fold_id='N0_Chen_R5', analysis='within_study_notch_transfer',
                               record_key=row['record_key'], study_id=row['study_id'],
                               tier=row['tier'], role=role,
                               event_failure=row['event_failure'],
                               cycles_or_bound=row['cycles_or_bound'],
                               stress_ratio_R=row['stress_ratio_R']))
    folds.append(dict(fold_id='N0_Chen_R5', analysis='within_study_notch_transfer',
                      train_studies=';'.join(exact_studies), test_studies='Chen_2024:R5_notched',
                      excluded_studies='', train_n=66, train_fail=57, train_runout=9,
                      test_n=9, test_fail=9, test_runout=0, excluded_n=0,
                      interpretation='Within Chen study: geometry transfer only; not external validation'))

    assert len(folds) == 9 and len(membership) == 733
    output = args.output or root / 'data/validation'
    write_csv(output / 'study_holdout_folds_2026-10-02.csv', folds)
    write_csv(output / 'record_membership_2026-10-02.csv', membership)
    source_hashes = {key: hashlib.sha256(path.read_bytes()).hexdigest()
                     for key, path in sources.items()}
    (output / 'input_hashes_2026-10-02.json').write_text(
        json.dumps({'input_sha256': source_hashes, 'repository_source_paths': {
                    'smooth': 'data/cohorts/smooth_core_66.csv',
                    'confirmed': 'data/cohorts/confirmed_outcomes_75.csv',
                    'graph': 'data/graph_digitized/independent_sources_26_approximate.csv'},
                    'split_rule': 'study_id exclusive, except N0 within-study geometry transfer',
                    'fold_count': 9, 'membership_rows': 733}, indent=2) + '\n',
        encoding='utf-8')
    print(json.dumps({'folds': len(folds), 'membership_rows': len(membership),
                      'source_hashes': source_hashes, 'output': str(output)}))


if __name__ == '__main__':
    main()
