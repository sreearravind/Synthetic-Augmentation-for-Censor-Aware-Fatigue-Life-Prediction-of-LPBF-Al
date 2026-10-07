# Locked external outcome-only protocol: Al-Zuhairi 30 µm campaign

Protocol date: 2026-10-07. **Status: specified before any predictions on this campaign; no Al-Zuhairi model score has been calculated.** Earlier source inspection identified the specimen IDs, stress and life columns and the missing sixth 30 µm vertical as-built row. This is prediction-blind, not outcome-unseen, evaluation. Keep this document and its exact input blobs fixed for the next implementation.

## Source eligibility and input identity

The [cross-publication audit](lehner_2024_vs_al_zuhairi_2026_overlap_adjudication_2026-10-07.md) identifies 23 exact stress–life records made with the **30 µm** process: S1, 30 µm V as-built (5); S2, 30 µm V T6 (6); S5, 30 µm H T6 (6); S6, 30 µm 45° T6 (6). Lehner 2024 reported only a 60 µm build; that narrower comparison establishes no reuse of its reported specimens. The 12 S3/S4 **60 µm** records remain possible reuse and are excluded even from subgroup scores. The one missing S1 specimen is never inferred. All 23 included source rows have a specimen ID, a stress amplitude, and a printed failure-cycle value; no source row is labelled as a runout. The source is a 2026 preprint and all 23 belong to **one** publication, not four independent publications.

Frozen files and Git blobs at protocol lock:

| Role | Path | Blob SHA |
| --- | --- | --- |
| Prior development cohort, never altered | [v2 199-row cohort](../data/cohorts/development_v2_199_2026-10-06.csv) | `ee9f6451e60b290c89c44f681b471b3c007c6f74` |
| Full source transcription and outcomes, audit only until scoring | [Al-Zuhairi 35-row candidate ledger](../data/candidates/al_zuhairi_2026_s1_s6_35_exact_outcome_candidate_2026-10-07.csv) | `3847d10f768ee695fff8c2d22f13c73fc8a2af1d` |
| **Outcome-masked input and fixed membership** | [23-row prediction input](../data/validation/al_zuhairi_2026_30um_external_prediction_inputs_23_2026-10-07.csv) | `5079cdebfe22f6a6a57311c18e1487723c7ee7e1` |
| **Already fitted** parameters on 192 primary R=0.1 real rows | [Romano-transfer fit parameters](../results/development_v2/romano_transfer_fit_parameters.csv) | `72bb25ca79d72effd2c2bbac4c30fffcbc80ed19` |
| Published model implementation | [v2 comparison script](../scripts/compare_development_v2.py), [M1 helper](../scripts/fit_m1_source_aware.py), [C0 helper](../scripts/fit_weibull_exact_baseline.py) | `f9b76f3457d4823845f3e3567131738d15236440`, `0a4fabe03bde4d0bad693cba2ac8ab4abd21ec87`, `921c19a8a1bac5a15a6dc557fad89ce80d46bba7` |

The archived `Romano_2018_transfer` parameter rows are reused only because they were fitted on **Wu 41 + Chen 18 + Matušů 133 = 192** original R=0.1 observations and were saved before the present Al-Zuhairi predictions. Romano's seven outcomes were scored by that previous workflow; **no Romano outcome was used to fit or select these parameters**. Prior development showed no S1 augmentation advantage. Do not refit or select an arm using Romano or Al-Zuhairi performance.

## Input compatibility and shift

| Field | Locked model input | Al-Zuhairi 23 rows | Rule |
| --- | --- | --- | --- |
| Applied stress amplitude `σa` | The **only transportable numeric predictor**; `x = log2(σa/100 MPa)` | Exact printed stress amplitudes, 50–150 MPa | Direct numeric mapping, no maximum/mean stress substitution. All lie inside the 192-row training stress span **22.5–160 MPa**. |
| `R`, surface, heat treatment, orientation, layer thickness | Audit and source-grouping fields; no fitted coefficients in C0/C1/S0/S1 | All R = −1, four conditions, 30 µm | Record and report as domain shift. Never relabel R as 0.1 or impute missing coefficients. |
| Individual pretest defect/topography | No such predictor in the locked model | Not specimen-joinable in S7–S13 | No join by row position and no use of postfracture initiators. |
| Life/event | Hidden from model input; exact first-exposure outcome for scoring | 23 printed `N_B` failures, no marked runout | Join by **original specimen ID** only after exporting predictions. Do not invent the absent sixth record. |

This is an **R=0.1 to R=−1 transfer challenge**, despite in-range numeric stress. The earlier seven-row Romano R=−1 score is separate development evidence; it is not pooled with this preprint, used for recalibration or treated as a jointly untouched external test. The 23 records cannot establish censoring performance because they contain no documented runout.

## Predictions and score lock

1. Read the 23-row outcome-masked input and verify its blob, count, unique IDs, 30 µm status, positive stresses and in-range flag. Verify the archived parameter file blob has exactly one C0 and one C1 all-192 fit, and five each for S0/S1 with seeds **13, 29, 47, 71, 101**; success flags and no boundary fit. The input/model parameter blob checks are hard gates. Do not train on or infer a source offset using any Al-Zuhairi row.
2. Compute and save per-ID predictive median `log10(N)` and predictive **log10-cycle failure density** for **C0, C1, S0, S1**, using the existing model code. C1 is the fixed primary experimental-only comparator; C0 and the two exploratory synthetic arms are reported fully. For C1/S0/S1 integrate a fresh, independent source offset `b_new ~ N(0,0.25²)` at prediction time; do not fit an offset to the 23 lives. Check the 161-versus-321-node predictive log-density difference ≤ `1e-5`. Export these forecasts with original IDs and input/model blob IDs **before the outcome join**. All four arms and every seed must be present or mark the run invalid, not replace a seed.
3. After forecasting, join to the candidate ledger strictly on original specimen ID and require exact agreement of source file, stress, 30 µm condition and 23 failures. Score each real failure as `-log f_Z(log10 N_i | σa_i)`, using the **natural logarithm** of density relative to `log10` cycles. Primary descriptive number: the **23-row mean NLL** for each arm, C1 as comparison anchor. Show all five seed-level S0/S1 means and their arithmetic mean and min–max, as well as paired per-ID and aggregate differences against C1. No seed selection.
4. Secondary descriptive diagnostics: mean absolute predictive-median error `|median_log10N - log10N|` and signed bias `median_log10N - log10N`, over the same 23 failures. Give NLL, error and count by the four conditions, **without** treating conditions as independent studies or reweighting them to manufacture a four-study macro. Include the ratio shift and whether each stress is within numeric training support. There is no runout-survival score, censor-discrimination metric, or right-censor subset for this campaign.
5. No parameter tuning, feature selection, uncertainty adjustment, pseudo-row generation, synthetic training, calibration, threshold choice, publication weighting, or study-offset posterior update may depend on these 23 outcomes. Do not combine this score with the three primary development fold means or the Romano score. Report the preprint status, single-publication n=23 size, original-vs-derived feature distinction and possible other publication overlap not established by the Lehner-only audit. No superiority p-value or algorithm-novelty claim follows from one all-failure source.

**Interpretation:** the calculation can test stress-only failure-life transfer under a large R/process shift. It cannot validate a specimen-level confocal feature or a censor-aware augmentation benefit. A poor score is an informative limit of the fixed model, not grounds to redefine this cohort; an apparently improved synthetic-arm score is exploratory and cannot overturn the prior negative primary comparison.

## Next execution

Implement a read-only scorer that uses the archived all-192 fit rows and writes a forecast artifact before joining outcomes, then a separate keyed scoring artifact. Retain per-row outputs, quality checks and hash references in a new `results/external_al_zuhairi_30um_2026-10-07/` directory. The present step deliberately stops before those predictions.
