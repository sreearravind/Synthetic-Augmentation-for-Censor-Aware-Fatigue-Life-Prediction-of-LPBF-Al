# Development cohort v2 membership freeze — 6 October 2026

**Scope.** Freeze the experimental *development inventory* before any new model comparison. This is a source and split decision, not a model fit or a journal adequacy claim. [199 normalized first-exposure rows](../data/cohorts/development_v2_199_2026-10-06.csv) are the only v2 development observations: 172 failures and 27 right-censored observations. The 66-row exact-only E0/M1 membership and its already inspected folds remain historical controls and must not be reinterpreted as fresh validation.

## Cross-publication overlap check

| Publication or source | Relevant evidence | Decision |
|---|---|---|
| Matušů et al. 2024, *International Journal of Fatigue*, DOI [10.1016/j.ijfatigue.2024.108357](https://doi.org/10.1016/j.ijfatigue.2024.108357) | The [2026 full article](https://doi.org/10.1016/j.rineng.2026.112570), Table 3, explicitly labels 41–44 as reused from ref. [18]; the 2026 workbook lists 44 first loadings and five retests in those series. | Exclude all 49 episodes of 41–44 from v2. |
| Matušů et al. 2024, *Procedia Structural Integrity* 54, DOI [10.1016/j.prostr.2024.01.065](https://doi.org/10.1016/j.prostr.2024.01.065), [author-uploaded full text](https://www.researchgate.net/publication/378610548_Fatigue_analysis_of_additively_manufactured_specimens_from_AlSi10Mg_with_different_levels_of_powder_recycling) | Compares several CLM2 GE/Eckart powder-recycling platforms. Its Fig. 4b explicitly gives T240, 70 MPa, **105,156 cycles** from platform 3; the 2026 workbook has the exact fingerprint in series **42**, specimen **18**. Its fresh platform 1 Fig. 4a T240 example (100 MPa, **170,031 cycles**) and Fig. 2b example (90 MPa, **106,313 cycles**) are absent from **all** 2026 workbook episodes. Shared printer, powder label and heat treatment alone do not make 91–94 the same physical platform. | Confirms earlier 41–44 reuse. Gives **no specimen-level evidence** that 91–94 was previously published; do not import this paper's S–N symbols as extra v2 rows. |
| Matušů et al. 2024, *Fatigue & Fracture of Engineering Materials & Structures*, DOI [10.1111/ffe.14442](https://doi.org/10.1111/ffe.14442) | One build platform, four heat treatments; NoHT tensile values 244.9/438.3 MPa match 2026 series 41, not the separate virgin-powder series 91 (244.1/437.3 MPa). | Reanalysis of the prior 41–44 family, no v2 addition. |
| Matušů et al. 2026, [build-position paper](https://doi.org/10.1016/j.prostr.2026.01.018) | Describes a pooled 22-series, seven-platform campaign over four years; some underlying platforms may coincide with the 2026 workbook but the publication does not supply a specimen-to-workbook crosswalk. | **Possible aggregate reanalysis**, not a new independent experiment; never extract its plotted records as additional v2 observations. Membership of 91–94 in that broad reanalysis is unresolved, and does not duplicate rows *within* the workbook. |
| Mára et al. 2026, [combined defects/heat-treatment paper](https://doi.org/10.1016/j.prostr.2025.12.295) | Reports three fresh-GE batches of 30 **machined** HCF specimens; 2026 series 91–94 are **as-built** GE virgin specimens, with 60 identified first exposures. | Distinct surface/production matrix on available evidence; no extra v2 rows. |
| Matušů et al. 2024 [AI/self-heating and position paper](https://dspace.zcu.cz/items/7f7829d4-efd3-4c6f-a096-bb86def13501) and 2025 [laser shock peening paper](https://doi.org/10.1016/j.ijfatigue.2025.109149) | Same group; the first is a position analysis without a specimen-level crosswalk here, the second uses laser-peened thin tubes. | Do not count either as an additional independent source. No direct 91–94 specimen match was established. |

This is a **bounded evidence conclusion**: the checked prior papers do not establish reuse of 91–94 fatigue rows. It is not a proof that no earlier abstract or unavailable dataset used any of those specimens. The 2026 workbook is the single canonical source for its 133 identified first exposures. Reuse of those same results in another publication never increases the specimen count.

## Frozen membership

| Publication group | Platform families represented | Failures | Runouts | Total |
|---|---:|---:|---:|---:|
| Wu 2021 | One publication group | 33 | 8 | 41 |
| Romano 2018 (Tognan re-report) | One underlying experiment | 6 | 1 | 7 |
| Chen 2024 | One publication group | 18 | 0 | 18 |
| Matušů 2026: GE virgin, Eckart virgin, Aconity TWO | **Three platforms within one publication group** | 115 | 18 | 133 |
| **v2 total** | **Four publication groups** | **172** | **27** | **199** |

For Matušů, GE virgin 91–94 contributes 54 failures/5 runouts; Eckart virgin 71–74 contributes 36/8; Aconity C01–C03 contributes 25/5. Exclude anonymous 92/XX (one runout), all 19 later loadings in these platforms, and all reused 41–44 episodes. Four retest-amplitude discrepancies in the [full-text audit](matusu_2026_full_text_protocol_audit_2026-10-06.md) concern excluded later episodes and do not turn their initial runouts into failures. No new per-specimen censor stop is inferred: the Matušů runout bound is the article's 10,000,000 cycles, while the instrument count remains in the [candidate ledger](../data/candidates/matusu_2026_protocol_checked_133_first_exposures.csv).

The v2 file normalizes record IDs, event indicators, bounds and stress amplitude; all are original experimental first exposures. It does **not** contain graph readings or synthetic records. Blank printer/powder for prior sources means unavailable in this harmonized file, not a common setting. The seven Romano core records had `test_frequency_Hz=0` in the prior CSV; this is not a physical test frequency and is blank in v2, explicitly annotated. Per-specimen frequency is unavailable for Matušů (only the article's 90–120 Hz range is recorded). Do not use these fields as if uniformly measured.

**Immutable inputs for this version:** `data/cohorts/smooth_core_66.csv` GitHub blob `fd9e7600588eddb2c25167ca1cfe3f2f57422409`; `data/candidates/matusu_2026_protocol_checked_133_first_exposures.csv` blob `33c455ca4067f08ed32e54cb94daa51f1f4ce356`; v2 output blob `ee9f6451e60b290c89c44f681b471b3c007c6f74`. The Matušů workbook MD5 is `c6c2df499bc323928d55f08109f45678`. All 199 IDs are unique; event/bound consistency and source totals were checked after upload.

## Locked evaluation rules for the next comparison

1. Keep the old exact-only E0/M1 results as **inspected development history**. Fit comparisons using v2 may be new computational runs, but the Wu/Romano/Chen fold outcomes are no longer fresh independent evidence.
2. For publication transfer, leave out **one entire publication group** at a time. Keep all 11 Matušů treatment series and its three platforms together whenever Matušů is held out. Score specimen likelihood with censoring, report failure and runout contributions separately, and summarize by publication group so 133 Matušů rows do not dominate a pooled metric.
3. A within-Matušů leave-one-platform-out check is **secondary domain-shift sensitivity**, never three independent published-study validations. No random specimen split across the same platform for a claimed external test.
4. Use only pretest information shared across sources for a primary comparator (at minimum stress amplitude and R, with missingness handled explicitly). Treatments, finishes, powder, geometry and test frequency require availability and confounding review before any expanded feature set. Postfracture initiator features cannot enter prediction.
5. Any synthetic generator is trained within each training fold only. Synthetic samples must have generated provenance and must never be counted among these 199 experimental observations or scored as test specimens.
6. The reserved [Strauß/Löwisch primary and Kempf secondary external campaigns](external_holdout_source_lock_2026-10-02.md) remain outside v2 and **unscored**. Freeze algorithm, feature handling and comparison metrics before opening their outcomes for a final external evaluation.

Any later addition or correction creates v3 with a new file and manifest; do not silently edit v2 membership. The immediate technical task is a no-outcome-leakage harmonization and grouped-fold feasibility audit, followed by predeclared model comparisons.
