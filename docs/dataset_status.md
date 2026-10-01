# Censor-aware fatigue life prediction of LPBF AlSi10Mg

This repository records literature-sourced experimental fatigue observations and source decisions for a planned synthetic-augmentation study. **No synthetic data have been generated or mixed with the experimental records.** Counts below describe candidate data, not a finalized modelling cohort or a journal acceptance threshold.

## Current data

| File | Meaning | Count |
| --- | --- | ---: |
| `data/experimental_master_80_candidate_records.csv` | Candidate first-exposure experimental rows from Wu 2021, Romano 2018 as re-reported by Tognan 2024, and Chen 2024 | 80 |
| `data/chen_2024_tables_3-5_27_failures.csv` | Exact table rows from three specimen geometries, all failed | 27 |
| `data/roveda_2024_table_4_20_episodes.csv` | Exact fatigue **test episodes** with unresolved runout/retest linkage; held outside the 80-row master | 20 |
| `docs/source_audit.md` | Extraction, outcome, feature-timing, and inclusion decisions | — |

The master currently has **66 known failures, eight explicit right-censored Wu runouts, and six Tognan threshold-labelled outcomes whose true failure/censoring status remains unresolved**. The six must be excluded from event-based modelling until adjudicated. The Romano experiment and Tognan re-report are one underlying study, not independent cohorts.

The Roveda source says runout survivors were retested at a higher stress. Its Table 4 does not identify which failure episode belongs to which previous runout. Consequently its 20 episodes must not be counted as 20 independent specimens. The runout episodes have valid within-episode right-censoring at 10 million cycles, but pooling the rows as independent subjects would duplicate some specimens.

Postfracture initiator/“killer defect” measurements in Chen and Roveda are retained for descriptive checks. They are **outcome-informed** and are excluded from pretest fatigue-life prediction inputs. Roveda performed pretest micro-CT, but Table 4 does not provide a matched pretest defect value for each specimen.

## Source papers

- Wu et al. (2021), *International Journal of Fatigue*, DOI [10.1016/j.ijfatigue.2021.106317](https://doi.org/10.1016/j.ijfatigue.2021.106317).
- Romano et al. (2018), *Engineering Fracture Mechanics*, DOI [10.1016/j.engfracmech.2017.11.002](https://doi.org/10.1016/j.engfracmech.2017.11.002); subset re-reported by Tognan et al. (2024), DOI [10.1016/j.cma.2023.116521](https://doi.org/10.1016/j.cma.2023.116521).
- Chen et al. (2024), *International Journal of Fatigue* 182, 108163, DOI [10.1016/j.ijfatigue.2024.108163](https://doi.org/10.1016/j.ijfatigue.2024.108163), Tables 2–5.
- Roveda et al. (2024), *Materials & Design* 244, 113170, DOI [10.1016/j.matdes.2024.113170](https://doi.org/10.1016/j.matdes.2024.113170), Section 2.3 and Table 4.

Local row and episode IDs in the CSVs follow printed table order. They are **not author-assigned specimen IDs**. The previous graphical reading of Romano Figure 7 is a separate approximate, potentially overlapping candidate set and is not included in the exact master.

## Next data decision

Seek the specimen-level linkage of Roveda's runout-to-retest episodes, and adjudicate the six Romano/Tognan threshold outcomes against the original test histories. Then freeze a model-eligible experimental cohort and define study-held-out validation before fitting a synthetic generator.
