# Data path without waiting for author correspondence

## Decision

Use **66 smooth, confirmed-outcome first-exposure experimental rows** for the initial stress–life benchmark. They comprise 57 failures and nine right-censored runouts from Wu 2021 (41 rows), Romano 2018 as re-reported by Tognan 2024 (seven), and Chen 2024 L40/L10 (18). The `smooth_core_66.csv` file has one row per first exposure and retains the exact source DOI and table location. `bound_operator` distinguishes exact failure cycles (`=`), Wu's strict `>10,000,000` runout, and Romano specimen 3's observed stop at 8,889,311 (`≥`).

`confirmed_outcomes_75.csv` contains the same 66 plus Chen's nine R5 notched failures as an explicit **geometry sensitivity** set. Chen reports local maximum stress for R5 (`Kt=1.27`), while smooth rows use nominal axial stress. Pooling those stress values without a geometry and stress-basis distinction would produce a false comparison. The two CSVs are nested views, **not 141 independent observations**.

`excluded_ambiguous_5.csv` lists Romano/Tognan IDs 4, 8, 9, 10 and 12. Their source's ≥2-million-cycle threshold class cannot establish a physical censoring event. The 20 Roveda Table 4 test episodes remain in their separate source ledger: all three runouts were retested, and the paper does not identify the matching failure rows. An optional later author reply can expand this cohort but is not a prerequisite to the benchmark.

## Alternatives considered

| Option | Decision | Reason |
| --- | --- | --- |
| Treat Tognan's five remaining “runouts” as censored | Reject for main analysis | Its event label is assigned from a cycle threshold, not an explicitly linked physical stopping reason. |
| Match Roveda runouts to high-stress failures using repeated √area | Reject for main analysis | Similar postfracture defect sizes are not specimen IDs. Incorrect pairing would double count a specimen. |
| Use only Roveda's three runout rows | Hold | They are distinct survivor episodes, but adding an all-censored treatment cohort while excluding possible linked failures creates a selected outcome sample. |
| Digitize S–N figures with open runout symbols | Separate sensitivity tier | Plotted coordinates are approximate, some glyphs overlap, and a graph marker may duplicate a table record. Preserve digitization bounds and deduplicate before use. |
| Generate synthetic labels to “replace” missing experimental histories | Reject | Generated outcomes cannot resolve whether a real specimen failed or survived. Synthetic records belong to training folds only. |
| Broaden from AlSi10Mg to other Al alloys | Defer | A different alloy changes the material question and adds a larger domain shift. |

## Scientific limits and permitted inputs

The smooth core has nine censored rows, **eight from Wu and one from Romano**, and Chen contributes no tabulated runout. This supports a transparent method-development benchmark; by itself it is weak evidence for broad transfer of censoring behaviour. There is no universal Q1-journal specimen-count threshold. Strength depends on provenance, leakage control, baselines, uncertainty and genuinely independent validation.

The shared pretest predictors are applied stress, load ratio, documented orientation, finish, heat condition, frequency and smooth geometry where available. Unknown Romano orientation and frequency remain missing. Specimen-matched numerical pretest CT descriptors appear in the Romano subset but not in comparable form for Wu or Chen. Therefore the **pooled core supports a stress–life study, not a claim of pooled specimen-level defect-aware prediction**. Chen's and Roveda's fracture-origin descriptors are measured after failure and must not be fed to a pretest predictor.

For any later algorithm comparison, group splits by **underlying experimental study** (Romano and Tognan are one group). Fit imputers, encoders, scalers, synthetic generators and sample-selection rules only on the training studies. Hold-out scores must be measured only on real, untouched experimental data. Treat runouts as lower bounds in an appropriate survival/censor-aware objective, never as failures at the stop cycle. With only three underlying studies and heterogeneous protocols, leave-one-study-out results are exploratory rather than a definitive external-validity claim.

## Focused Drive source screen

The supplied folder includes the Wu paper already represented by 41 rows. A focused check of Fini et al. 2025 (orientation/heat/surface factorial), Zhang et al. 2022 (three build directions), Glodež et al. 2020 (eight stress levels), Fernandes et al. 2024 (notches and heat treatments), and selected heat/surface papers found plotted S–N points or aggregate/model-parameter tables. For example, Glodež Table 2 gives individual applied stresses but not each life; Zhang Fig. 4 differentiates failures and 10⁸-cycle stops; Fernandes S–N figures mark runouts. None of these observations was silently counted as a new exact specimen row. They are candidates for a **separately labelled, uncertainty-bounded graphical extraction** in the next data task.

## Provenance

- Candidate 80-row inventory and primary source audit: [`data/experimental_master_80_candidate_records.csv`](../data/experimental_master_80_candidate_records.csv), [`docs/source_audit.md`](source_audit.md).
- Outcome adjudication: [`data/outcome_adjudication_2026-10-01.csv`](../data/outcome_adjudication_2026-10-01.csv).
- New cohort files: [`smooth_core_66.csv`](../data/cohorts/smooth_core_66.csv), [`confirmed_outcomes_75.csv`](../data/cohorts/confirmed_outcomes_75.csv), [`excluded_ambiguous_5.csv`](../data/cohorts/excluded_ambiguous_5.csv).
- [Wu et al. 2021](https://doi.org/10.1016/j.ijfatigue.2021.106317); [Romano et al. 2018](https://doi.org/10.1016/j.engfracmech.2017.11.002); [Tognan et al. 2024](https://doi.org/10.1016/j.cma.2023.116521); [Chen et al. 2024](https://doi.org/10.1016/j.ijfatigue.2024.108163); [Roveda et al. 2024](https://doi.org/10.1016/j.matdes.2024.113170).
- Further figure candidates: [Fini et al. 2025](https://doi.org/10.1007/s40964-024-00712-y); [Zhang et al. 2022](https://doi.org/10.1016/j.ijmecsci.2022.107336); [Fernandes et al. 2024](https://doi.org/10.1016/j.tafmec.2024.104553).
