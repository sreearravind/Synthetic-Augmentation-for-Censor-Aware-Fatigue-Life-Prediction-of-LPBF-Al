# Kramer 2025 Appendix A2 audit (6 October 2026)

Source: Steffen Kramer et al., *Impact of different pore types on the tensile and fatigue properties of AlSi10Mg parts produced by laser powder bed fusion*, DOI [10.1007/s40964-025-01288-x](https://doi.org/10.1007/s40964-025-01288-x). Inspected original PDF pp. 11307–11308, 11310–11311, 11315 (Appendix A2) and the [full-size Fig. 5](https://link.springer.com/article/10.1007/s40964-025-01288-x/figures/5). Source candidate file: [19 Appendix A2 rows](../data/candidates/kramer_2025_appendix_A2_19_unadjudicated.csv).

## Transcription check

The 19 KH/LoF entries in the candidate CSV were compared one by one with an independent reading of Appendix A2's columns for stress amplitude and load cycles. Result: **19/19 exact matches, zero transcription discrepancies**.

| Group | A2 rows | Failure | Right-censored at 10,000,000 cycles | Verified stress/cycles pairs (MPa / cycles) |
|---|---:|---:|---:|---|
| Keyhole (KH) | 10 | 9 | 1 | 80/10000000 (runout); 85/6574900; 90/144100; 95/259900; 100/55700; 105/115700; 110/80700; 120/139200; 140/75200; 150/42400 |
| Lack of fusion (LoF) | 9 | 9 | 0 | 20/203400; 30/317500; 40/118000; 45/110500; 50/37400; 55/89700; 60/48700; 70/19700; 80/13100 |
| High density (HD) | 10 shown in A2 | — | — | **Excluded here:** methods and Fig. 5 identify this series as reused from Wexel et al. (2024), DOI 10.1016/j.procir.2024.05.032. |

The figure uses half-filled marks for runouts. It shows the KH 80 MPa / about 10^7-cycle runout and HD 60 MPa / about 10^7-cycle reused runout, consistent with A2. LoF plotted marks are failures. Figure positions are an independent *event and cohort* cross-check; plotted coordinates are not used to overwrite the exact A2 values. Some marks could overlap, so the graph cannot establish the number of unique specimens at a given coordinate.

## Protocol and censor decision

The paper specifies vertically built cylindrical specimens subsequently machined, rotating-bending fatigue at R = −1, 50 Hz, and a high-cycle range extending to 10^7 cycles. It says specimens exceeding 10^7 are counted as runouts; A2 lists 10,000,000 cycles for KH at 80 MPa. The defensible event representation is a right-censored observation at 10^7 cycles, *not* failure at 10^7.

Section 3.3 says both runout stress amplitudes were confirmed with a second test. It does **not** supply separate specimen identifiers or a second KH row in A2; a repeated mark in Fig. 5 could coincide exactly. Treat the A2 row as **one reported runout**, not two. Do not invent an additional specimen or claim that the confirmation test was the same physical specimen. The identity and numerical result of any further test remain unreported here.

The KH and LoF rows appear to be original results from this paper; the source explicitly identifies only the HD series as prior-work reuse. They form **one study/campaign with two process-parameter groups**, not two independent held-out studies. The pronounced porosity regimes, rotating bending, and one censored result make this a distinct-domain candidate; any future training analysis must retain group and loading labels and must not be described as solving the axial runout shortfall.

## Disposition

**Source-table transcription verified; training eligibility remains conditional.** Keep the 19 rows in `data/candidates/` and preserve the locked 66-row exact core, its exact-only folds, and the reserved Strauß/Kempf external sources. If a versioned development cohort is proposed later, document this audit, screen cross-paper overlap, and evaluate bending domain shift separately before model fitting. No results or model scores were produced in this audit.

The [Matušů 2026 Zenodo workbook](https://zenodo.org/records/22230072) was identified, but the available web retrieval could not decode its XLSX binary. Its row count, censor coding, and relation to Matušů 2024 remain unverified; no dataset entries were inferred.
