# Beretta 2022 ESA benchmark: supplementary intake and source gate

**Date:** 7 October 2026. **Decision:** Preserve a fully transcribed **candidate outcome ledger**, with the roughness table separate. Do not change the frozen development v2 cohort, train on the reported roughness, score the source, or claim a validated feature-plus-censor cohort.

## Sources and exact population

- [Main article (user-supplied PDF)](https://drive.google.com/file/d/1btsilFsrGV-8j_uxbsMF-8J55MtftNXt/view), Beretta et al., *Materials & Design* 218 (2022) 110713, DOI [10.1016/j.matdes.2022.110713](https://doi.org/10.1016/j.matdes.2022.110713): §§3.2, 3.3, 3.7; Table 3 and Appendix Table 18.
- [Supplementary Material (user-supplied PDF)](https://drive.google.com/file/d/1OWi75fQx1aALCtrLfXo-36EbqrZTdSnx/view): Tables 1, 4 and 6, PDF pages 2, 4 and 5. The manuscript and supplement are distinct PDFs; this is the advertised raw specimen-level data.
- [Machine-readable, unscored candidate ledger](../data/candidates/beretta_2022_esa_cylindrical_32_specimens_40_exposures_candidate_2026-10-07.json). Source IDs are composite **surface condition + FN number + batch** (e.g., AB:FN7-243); `FN7` alone repeats across batches, and M/AB are separate specimens. Diameter, stress range, actual life or bound, event, exposure sequence and source table are retained.

| Cylindrical series | Unique specimens / first exposures | First-exposure failures | First-exposure runouts | Extra retest exposures | Total table entries |
| --- | ---: | ---: | ---: | ---: | ---: |
| As-built, Table 4 | 19 | 15 | 4 | 4 | 23 |
| Machined, Table 1 | 13 | 10 | 3 | 4 | 17 |
| **Total** | **32** | **25** | **7** | **8** | **40** |

The **40** entries are test exposures, not 40 independent specimens. Machined FN2-243 has two consecutive runouts at different stress ranges, followed by a failure, so the eight repeated exposures contain **one additional runout and seven later failures**. Across all exposures there are eight runout entries and 32 failures; for a first-exposure survival cohort there are **seven runouts and 25 failures**. The later failure after a runout must not be counted as an independent first-exposure life.

## Protocol and value reconciliation

The supplement headings show **Δσ in MPa** (stress range), not stress amplitude. The main article states axial load-amplitude control, nominal R=0.1 and ~35 Hz. Candidate amplitude is therefore explicitly **Δσ/2**; original Δσ is preserved. Failure means 10% stiffness reduction. The manuscript specifies interruption after **5×10^6 cycles**; the supplementary tables say “run-out” without printing the cycle number in each row. Candidate bounds at 5×10^6 inherit that stated protocol, tagged as such.

**One unresolved discrepancy:** Table 4 reports AB **FN1-245**, Δσ=75 MPa, a failure at **5.6×10^6 cycles**, beyond the manuscript's stated 5×10^6 interruption rule. Preserve the reported failure and its flag; do not correct it to 5×10^5, reclassify as a runout, or drop it silently. Any later role decision should include a prespecified sensitivity excluding this one record.

Builds 242, 243 and 245, R=0.1, and composite FN IDs distinguish this candidate from the frozen Romano R=−1 seven-row series and the 91–94 platform; the cross-publication independence check remains explicit before admitting rows. The wishbone component tables use different geometry/local stress and a separate 10^7-cycle stopping rule, so they are outside this cylindrical candidate.

## Roughness join: available, but predictor blocked

Supplement Table 6 provides **11** AB composite IDs in batches 243 and 245, all matched exactly to Table 4 first exposures: **eight failures and three 5×10^6 runouts**. It reports Rt, Rv and √area in µm; there are no matching roughness rows for AB batch 242 or the machined group. This makes a narrow same-ID table join possible, but it does **not** establish a prospective predictor.

Main article §3.7 describes four gauge-surface areas but also says the reported cylindrical profile measurements were taken **near crack initiation sites**; it does not explicitly establish measurement time or that the selected site and summary were fixed before fatigue. In the supplement, √area in roughness Table 6 is **identical to the fracture-origin Table 5 value for seven IDs** (all five 243 IDs; 245 FN5 and FN7), approximately equal for 245 FN4 (183.8 versus 183.3 µm), different for 245 FN3 (226 versus 256 µm), and the fracture-origin table is N/A for 245 FN1 and FN2. These comparisons do not prove how Table 6 was generated, but they preclude treating its √area as an independently established pretest metric. Table 5 itself is explicitly a **fracture-origin** descriptor, including corrosion-pit annotations, and is not a pretest feature.

The published Rt/Rv were measured on the specimen's surface, yet site choice relative to the later fracture and measurement timing remain unresolved. For any future predictive analysis, the original *pre-fatigue, outcome-blind*, whole-gauge feature extraction and a pre-specified rule for choosing measured areas would need to be documented. Do not impute group roughness for missing IDs or select the eventually failing location in a runout/failure classifier. The methods call the equipment a Keyence confocal microscope while Appendix Table 18 has a “Stylus” heading; preserve that discrepancy.

## Adjudication and next task

1. The supplied supplement **resolves the requested exact stress/life/event/ID/retest join** for the cylindrical population. There is no need to request author data to use these as source-table **candidate outcomes**.
2. **The feature gate is not met:** Table 6 Rt/Rv timing and outcome-independent site selection are unresolved; Table 5 and origin-like √area may leak post-test information. No row is labelled “feature-ready.”
3. **Next single step:** predeclare Beretta's **32 first exposures** as either a separate held-out R=0.1 outcome-and-censor check or a future development source, document the 5.6×10^6 protocol anomaly and the non-independent retests, and audit overlap with the existing publications. Only after the role is fixed should any locked model be evaluated. A prospective roughness analysis remains conditional on independently documented pretest extraction; the supplied two PDFs do not establish it.
