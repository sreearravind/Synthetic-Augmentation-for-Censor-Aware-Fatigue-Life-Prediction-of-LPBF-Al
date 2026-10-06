# Next experimental source screen (6 October 2026)

Purpose: find independent, original LPBF AlSi10Mg fatigue specimens with an event label, defensible censoring time, and traceable stress, loading, and manufacturing metadata. This is a candidate screen, not an expansion of the locked 66-row exact core, a model fit, or an external evaluation.

## Priority decisions

| Priority | Source | What can be used | Gate and disposition |
|---|---|---|---|
| 1 — extract and independently audit | Kramer et al. (2025), [10.1007/s40964-025-01288-x](https://doi.org/10.1007/s40964-025-01288-x), Appendix A2 | 19 tabulated new KH/LoF fatigue rows: 18 failures, one 10,000,000-cycle runout; vertical, machined, rotating bending, R = −1, 50 Hz. Candidate rows: [CSV](../data/candidates/kramer_2025_appendix_A2_19_unadjudicated.csv). | Verify transcription against Appendix A2 and Fig. 5, check whether any repeated or second confirmation tests are in the figure, preserve KH versus LoF. A2 has no unique specimen IDs. Do not count second confirmation tests from prose. HD 10 rows were taken from authors' earlier publication [45] and are excluded from this new cohort. This is one experimental study with two groups; bending domain requires separate reporting from axial tests. |
| 2 — acquire and audit dataset | Matušů et al. (2026), [10.5281/zenodo.22230072](https://doi.org/10.5281/zenodo.22230072), `Data_Fatigue_Life_Only.xlsx` | Open 33.9 kB fatigue-life workbook accompanies a new surface integrity / heat treatment / in-situ ageing study. The actual rows were not accessible in this screen. | Inspect workbook and preprint for individual identifiers, loading, stop cycles, failure/runout codes, and overlap with Matušů 2024. Do not estimate specimen count or import until provenance and first exposure are resolved. |
| 3 — axial graph audit | Afroz et al. (2024 online; 2025 volume), [10.1007/s40964-024-00759-x](https://doi.org/10.1007/s40964-024-00759-x), Fig. 9 | Original smooth axial R = 0.1 and −1 series across as-built, machined, and polished conditions. | Table 5 contains *average* lives, not individual specimen outcomes. Read Fig. 9 symbols and their event coding independently; establish the exact stop before admitting any censored row. If unavailable, admit only clear failures as graph-derived data and keep averaged table values out of specimen counts. |
| 4 — conditional existing-folder leads | Matušů 2024 [10.1016/j.prostr.2024.03.035](https://doi.org/10.1016/j.prostr.2024.03.035); Roveda 2024 [10.1016/j.matdes.2024.113170](https://doi.org/10.1016/j.matdes.2024.113170) | Axial R = 0.1, stated 10^7 stop, published failures and runouts. | Runouts were retested at higher stress. Link retest failures to original specimen/runout exposure or exclude ambiguous later episodes. Do not treat a second loading of one specimen as an independent specimen. |
| 5 — failure-only additions | Zhang 2018; Uzan 2017/2018; Tang and Pistorius 2019 | Original graph marks may provide additional failures. | Verify stress basis and specimen provenance. No explicit runout stopping cycle established in the current screen; Uzan papers may overlap. These sources cannot alone strengthen censor-specific evidence. |

## Exclusions and locks

- Strauß and Löwisch (2024), [10.1007/s40964-024-00577-1](https://doi.org/10.1007/s40964-024-00577-1), remains the **reserved, unscored primary external test**. Kempf (2022), [10.1016/j.prostr.2022.03.009](https://doi.org/10.1016/j.prostr.2022.03.009), remains the **reserved, unscored secondary test**. Fini (2025) remains backup. Do not train, tune, select augmentation, or report scores using their outcomes. Papers reusing these campaigns need specimen-level overlap screening before any training use.
- Wu, Romano, and Chen already form the exact core; Glodež and Chen files with alternate names are not new studies. Hamidi Nasab has already been scored externally. Muhammad and Fernandes provide the previously extracted failure-only graph tier, not new censor rows. Do not count a source twice merely because it has a different filename or a follow-on analysis.
- Candidate counts do not imply journal sufficiency or a predictive gain. The Kramer candidate offers one runout in a bending study; axial runout evidence is still the limiting need.

## Immediate next task

Independently read Kramer Appendix A2 against its figure and manufacturing protocol, confirm all 19 entries and the one runout, and record an adjudication note for the unlisted runout confirmation tests. In parallel, inspect the Matušů 2026 workbook for specimen identity and censoring fields. Only then decide whether any rows may enter a *new versioned* development cohort; keep the locked exact folds and external tests intact.

### Source locations

- Kramer 2025, methods §2 (loading and 10^7 threshold), results §3.3 (HD reuse, runout confirmations), Appendix A2 (individual results): https://link.springer.com/content/pdf/10.1007/s40964-025-01288-x.pdf
- Zenodo 2026, dated record and file listing: https://zenodo.org/records/22230072
- Afroz, methods §2.2 and results §3.3: https://link.springer.com/article/10.1007/s40964-024-00759-x
- Earlier folder screening: [unscored source screen](unscored_experimental_source_screen_2026-10-06.md).
