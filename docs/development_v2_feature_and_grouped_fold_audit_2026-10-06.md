# Development v2 feature and grouped-fold audit — 6 October 2026

This audit confirms the frozen [199-row experimental membership](../data/cohorts/development_v2_199_2026-10-06.csv) and defines a feasible comparison track before fitting any new model. It corrects the provisional feature wording in the [membership lock](development_v2_overlap_and_membership_lock_2026-10-06.md): **stress ratio is complete as metadata but cannot be estimated as a source-independent fitted effect** in leave-publication-out training. The 199 membership rows and their blob are unchanged.

## Pretest feature check

| Field | Availability across v2 | Decision for first controlled comparison |
|---|---|---|
| Nominal stress amplitude, MPa | 199/199; all four publications. Stress ranges: Wu 22.5–90; Romano 90–200; Chen 67.5–99; Matušů 30–160. Core stress conversions and the workbook's amplitude are documented in source ledgers. | **One fitted predictor:** log stress amplitude, with transformation and reference stress fixed using training rows only. Preserve source stress basis and original values in their ledgers. |
| Stress ratio `R` | 199/199; Wu 41, Chen 18, Matušů 133 at `R=0.1`; **all seven `R=-1` records come from Romano**. | Stratify the evaluation. The primary publication-transfer track is 192 `R=0.1` rows. Romano is a separate, labelled `R=-1` transfer challenge. Do **not** fit or select an `R` coefficient from these grouped folds; when Romano is held out, its `R` value is absent from training. |
| Build orientation | 192/199 filled: Wu H/V, Chen vertical, Matušů upright; Romano blank. | Audit/stratum only. A future harmonization must explicitly verify whether “upright” and “vertical” have the same referenced axis and specimen geometry. |
| Surface condition | 199/199 textual labels, but Wu, Romano and Chen each have a source-specific condition. Matušů has three labels across its platforms. | Audit/stratum only; a common numeric roughness for every specimen is unavailable, and surface/process effects are coupled. |
| Heat treatment | 199/199 textual descriptions, but the common NoHT/T200/T240/T300 levels vary within Matušů, while other publications have distinct protocols. | Audit/stratum only. Do not infer a global causal heat-treatment effect from these four publication groups. |
| Printer and powder | 133/199, all from Matušů. GE virgin is as-built CLM2; Eckart virgin is machined CLM2; Nikon SLM is Aconity TWO with as-built or polished treatments. | **Not** cross-source predictors in the first comparison. Printer, powder and finish are partly or fully confounded with platform family. |
| Frequency | Exact numerical value in 59/199 (Wu 85 Hz; Chen 20 Hz); Matušů gives a source-level 90–120 Hz interval for 133; Romano's source CSV `0` was blanked rather than treated as a physical frequency. | No per-specimen pooled frequency predictor. Keep range/known frequency as provenance. |
| Geometry and defect descriptors | Core source geometry resides in original ledgers; Matušů uses upright hourglass specimens with 64 mm² critical section, but the normalized v2 file has no common geometric descriptor. Fracture initiator defects are measured after fatigue in several papers. | No pooled geometry or postfracture-defect predictor. Releasing geometry or matched pretest XCT features would require a separately audited feature version. |
| Failure life or censor bound | 199/199 outcomes: 172 failures, 27 runouts. Matušů right censor is at the method-defined 10 million cycles; its precise instrument count remains in the candidate ledger. | Outcome only, handled with failure density or runout survival probability. Never treat a runout as a failure or turn a synthetic row into an experimental observation. |

Matušů's internal conditions are: GE virgin 91–94 (59 rows, 5 runouts), Eckart virgin 71–74 (44, 8), and Aconity C01–C03 (30, 5). The two CLM2 families have four thermal series apiece; Aconity has two NoHT surface states and one polished T240 state. This is useful for **within-paper sensitivity**, while powder, surface and printer effects are not independently isolated.

## Frozen fold assignment and feasibility

[Row-level assignment](../data/validation/development_v2_grouped_fold_assignments_2026-10-06.csv) and [fold counts/stress support](../data/validation/development_v2_grouped_fold_feasibility_2026-10-06.csv) are the machine-readable definitions. Every training set is the complement of its held-out publication **within the specified track**, so none of Matušů's three platforms enters training when that publication is tested.

| Track and test group | Train failures/runouts | Test failures/runouts | Test stresses beyond training range | Interpretation |
|---|---:|---:|---:|---|
| Primary `R=0.1`: Wu | 133/18 | 33/8 | 7/41 (3 failures, **4 runouts** below 30 MPa) | Study transfer plus low-stress extrapolation; show tail separately. |
| Primary `R=0.1`: Chen | 148/26 | 18/0 | 0/18 | No test runouts, so no censor assessment on this fold. |
| Primary `R=0.1`: Matušů, all three platforms together | 51/8 | 115/18 | **41/133 failures** above the 99 MPa training maximum | Strong publication/process and high-stress transfer; aggregate and in-range/tail metrics both needed. Training has only two publication groups. |
| Secondary `R=-1`: Romano | 166/26 (`R=0.1` only) | 6/1 (`R=-1`) | 2/7 above 160 MPa; **all 7 have an unseen ratio** | Out-of-ratio challenge only; unsuitable for choosing a fitted mean-stress effect. |

The **primary track contains 192 rows from three publication groups**: 166 failures and 26 runouts. Do not pool the seven Romano `R=-1` observations into the primary training or fold metric. They remain in v2 for a separately reported fixed-model challenge. Existing Wu/Romano/Chen E0/M1 scores were inspected previously and are not prospective validations.

A further *secondary* leave-one-Matušů-platform-out check holds out, respectively, GE virgin 59 rows (train 133), Eckart virgin 44 (train 148), or Aconity 30 (train 162), using the other `R=0.1` rows as training. These are shared-publication process-route sensitivities, not three independent source validations. GE's 13 stress-tail failures above the training maximum must be labelled.

## Confirmation and next gate

**Feasible now:** a simple, censor-aware stress-amplitude probabilistic comparator with predeclared source-group folds, macro publication metrics, separate failure/runout likelihood, and explicit in-range/tail reporting. A highly parameterized treatment/powder/surface algorithm or fitted `R` effect is **not identifiable from these group splits**. Keep augmentation train-only and compare against the exact experimental baseline on the same held-out records. Any feature engineering and hyperparameter choice must be made within training groups; the reserved external sources stay unscored.

Checks on the frozen files: 199 unique record IDs; primary 192 and Romano challenge 7; no row is assigned to two primary test folds; three Matušů platforms share one primary fold; all outcomes have consistent failure/censor operators. Cohort blob `ee9f6451e60b290c89c44f681b471b3c007c6f74`. This audit changes **evaluation scope**, not v2 membership or earlier model results.
