# Matušů 2026 full-text protocol audit (6 October 2026)

## Documents checked

- User-provided full 2026 article, [Matušů et al., Results in Engineering 32, 112570](https://drive.google.com/file/d/1T5dFDHVOwxAectVLCl-lB5cMBjjSmBb8/view?usp=drivesdk), DOI [10.1016/j.rineng.2026.112570](https://doi.org/10.1016/j.rineng.2026.112570). Specific evidence: Table 3 (four build platforms and source labels), §2.9 (fatigue protocol), Fig. 13 (failure/runout symbols), references [18] and [26].
- Authors' [Zenodo experimental workbook and figure archive](https://zenodo.org/records/22230072), DOI 10.5281/zenodo.22230072; workbook MD5 `c6c2df499bc323928d55f08109f45678`. Preserved [202-episode ledger](../data/candidates/matusu_2026_all_202_episodes_screen.csv).

**Correction to earlier provisional audit:** Table 3's reference **[18] is Matušů et al., *Fatigue analysis and heat treatment comparison of additively manufactured specimens from AlSi10Mg alloy*, International Journal of Fatigue 185 (2024) 108357, DOI [10.1016/j.ijfatigue.2024.108357](https://doi.org/10.1016/j.ijfatigue.2024.108357).** It is not the previously suggested Procedia Structural Integrity article 10.1016/j.prostr.2024.03.035. The 41–44 source-family exclusion remains valid; its cited provenance is now exact.

## Protocol and revised candidate decisions

| Field or question | Full-text result | Treatment in candidate file |
|---|---|---|
| Test and ratio | §2.9: constant-amplitude **uniaxial** fatigue, **R = 0.1**, resonant pulsators, **90–120 Hz**. | Record mode, ratio and frequency interval for all candidate series. Do not assume a specimen-specific frequency. |
| Stopping and event | §2.9: test ends on a frequency drop >10 Hz, load-amplitude change >±0.5 kN, static-load change >±0.5 kN, or completion of **10^7 cycles**; a specimen reaching 10^7 without failure is a runout. Fig. 13 identifies runouts separately. | For a long-life first exposure, use right censor at 10,000,000 cycles; preserve the precise instrument count as `cycles_reported`. Short-life entries are treated as reported failures, subject to no additional invalid-test flag in the workbook. |
| Prior source | Table 3 marks 41–44 with [18], whose bibliography identifies the International Journal of Fatigue article above. | Exclude **44 first exposures and five later loadings** of 41–44 from any new 2026 contribution. Do not count the earlier Procedia or Wiley analyses as additional independent campaigns. |
| Later loading | §2.9 reports retesting selected runouts after visual crack inspection. All workbook `B/b` suffix rows match an earlier same-sheet long-life ID. | Exclude **24 later loadings** as independent first exposures, including 19 in the additional series. Keep exposure linkage in the full episode ledger. |
| Four amplitude anomalies | §2.9 states subsequent loading at **at least 2×** initial amplitude. Workbook gives 91/21B 1.80×, 92/17B 1.80×, 93/35B 1.833×, C02/9B 1.769×. | **Genuine paper/workbook inconsistency unresolved.** The later-loading rows are already excluded. Preserve the original first-exposure outcomes, but flag the four pairs in this audit and do not cite the 2× rule as universal for every recorded pair. |
| Anonymous ID | Series 92 `XX`: 55 MPa, 10,000,078 cycles, linked to `XXb`: 160 MPa, 2,960 cycles. The article does not define `XX`. | Exclude `XX` from the new protocol-checked 133-row file pending identity verification. It remains visible in the 134-row provisional ledger. |
| Authors' regression | §2.9 first says only failures enter K&V regression and runouts never enter it, then says runouts enter if their stress exceeds the lowest-stress failure. Fig. 13 also labels some runout series “included in fit.” | Internal methodological wording is inconsistent. It does not change the workbook's distinct failure/runout outcomes. Do **not** reuse authors' fitted K&V curves as specimen records or assume their fitting rule. |
| Cross-paper overlap beyond [18] | Reference [26], DOI 10.1111/ffe.14442, is cited regarding surface/contour porosity in series 41 and 91. Table 3 marks prior reuse explicitly for 41–44, but not 91–94. | Three additional printing platforms are candidate evidence within **one 2026 paper**. Retain a family-level cross-paper overlap check for 91 and related group publications before claiming wholly new experimental campaigns. |

## Count and artifact

From 202 workbook episode rows, 49 belong to cited prior family 41–44. The other 153 comprise **134 first reported exposures** (115 failures, 19 runouts) and **19 later loadings**. One first-exposure runout has anonymous ID `XX`. The [protocol-checked, identified 133-row candidate file](../data/candidates/matusu_2026_protocol_checked_133_first_exposures.csv) contains **115 failures and 18 right-censored runouts**, with explicit `event_observed` (1=failure; 0=censor), `censor_lower_bound_cycles`, R, frequency range, and processing family. It remains **outside** the locked 66-row exact core.

These 133 rows are literature-exact with respect to tabulated stress and cycles and source-defined event coding, but are still a **candidate tier** pending cross-paper family review and a decision on the four anomalous retests. The 2026 paper contributes up to three printing-platform families, not 11 independent study holdouts. No model fit, synthetic generation, external scoring, or novelty claim is made here.

## Next gate

Map the 91-series fatigue records against reference [26] and any other prior reports that reused the same build; then define a versioned development cohort and study/platform-aware sensitivity design *before* seeing reserved Strauß/Kempf outcomes. The anonymous `XX` record can remain excluded without blocking this work.
