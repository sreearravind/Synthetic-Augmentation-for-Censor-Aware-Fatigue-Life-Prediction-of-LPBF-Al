# Locked Al-Zuhairi 30 µm external outcome-only comparison

Date: 2026-10-07. This completes the [prospectively fixed scoring protocol](al_zuhairi_30um_external_outcome_only_protocol_2026-10-07.md) on the 23 specimen-identified 30 µm results in the Al-Zuhairi 2026 preprint. The protocol received a [pre-score wording clarification](al_zuhairi_30um_external_outcome_only_protocol_2026-10-07.md): forecast parameters and medians are saved before outcomes, while density at an observed life is computed after the keyed outcome join. No membership, arm, seed, or metric changed.

## Execution and integrity

The frozen 192-row primary R=0.1 training fits (Wu 41, Chen 18, Matušů 133) were read from [archived parameters](../results/development_v2/romano_transfer_fit_parameters.csv); there was **no fit, calibration, source-offset update, feature selection, or seed choice using these 23 lives**. The [outcome-masked input](../data/validation/al_zuhairi_2026_30um_external_prediction_inputs_23_2026-10-07.csv) had 23 unique original IDs and stresses 50–150 MPa, inside the primary numerical stress span of 22.5–160 MPa. All 23 were documented failures; there was no marked runout. Five as-built vertical rows and six each of vertical T6, horizontal T6, and 45° T6 were included. The missing sixth as-built vertical result was not inferred. The 12 60 µm candidates were excluded under the [publication-overlap audit](lehner_2024_vs_al_zuhairi_2026_overlap_adjudication_2026-10-07.md).

The [scorer](../scripts/score_external_al_zuhairi_30um.py) saved [276 forecasts](${dir}forecasts_23x12.csv) for the 23 IDs × 12 fixed fits (C0 and C1 once each; S0 and S1 for five seeds each) before the candidate outcome ledger was read. Git blob `9d0497d0d67f089c1b455e4539935f1318b213d4` and [forecast manifest](${dir}forecast_manifest.json) `5483c37a1303d531d8257329757a1b77ba916793` were committed and read back before scoring. The subsequent strict keyed join required matching original ID, source row, stress, and condition and produced [276 individual scores](${dir}scores_per_record.csv), [seed and condition scores](${dir}scores_by_arm_seed_condition.csv), [summary](${dir}summary.csv), and [score manifest](${dir}score_manifest.json). Remote blobs matched the local artifacts. Numerical 161/321-node source-offset marginalization checks differed by at most `8.9 × 10^-16`, below the `10^-5` gate.

## Fixed-arm results

NLL is the mean negative **natural log** predictive density of observed `log10(N)`; smaller is better. S0/S1 values are the arithmetic mean across all five predetermined seeds, with no winner selected. Median error and signed bias are measured in `log10` cycles; bias = predicted median minus observed life.

| Arm | Mean NLL | Δ NLL from C1 | Five-seed NLL range | Mean absolute median error | Mean signed bias |
| --- | ---: | ---: | ---: | ---: | ---: |
| C0, unpooled baseline | 1.7300 | +0.1145 | — | 0.9893 | −0.7749 |
| C1, experimental-only source-marginal comparator | 1.6155 | 0 | — | 1.0015 | −0.7807 |
| S0, synthetic all-source | 1.6038 | −0.0118 | 1.5670–1.6290 | 0.9982 | −0.7760 |
| S1, source-filtered synthetic | 1.6131 | −0.0024 | 1.6054–1.6180 | 1.0009 | −0.7799 |

| Fixed seed | S0 mean NLL | S1 mean NLL |
| ---: | ---: | ---: |
| 13 | 1.5886 | 1.6107 |
| 29 | 1.6290 | 1.6180 |
| 47 | 1.6113 | 1.6137 |
| 71 | 1.6228 | 1.6179 |
| 101 | 1.5670 | 1.6054 |

The small aggregate NLL reductions for S0 and S1 are **descriptive**. Individual seeds cross C1. The C1 average absolute median error is about one order of magnitude in cycles, and both synthetic arms have nearly the same error and bias. This external exercise does not reverse the prior fixed development-fold finding that S1 failed to outperform C1. Five seeds are repeated fits, not independent publications or additional test specimens.

C1 condition-level diagnostics locate a large shift in the T6 subsets:

| 30 µm condition | n | C1 mean NLL | C1 mean signed bias (log10 cycles) |
| --- | ---: | ---: | ---: |
| Vertical as-built | 5 | 1.0949 | +0.5079 |
| Vertical T6 | 6 | 1.5990 | −1.0874 |
| Horizontal T6 | 6 | 2.0309 | −1.2438 |
| 45° T6 | 6 | 1.6504 | −1.0847 |

Positive bias means median overprediction and negative bias means median underprediction. These are four **conditions within one preprint**, not four held-out studies. Their descriptions must not be used to retrofit condition coefficients or reweight this test into a publication macro.

## Scope and next decision

This tests stress-only failure-life transfer from R=0.1 training to R=−1, with changes in process and T6 state. The four fitted arms have no R, orientation, treatment, or specimen-matched pretest defect/topography coefficient. Stress lies inside numerical training support, but that alone does not ensure domain compatibility. The source is a preprint with 23 all-failure records; it provides no right-censor score and cannot establish a censor-aware augmentation benefit. Lehner 2024's reported 60 µm process does not reuse these 30 µm specimens; other cross-publication reuse has not been comprehensively ruled out. No superiority p-value or algorithm-novelty claim is warranted.

**Next task:** audit whether a genuinely independent source supplies specimen-level pretest features, a known stress ratio and documented runouts in enough rows to define a model input and evaluate censoring. Keep this fixed external score untouched. If such data are unavailable, frame the manuscript around the well-supported limits of stress-only transfer and the negative development-fold augmentation finding rather than claiming augmentation gains from this small preprint cohort.
