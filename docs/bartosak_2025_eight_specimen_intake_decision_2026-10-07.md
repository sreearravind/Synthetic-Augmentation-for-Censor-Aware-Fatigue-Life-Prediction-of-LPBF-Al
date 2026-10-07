# Bartošák 2025: eight-specimen public deposit intake

**Decision (7 October 2026):** Register eight matched, pretest-XCT **low-cycle fatigue candidate specimens** for a separately labelled case study. Do **not** add them to the frozen 199-row stress-controlled high-cycle fatigue (HCF) development cohort, its fixed folds, or censor/synthetic-augmentation comparisons. There are **no runouts** in this eight-row deposit.

## Evidence and reconciliation

- The user-supplied `Bartosak_Dataset.zip` is 11,029 bytes, MD5 `b7ccc508a3abb290fc6f729258fc97c3` (matches the [Zenodo record](https://zenodo.org/records/13828238)), SHA-256 `61e409e261c992acd5119a330242d125aa164acabb1cb6b110192b6f8619e50c`.
- The fatigue CSV has exactly eight unique IDs. Each has exactly one identically numbered defect CSV; no missing or extra IDs. Every defect file has 100 complete rows, sorted by **projected area** in descending order: 800 *defects*, eight *fatigue specimens*.
- The deposit's defect README defines projected area (mm², perpendicular to loading), sphericity (unitless) and minimum distance to the free surface (mm). It says these are the 100 largest projected-area defects per specimen. The [paper's methods](https://doi.org/10.1016/j.matdes.2025.113926) state that selected specimens underwent whole-gauge X-ray CT **prior to low-cycle fatigue testing**; the reported voxel size is 22 µm. Exact individual scan timestamps are not supplied. The ranking is by a pretest geometrical quantity, without selecting a defect using the later fracture origin.
- The fatigue README calls `delta e pl [-]` **plastic strain range**, and defines `Nf` at a **10% decline in maximum stress relative to the saturated trend**. All eight entries are Nf values (417–2577 cycles); the deposit has no event/status or stopping-cycle column and documents no runout. Treat these as eight protocol-defined failure observations, **not eight fracture-cycle measurements**. Build directions: four vertical and four horizontal.

| Original ID | Build | Plastic strain range | Nf, cycles | Largest CT area, mm² | Largest defect: sphericity / surface distance, mm | Nearest surface distance among top 100, mm |
| --- | --- | ---: | ---: | ---: | --- | ---: |
| 4 | Vertical | 0.00651 | 463 | 0.14552 | 0.16 / 2.07433 | 0.57190 |
| 7 | Vertical | 0.00213 | 2577 | 0.41019 | 0.11 / 1.98945 | 0.37329 |
| 8 | Vertical | 0.00352 | 1124 | 0.14806 | 0.16 / 0.61787 | 0.47789 |
| 10 | Vertical | 0.00498 | 719 | 0.65901 | 0.09 / 1.88928 | 0.43993 |
| 14 | Horizontal | 0.00510 | 541 | 0.72312 | 0.09 / 0.73943 | 0.00000 |
| 15 | Horizontal | 0.00669 | 417 | 0.55292 | 0.09 / 1.52095 | 0.02200 |
| 16 | Horizontal | 0.00354 | 758 | 0.64715 | 0.10 / 1.44652 | 0.02200 |
| 17 | Horizontal | 0.00204 | 1503 | 0.88642 | 0.09 / 1.01493 | 0.02198 |

The linked [machine-readable candidate ledger](bartosak_2025_lcf_pretest_ct_8_candidate_2026-10-07.json) preserves the original IDs, source field semantics, file paths and ZIP checksum. `nearest_surface_distance_among_top100_mm` is a derived minimum over the published **area-ranked subset**, not necessarily the nearest defect in the entire gauge. The sphericity and distance next to largest area refer to **that same first-ranked defect**. Do not sum projected areas and call the result a porosity fraction.

## Implication for the manuscript

This is genuine specimen-matched pretest defect information, but its eight observations are **strain-controlled LCF** with a different failure definition and no right-censored test. The current HCF model uses nominal stress amplitude and studies runouts at much longer lives. No direct stress conversion, pooled training, synthetic augmentation claim, or censor-validation claim is justified from this deposit. It may support a carefully separated methods illustration after a question and evaluation protocol are fixed; with eight specimens, it cannot sustain a publication-transfer comparison by itself.

**Next source task:** seek an independent *stress-controlled HCF* AlSi10Mg study or open deposit containing original specimen IDs, pretest XCT/roughness values, stress amplitude and R, life and explicit runout stop. Wu's already included 41 specimens are a possible feature-enrichment route only if a public per-ID pretest XCT table is found; they are not independent additional observations.
