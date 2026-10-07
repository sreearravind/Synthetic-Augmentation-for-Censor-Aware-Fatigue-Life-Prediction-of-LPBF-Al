# Al-Zuhairi 2026 supplementary audit: S1–S13

Audit date: 2026-10-07. Source: [Al-Zuhairi et al., preprint version 1, posted 22 September 2026](https://www.preprints.org/manuscript/202609.1879). Uploaded source folder: [S1–S13](https://drive.google.com/drive/folders/1EmDF4hcBukWsReUI2sLo1LkM-7RI4lfl). The preprint is not peer reviewed.

## File inventory and row reconciliation

The files are semicolon delimited. S1–S6 use integer stress and cycles; S7–S13 use decimal commas for their decimal values. Parsing these as ordinary comma-separated files would corrupt the latter measurements.

| Condition | Fatigue file | Specimen IDs, stress amplitudes and `N_B` | Corresponding strength-comparison file | Paired strength rows | Reconciliation |
| --- | --- | ---: | --- | ---: | --- |
| 30 µm V, as-built | S1 | 5 | S9 | 5 | **One fewer than six specimens claimed in article** |
| 30 µm V, T6 | S2 | 6 | S10 | 6 | Count agrees |
| 60 µm V, T6 | S3 | 6 | S12 | 6 | Count agrees |
| 60 µm V, as-built | S4 | 6 | S11 | 6 | Count agrees |
| 30 µm H, T6 | S5 | 6 | S8 | 6 | Count agrees |
| 30 µm 45°, T6 | S6 | 6 | S7 | 6 | Count agrees |
| **Total** | **S1–S6** | **35 distinct printed IDs** | **S7–S12** | **35 pairs** | **No shared individual key** |

Article §2.1 states that six specimens per condition (36 total) were manufactured and tested, whereas [S1](https://drive.google.com/file/d/1QetLPxap63geCSNjL3oVPuzP8G_CAtrN/view?usp=drivesdk) has exactly five data rows. [S9](https://drive.google.com/file/d/1m8FkzGqdF4NntNgj4l7JXxVab_uVT_s9/view?usp=drivesdk) also has five paired-estimate rows. The sixth outcome is **not recoverable from the uploaded files**. Do not add an inferred row, infer its stress/life, or classify it as a runout.

S1–S6 headers are `Specimen ID;Stress in MPa;Number of cycles N_B`. Their 35 IDs are unique. The article §2.2 calls these stress amplitudes and cycles to failure `N_f`, describing postfailure fracture-surface examinations. Thus the 35 printed `N_B` rows have **reported-failure interpretation** (45,277 to 1,024,885 cycles) with no explicit right-censor mark or stop bound. This is a source-grounded interpretation of the **printed rows only**; it does not establish that all 36 manufactured specimens failed or rule out an omitted runout. The [candidate outcome ledger](../data/candidates/al_zuhairi_2026_s1_s6_35_exact_outcome_candidate_2026-10-07.csv) records the original IDs, source file IDs and row locators, R = −1 axial 10 Hz protocol, event = 1 for the 35 printed failure rows, an empty censor bound and `candidate_only` status. The printed stress column is retained as amplitude based on §2.2; no independent max/min stress columns are given.

S7–S12 have two numeric columns headed fractography and confocal `stress in MPa`; they are **fatigue-strength estimates**, not applied stresses or `N_B` outcomes. Rows contain no specimen IDs, test stresses, life values or explicit join keys. Even though counts match within each condition and the article compares estimates for each specimen, corresponding row order across files is not documented as an identity key. Do **not** attach any confocal-derived value to a specific S1–S6 outcome by row order, sorting, stress magnitude or outcome matching. Fractography estimates are postfailure information and prohibited as pretest predictors.

[S13](https://drive.google.com/file/d/1ukp28W35pgwAD-bHJkJU1jGXz4UArxan/view?usp=drivesdk) holds six condition columns under `fractography measurements` and `Confocal measurements` and additional `max. Values`/`min. Values` rows, but no specimen IDs. Their precise statistical meaning is not declared in the CSV; do not interpret them as per-specimen critical defects or replicate them across the 35 outcomes. The pretest confocal inspection covers only about 15% of vertical and about 30% of H/45° as-built gauge surface in the manuscript. A sampled maximum has that measurement-coverage limitation even if a future individual key becomes available.

## Duplicate/publication check

The authors cite [Lehner et al. 2024](https://doi.org/10.1016/j.ijfatigue.2024.108479) as prior testing/model work, and some authors recur. The new preprint says its six groups were manufactured and tested in this work, but it does not give an explicit prior-campaign specimen-ID crosswalk. The Lehner 2024 original specimen-level table or supplement was not in the supplied folder and could not be retrieved from the indexed publisher page in this audit. **Direct overlap with Lehner remains unresolved.**

As a narrower check, the 35 candidate IDs were compared against [development v2's 199 rows](../data/cohorts/development_v2_199_2026-10-06.csv): zero identical `record_id` strings and zero exact `(stress amplitude, observed cycles, R)` triples. That confirms no exact row collision with the *current* frozen cohort; it cannot prove independence from Lehner 2024, which is not in that cohort. Shared authors and a similar test protocol are likewise insufficient to establish a reused specimen.

## Decision and next evidence gate

**35 stress–life outcomes are transcribed as a source-separated candidate; zero runouts are explicitly identified in those 35 printed rows; one of 36 reported specimens is absent.** There are **zero defensible specimen-joined pretest confocal/defect predictors** in S1–S13. No rows enter the 199-row frozen v2 development cohort, no folds change and no model is refit. The preprint can be assessed for a distinct R = −1 outcome-only external evaluation after documenting independence from Lehner and predeclaring the evaluation role, but it cannot presently test a specimen-level confocal predictor or a right-censor benefit. Peer-reviewed status must be stated accurately.

The most useful next source is the 2024 Lehner paper plus any original specimen-level table/supplement (or an explicit cross-publication specimen-ID statement). If a keyed confocal-data file becomes available, link it to S1–S6 using the original specimen ID and preserve pretest measurement timing; do not reconstruct IDs from matching row counts. The missing S1 sixth specimen needs a primary source correction or explicit documentation before its outcome can be used.
