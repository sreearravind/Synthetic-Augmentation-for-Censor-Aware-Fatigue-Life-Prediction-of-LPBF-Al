# Matušů 2026 fatigue workbook source screen (6 October 2026)

## Sources and status

- Authors' [open Zenodo record](https://zenodo.org/records/22230072), DOI 10.5281/zenodo.22230072; inspected `Data_Fatigue_Life_Only.xlsx` (33,851 bytes, MD5 `c6c2df499bc323928d55f08109f45678`) and `Preprint_Matusu_figures_and_tables.zip` (MD5 `a6a540f19d038d7b61ffa4cd964a472e`), especially Table 3, Fig. 13, and their captions.
- Related original research paper: Matušů et al., *Surface integrity, heat treatment and in-situ ageing effects on the fatigue behaviour of PBF-LB AlSi10Mg*, [10.1016/j.rineng.2026.112570](https://doi.org/10.1016/j.rineng.2026.112570). The full paper PDF was unavailable through the inspected access routes, so loading ratio, complete stop and crack criteria, and the exact meaning of every specimen suffix are **not yet independently checked** against its full methods. An indexed publisher excerpt states that selected runouts were subsequently loaded at higher amplitudes.
- Previous original experiment: Matušů et al. (2024), [10.1016/j.prostr.2024.03.035](https://doi.org/10.1016/j.prostr.2024.03.035), locally inspected. It describes four as-built heat-treatment groups from a single build, 11 S–N specimens per group, a 10^7-cycle runout condition, and subsequent higher-amplitude loading of runouts. Table 3 of the 2026 authors' archive marks exactly the four 41–44 series with a prior reference [18]. Assignment to the prior 2024 campaign is strongly supported by group descriptions and matching 11 initial rows per series; the full 2026 bibliography should confirm reference [18] before final publication wording.

## Workbook counts, preserving physical exposure

| Series family | Processing and surface from authors' Table 3 | Workbook rows | First reported exposures | Cycles < 10^7 | Cycles >= 10^7 | Later B/b loadings | Decision |
|---|---|---:|---:|---:|---:|---:|---|
| 41–44 | CLM2, recycled GE powder, as-built, NoHT/T240/T200/T300 | 49 | 44 | 39 | 5 | 5 | Previously reported family, excluded from new pool |
| 71–74 | CLM2, virgin Eckart powder, machined, four heat treatments | 52 | 44 | 36 | 8 | 8 | Candidate new family |
| 91–94 | CLM2, virgin GE powder, as-built, four heat treatments | 66 | 60 | 54 | 6 | 6 | Candidate new family; includes anonymous ID `XX` |
| C01–C03 | Aconity TWO, virgin Nikon SLM powder, as-built or machined plus polished | 35 | 30 | 25 | 5 | 5 | Candidate new family |
| **Total** | **15 series, four processing families** | **202** | **178** | **154** | **24** | **24** | 44 prior initial exposures, 134 candidate new initial exposures |

The three candidate new families together contain **153 episode rows = 134 first reported exposures + 19 later loadings**. Among the 134, 115 have shorter reported lives and 19 have cycles at or just above 10^7. The authors' Fig. 13 separately labels failure and runout symbols and illustrates the approximately 10^7 stopping region. Each of the 19 long-life candidate rows has a same-sheet `B` or `b` suffixed later-loading row matching its initial identifier. These are strong indications of 19 right-censored initial exposures, but the field in the workbook is labeled “Number of cycles, Nf,” without an explicit event column. The CSV deliberately labels events **provisional** and leaves every row quarantined from model training.

## Linkage and anomalies

- Specimen IDs must be scoped to the **sheet**: numeric IDs recur in different heat-treatment series. The 24 suffix rows pair one-to-one with the 24 initial rows at or above 10^7. Pair keys are `sheet + ID`, not ID alone. Later failure after a runout is a second loading of the same specimen, never another independent first-exposure failure.
- Series 92 contains `XX` at 55 MPa and 10,000,078 cycles, then `XXb` at 160 MPa and 2,960 cycles. This is a linked pair, but `XX` is an anonymous ID. **133 of 134** first exposures have numeric IDs; `XX` stays under a separate identity hold.
- An indexed excerpt of the 2026 paper says selected runouts were retested at **at least twice** the load amplitude. Four new-family pairs in the workbook are below 2×: 91/21B (90/50 = 1.80), 92/17B (90/50 = 1.80), 93/35B (110/60 = 1.833), and C02/9B (115/65 = 1.769). The suffix and initial runout still make linkage plausible; the wording or data require full-paper reconciliation. No B/b row is admitted to the candidate first-exposure file.
- Table 3 identifies three additional manufacturing/printing families, not 11 independent studies. The heat-treatment series share their source family. Future evaluation must preserve batch/source grouping and distinguish the Aconity and CLM2 routes.

## Durable screening files

- [Complete 202-row episode and source-role ledger](../data/candidates/matusu_2026_all_202_episodes_screen.csv): exact workbook stress/cycle values, source sheet/row, raw ID, linked initial ID, processing mapping, prior-family and later-loading exclusions.
- [134 candidate first reported exposures](../data/candidates/matusu_2026_new_134_first_exposure_candidates.csv): *provisional outcomes only*, including the flagged `XX` row. This is **not** an updated training set or a paper-ready censor cohort.

## Decision and next verification

Promising source with 134 potentially new initial exposures and approximately 19 censor observations, materially more valuable for this manuscript than the one-runout bending candidate. The decision is **quarantine pending full protocol and identity review**. Confirm the full paper's load ratio, stopping and crack criteria, Fig. 13 event coding, B/b handling, prior reference [18], and four less-than-2× pairs; determine whether `XX` is unique. Then, if justified, form a new versioned cohort and re-run a predeclared, printing-family-aware analysis. The locked 66-row exact cohort, existing results, and reserved Strauß/Kempf external tests are unchanged.
