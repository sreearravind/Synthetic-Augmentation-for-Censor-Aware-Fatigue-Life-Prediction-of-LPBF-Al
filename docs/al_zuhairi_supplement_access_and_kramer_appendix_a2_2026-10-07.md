# Candidate campaign audit: Al-Zuhairi supplement and Kramer Appendix A2

Screen date: 2026-10-07. This note is a provenance gate, not an amendment to the frozen v2 cohort (199 rows; 172 failures and 27 right-censored runouts). No model was refit.

## Al-Zuhairi et al. (2026 preprint): supplement required

The [version 1 preprint](https://www.preprints.org/manuscript/202609.1879) reports 36 PBF-LB/M AlSi10Mg specimens in six sets of six, with pretest confocal surface topography and fully reversed axial fatigue tests (R = -1, 10 Hz). It is explicitly not peer reviewed. Nine gauge-zone measurements cover about 15% of the vertical specimen surface of interest and about 30% of the H/45° surface of interest. The reported largest measured surface valley is therefore a sampled-surface descriptor, not an observed maximum over the full gauge. Postfracture initiation-defect measurements must never be used as pretest predictors.

The article's Supplementary Materials section advertises:

| Files | Advertised content | Audit status |
| --- | --- | --- |
| S1–S6: `S1_30_µm_V.CSV`, `S2_30_µm_V_T6.CSV`, `S3_60_µm_V_T6.CSV`, `S4_60_µm_V.CSV`, `S5_30_µm_H_T6.CSV`, `S6_30_µm_45_T6.CSV` | Experimental stress–life data underlying the S–N curves | Actual columns and records not retrieved |
| S7–S12: `S7_30_µm_45_T6.CSV`, `S8_30_µm_H_T6.CSV`, `S9_30_µm_V.CSV`, `S10_30_µm_V_T6.CSV`, `S11_60_µm_V.CSV`, `S12_60_µm_V_T6.CSV` | Fatigue-strength comparison data | Actual columns and specimen linkage not retrieved |
| S13: `S13_√area_values.CSV` | Defect-area comparison data | Actual columns and pretest/postfracture distinction not retrieved |

The text of the indexed article identifies these files, but its readable page did not provide their CSV bodies to the research tools; the shared Drive literature folder contained the earlier article PDFs and no S1–S13 CSV. Consequently **the presence of specimen identifiers, a one-to-one join across these files, exact runout flags, and the count of reusable specimen records are unverified**. The manuscript's mention of cycles to failure does not establish that all 36 tests failed, nor does a plot symbol establish an exact censor time. The article cites the earlier Lehner et al. work (2024, DOI [10.1016/j.ijfatigue.2024.108479](https://doi.org/10.1016/j.ijfatigue.2024.108479)) and has overlapping authors; publication overlap cannot be resolved from authorship or narrative alone.

**File-level decision rule once the 13 CSVs are available:** preserve raw files and checksums; inventory headers, units, row counts, duplicate keys and six condition labels; record stress amplitudes, observed cycles, event/censor indicator and explicit stop rule from the original field or caption; check whether a stable specimen ID is repeated across S1–S6, S7–S12 and S13. If no such key exists, do not create a specimen-matched confocal predictor by ordering rows or matching outcomes. Distinguish pretest `√A_perp` from postfracture `√area` in separate columns and block the latter from prediction input. Compare specimen IDs and available (condition, stress amplitude, cycle count, event) fingerprints with Lehner's original data before assigning a new source group. Ambiguous runouts or duplicate platform records stay outside the modeled cohort. The file upload that unblocks this check is the 13 CSVs together (a ZIP is fine); no TIFF imagery is needed for this audit.

## Kramer et al. (2025): separate candidate screen

The peer-reviewed [Kramer et al. paper](https://link.springer.com/article/10.1007/s40964-025-01288-x), DOI [10.1007/s40964-025-01288-x](https://doi.org/10.1007/s40964-025-01288-x), reports individual stress amplitudes and observed cycles in Appendix A2. Its high-density (HD) fatigue results are stated to come from Wexel et al. (2024), DOI [10.1016/j.procir.2024.05.032](https://doi.org/10.1016/j.procir.2024.05.032); those 10 HD rows are excluded from the newly reported candidate subset. The remaining 10 keyhole (KH) and 9 lack-of-fusion (LoF) table entries are transcribed in [the candidate CSV](../data/candidates/kramer_2025_kh_lof_appendix_a2_screen_2026-10-07.csv): 19 rows, 18 failures and one KH right-censored entry at 10,000,000 cycles. The paper says its runout stress amplitudes were confirmed with a second test; Appendix A2 exposes only one KH line at that threshold, so do not invent an additional row from that statement.

These specimens were machined and tested in rotating bending at R = -1 and 50 Hz. The investigators measured Sa and Sz before testing for every fatigue specimen, but Table 4 summarizes them by porosity condition; Appendix A2 does not identify which pretest reading belongs to each stress–life row. The CSV thus leaves `original_specimen_id` empty and explicitly marks `pretest_Sa_Sz_matched=no`. Its `KH_A2_01` etc. keys are transcription row IDs, not claimed physical specimen IDs. The only known runout bound is recorded separately from failure time. This campaign is useful for provenance, outcome-count and out-of-domain protocol screening; it must not be pooled with the frozen axial cohort or used as proof of a specimen-level surface feature effect.

## Immediate gate

Await the Al-Zuhairi S1–S13 files for the specimen join, censor and Lehner-overlap audit. Preserve the frozen v2 development folds and existing comparisons. Reconsider a separate rotating-bending evaluation only after campaign identity, predictor availability and study-level grouping are specified.
