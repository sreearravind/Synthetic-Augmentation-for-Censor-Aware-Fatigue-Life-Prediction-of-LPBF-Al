# van der Rest 2025 article and supplement adjudication — 7 October 2026

**Source files inspected:** user-supplied [three-page supplementary PDF](https://drive.google.com/file/d/1SI9OGfgYtVYqFwqoAABFQDTvFOKBHhzA/view) and [article PDF](https://drive.google.com/file/d/1zz-RarEIv4i1GWtZYrFVcLrKEQXBInwJ/view), from [van der Rest et al., *Materials Science and Engineering: A* 944 (2025) 148885](https://doi.org/10.1016/j.msea.2025.148885). The earlier access limitation is now resolved. Pages 1–3 of the supplement and the article's methods, Tables 4–7, and fatigue figures were inspected. The [aggregate CSV](../data/candidates/van_der_rest_2025_supplement_48_aggregate_strata_2026-10-07.csv) preserves S1–S3 counts by treatment, contour family and **reported maximum stress**. It has **48 strata, not 122 specimen rows**.

## Exact content and cross-check

| Supplement | Treatment | Stress-level strata | Tested counts by family: rough / smooth / smooth with KHP | Runouts by family | Data beyond counts |
| --- | --- | ---: | --- | --- | --- |
| Table S1 | SRHT | 18 | 14 / 14 / 14 | 0 / 0 / 0 | Failure-initiation categories as fractions at each stress |
| Table S2 | SRHT + polished | 15 | 12 / 13 / 12 | 0 / 3 / 0 | Failure-initiation categories and runout fractions |
| Table S3 | SRHT + sandblasted | 15 | 12 / 16 / 15 | 4 / 4 / 3 | Failure-initiation categories and runout fractions |
| **Total** | | **48** | **122 tested in all conditions** | **14 runouts, 108 failures by difference** | No original specimen IDs or numeric failure lives in S1–S3 |

The runout fractions in S2/S3 reconcile with article Table 7. S4 and S5 are **additional plots of the same polished and sandblasted tests** shown by families in Figures 10, 11 and 13, not additional campaigns or rows. Arrows and multiplicity labels in S4/S5 agree with the table counts. “Undefined” in S3 describes the **crack initiation site of broken specimens**; it is not an unknown event flag.

Article §2.4 specifies force-controlled uniaxial tension–tension loading, **R = 0.1**, 30 Hz, **maximum stress** 140–240 MPa, with intact tests stopped at **10^7 cycles**. These are 14 documented runout counts and bounds, but not identified original first-exposure specimens. If later comparing with an amplitude-based model, the formula would be `sigma_a = (1-R)*sigma_max/2 = 0.45*sigma_max`; no conversion or model score was performed here.

Article §2.3 describes six roughness readings around each characterized sample. Yet Table 4 publishes only roughness **means ± variation for each contour/treatment group**, and provides no specimen IDs paired with S1–S3 outcomes. Its CT analysis (2 μm voxel, 1000 slices for each of the three contour families) describes family-level porosity and does not provide a per-fatigue-specimen CT descriptor joined to outcome. The postfailure initiation categories in S1–S3 cannot be prospective XCT predictors. The polished group has no separate rowwise roughness table in this source.

## Admission decision

**Feature-plus-censor training: reject.** Neither the main article nor its complete three-page supplement contains the required original specimen ID + same-specimen numeric pretest roughness/XCT + exact fatigue event/life join. Do not populate 122 apparent “specimen” rows from stress-stratum fractions, copy group roughness into each row, or label postfracture initiation as a pretest input.

**Outcome-only potential: bounded.** The source provides 14 precise runout *counts and limits* at group/stress level; failures are displayed as graph symbols rather than a numerical life table. A separately audited graph-reading exercise could assess whether individual failure glyphs can be reconciled with S1–S3 denominators and whether any overlap or retests exist. Read each physical test once: S4/S5 are re-plots. Until that exercise, no exact outcome-only specimen ledger is admitted and the frozen v2 cohort, folds, four-arm comparisons and external results remain unchanged.

The next data task is **independent symbol reconciliation for Figures 6, 10, 11, 13 against S1–S3 counts**, explicitly preserving graph-reading precision and the 14 grouped runout bounds. Do not use S4/S5 as additional observations or run model comparisons during extraction.
