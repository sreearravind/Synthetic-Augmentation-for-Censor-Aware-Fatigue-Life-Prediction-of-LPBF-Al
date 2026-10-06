# Source-aware sensitivity to 53 additional graph-derived failures

**Status: exploratory development analysis, 6 October 2026.** The exact held-out Wu, Romano and Chen studies were already inspected in E0/E1/M1 work, so these scores cannot be claimed as a fresh independent validation or used to select a final method. No synthetic data were generated. Strauß and Löwisch 2024 and Kempf 2022 remain untouched prospective tests.

## Controlled comparison

The control is the stored M1 study-marginal Weibull AFT model with fixed study-effect SD τ=0.25, trained on the frozen exact studies in each of three leave-study-out folds. The sensitivity variant uses **the same model, scoring rule, exact fold membership and τ**, but adds 53 candidate graph-derived *failure-only* glyphs from Muhammad 2023 (38) and Fernandes 2024 (15) to each fold's training set. Each graph source has its own integrated study intercept. Its per-glyph failure log likelihood is multiplied by a fractional weight **inside** that source's marginal likelihood; exact rows retain weight 1. A diagnostic graph-source cap of five total effective likelihood contributions gives Muhammad 5/38 per glyph and Fernandes 5/15 per glyph. The caps are assumptions for sensitivity, **not measured reading-error probabilities** or a fitted quality score. A new held-out study receives a fresh integrated intercept, not its own fitted source offset. All exact test observations and censor bounds remain unchanged.

For graph-derived failures the central plotted Δσ was converted to stress amplitude Δσ/2; the reported life-axis centers were used as failure times. The reading scenarios use joint low/low or high/high graph intervals, without manufacturing extra observations. Since the source figures do not establish arrow runout stop cycles, **no new graph runouts** entered training. The metadata, source checksums and 21 fitted scenario × fold parameters are saved alongside this report.

## Primary diagnostic: cap 5 per new source, central readings

Mean censored negative log likelihood (NLL) on **log10 life**, lower is better. Changes are augmented minus exact-only M1; negative values favor the added graph tier. Failure and runout columns are event-specific mean NLL changes on the unchanged exact test records.

| Held-out exact study | Fail/runout | M1 NLL | Added-tier NLL | Δ overall | Δ failure | Δ runout | Δ failure median-life MAE (log10 cycles) |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Wu 2021 | 33/8 | 1.787 | 1.304 | **−0.483** | −0.934 | **+1.379** | −0.817 |
| Romano 2018 | 6/1 | 2.035 | 2.054 | +0.019 | +0.046 | −0.141 | +0.031 |
| Chen 2024 | 18/0 | 1.084 | 1.022 | −0.062 | −0.062 | — | −0.013 |

The largest overall improvement is in Wu, but its eight runouts are much less probable after adding only graph failures. Romano's one runout moves in the opposite direction while its six failures worsen slightly. Chen has no runouts with which to evaluate censoring. The failure median error improvement in Wu must be read alongside its runout loss. Pooling all 66 specimens would let the 41 Wu outcomes dominate; the study-level table is the main result.

## Sensitivities

| Case | Wu Δ overall | Romano Δ overall | Chen Δ overall | Wu Δ runout |
| --- | ---: | ---: | ---: | ---: |
| Cap 2.5 per graph source | −0.446 | −0.002 | −0.034 | +0.910 |
| **Cap 5 per graph source** | **−0.483** | **+0.019** | **−0.062** | **+1.379** |
| Cap 10 per graph source | −0.479 | +0.064 | −0.109 | +1.803 |
| Cap 5, joint lower stress/life reading | −0.486 | +0.033 | −0.063 | +1.515 |
| Cap 5, joint upper stress/life reading | −0.476 | +0.005 | −0.060 | +1.254 |
| Cap 5, Muhammad only | −0.434 | −0.059 | −0.017 | +0.818 |
| Cap 5, Fernandes only | −0.406 | +0.127 | −0.052 | +0.802 |

The Wu runout penalty persists in every scenario; greater source weight magnifies it. Romano's sign and its runout contribution depend on which graph source is admitted. Reading bounds do not reverse the primary Wu/Chen direction, but the Romano delta stays close to zero. Both graph sources are heterogeneous in finish and protocol: Muhammad combines AB and chemo-mechanical polished samples at R=0.1/−1; Fernandes combines AB, stress relief and HIP at R=0. Neither the stress-only slope nor a single study intercept can attribute these effects. Thus the source-drop cases are diagnosis, not a rationale for choosing a favorable subset.

Numerical gates: all 21 fits converged with negative stress slopes and unconstrained Weibull shapes, and all 161-versus-321-node Gauss–Hermite objective and prediction checks passed at 10⁻⁵. The stored exact-only M1 control scores were reproduced to 10⁻⁹ on every fold. The 53 graph rows were never scored as test cases. Exact source and split hashes match the locked inputs; the graph candidate CSV digest is in `run_metadata.json`.

## Decision and manuscript implication

The newly read failure-only tier is **usable as an exploratory training sensitivity**, with source grouping and transparent weight caps, but it cannot presently support a general improvement claim or a final augmentation design. Runout ascertainment is imbalanced, treatment and stress ratio are confounded with sources, and the three exact folds are no longer fresh tests. The next technical gate is to specify a censor-aware synthetic generator using training sources only, freeze its comparator and scoring rules, and then assess it on the two reserved original experimental campaigns without tuning to those outcomes. Source-original runout data or author tables would improve this gate, but no author reply is assumed here.

Reproduce using `scripts/source_aware_new_graph_tier_sensitivity.py` with the locked exact CSV, membership CSV, graph53 CSV and M1 development fit/score CSVs. Outputs: `fold_metrics_21.csv`, `fit_parameters_21.csv`, `paired_exact_record_predictions_462.csv` and `run_metadata.json`.
