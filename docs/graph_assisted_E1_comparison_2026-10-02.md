# Graph-assisted training against the exact-only baseline

**Run date:** 2 October 2026. This is the frozen **E1** comparison. In each leave-one-study-out fold, the same stress-only Weibull model and likelihood as E0 were fitted to the two available exact studies **plus 26 approximate graph-derived experimental rows**. Each test set contains exactly the same untouched exact specimens as its E0 counterpart. No graph record entered a test set, and no synthetic data were created.

## Paired held-out scores

Lower mean censored negative log-likelihood (NLL) and lower failure-only log-cycle MAE are better. \(\Delta=\mathrm{E1}-\mathrm{E0}\), so a positive delta is worse. NLL uses a log10-cycle density for failures and survival beyond the reported bound for runouts.

| Exact study held out | Test, failure/runout | E0 NLL | E1 NLL | \(\Delta\) NLL | E0 failure MAE | E1 failure MAE |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Wu 2021 | 41, 33/8 | 1.345 | 2.149 | **+0.805** | 0.586 | 2.102 |
| Romano 2018 | 7, 6/1 | 2.640 | 1.648 | **−0.992** | 0.356 | 0.358 |
| Chen 2024 smooth | 18, 18/0 | 1.058 | 1.417 | **+0.359** | 0.287 | 0.449 |

At the **record level**, E1 gives a worse failure-density contribution on **all 57 exact failures** and a better survival contribution on **all nine exact runouts**. Thus the Romano NLL gain is driven by its single runout: its contribution falls from 13.020 to 3.335, while the summed six failure-density contributions rise. Wu's runouts also improve (summed contribution 14.206 → 2.547), but its failure contributions worsen enough for its overall score to deteriorate. Chen has no runouts and worsens on failure scoring. This is a diagnostic of the fitted distribution's trade-off, not proof that the graph data caused a physical effect.

| Exact study held out | E0 shape \(k\) | E1 shape \(k\) | E1 stress slope \(\beta\) |
| --- | ---: | ---: | ---: |
| Wu 2021 | 0.541 | 0.432 | −2.500 |
| Romano 2018 | 0.601 | 0.377 | −1.136 |
| Chen 2024 smooth | 0.461 | 0.348 | −1.076 |

The smaller E1 shape parameters are consistent with a broader fitted life distribution at fixed stress. They do not explain away the changes in stress ratio, material preparation or study protocol.

## Graph-reading sensitivity

The graph tier remains approximate. Nine deterministic scenarios combine lower/center/upper **stress readings** with lower/center/upper **failure-life readings** for the graph records. Graph-runout event status and paper-supported survival bound are fixed throughout. A tenth scenario excludes the flagged Zhang marker Z05 at the center reading. These are coordinated perturbations of chart readings, **not** confidence intervals or 9× independent new datasets.

| Exact study held out | E0 NLL | E1 range across 9 reading scenarios | E1 excluding Z05 |
| --- | ---: | ---: | ---: |
| Wu 2021 | 1.345 | 2.112–2.183 | 2.108 |
| Romano 2018 | 2.640 | 1.643–1.663 | 1.655 |
| Chen 2024 smooth | 1.058 | 1.396–1.439 | 1.371 |

The direction of each paired comparison persists in these specified reading checks. They **do not** address unmeasured source differences, uncertainty in the Z05 outcome itself, or the small number of independent studies. The Z05 exclusion changes the training count from 26 to 25 graph records, not any held-out exact test count.

## Stress harmonization and interpretation

- E0 and E1 use the exact same source-table stress amplitude for every exact row. For graph studies with \(R=0\), E1 uses \(\sigma_a=\sigma_{\max}/2\); the Zhang chart has approximate maximum stresses, while Glodež Table 2 prints exact amplitudes. Stress reading bounds are propagated to the training sensitivity checks.
- The shared model only sees stress amplitude. It does **not** model stress ratio, surface/thermal conditions, geometry, frequency, source identity, or label precision. Zhang and Glodež both have \(R=0\), whereas exact training has \(R=0.1\) and, for some folds, \(R=-1\). Their 26 graph points can outweigh a small exact training fold (Wu's E1 fold: 26 graph and 25 exact records).
- Exact source holdouts remain out of support in many cases: 32/41 Wu and 6/7 Romano test stresses fall outside the exact E0 training stress range, and Romano's \(R=-1\) is unseen in exact training. The E1 training range changes, but the mixed-source model still does not resolve stress-ratio confounding.
- The graph-reading checks show that pixel precision alone is unlikely to account for these results. They cannot distinguish source heterogeneity from the effect of adding right-censored high-life tests. Do not describe E1 as a demonstrated improvement or a validation of a new algorithm.

## Reproducibility

`paired_fold_metrics_E0_E1_3.csv` reports the central paired result; `paired_record_deltas_E0_E1_66.csv` shows its failure/runout contributions; `heldout_predictions_E1_center_66.csv` stores all central exact test predictions. `scenario_fold_metrics_E1_30.csv` and `scenario_parameters_E1_30.csv` contain three fits for each of ten training scenarios. `run_metadata_E1.json` records input hashes and mapping rules. The fit script imports the unchanged E0 likelihood and optimization bounds, verifies input hashes and checks each E1 test record against its E0 counterpart.

**Next evidence task:** diagnose why the single pooled stress-only distribution trades worse failure density for better runout survival. A study- and precision-aware modelling choice can then be specified and evaluated on the same held-out exact IDs. The negative E1 result is useful evidence for that choice, not a novelty claim by itself.
