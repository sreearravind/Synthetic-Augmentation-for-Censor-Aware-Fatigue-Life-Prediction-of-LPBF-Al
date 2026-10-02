# AlSi10Mg fatigue-life validation protocol

**Status:** prospective analysis rules, frozen 2 October 2026; no model fitted and no performance claimed. The split manifest and record membership were generated from the three source CSVs with input SHA-256 checksums. The manuscript's proposed algorithm and synthetic generator remain to be specified in later tasks.

## 1. Eligible experimental data and independent units

| Tier | Records | Failures | Right-censored | Source groups | Role |
| --- | ---: | ---: | ---: | --- | --- |
| Smooth exact core | 66 | 57 | 9 | Wu 2021 (41; 33/8), Romano 2018 (7; 6/1), Chen 2024 (18; 18/0) | Primary holdouts |
| Independent graph tier | 26 | 20 | 6 | Zhang 2022 (20; 15/5), Glodež 2020 (6; 5/1) | Prespecified training supplement and external diagnostic |
| Chen R5 exact notch | 9 | 9 | 0 | Chen 2024, shared with 18 smooth Chen rows | Geometry transfer only |

The five ambiguous Romano/Tognan labels and 20 Roveda test episodes remain excluded. Romano and Tognan refer to the same underlying experiment and must never occupy opposite sides of a source split. The 26 graph rows retain their approximate label; they are not promoted into the exact cohort. All record IDs and source assignments are in `record_membership_2026-10-02.csv`.

## 2. Frozen comparisons

| Analysis | Train / test | Valid interpretation |
| --- | --- | --- |
| **E0**, exact-only baseline | Leave one of Wu, Romano or Chen out. Train on the other two exact smooth studies; test on the held-out exact study. Three folds. | Main study-held-out performance, subject to severe between-study shift. |
| **E1**, graph-assisted training | Identical exact test IDs in each E0 fold; add *both* independent graph studies to that fold's training set. Three paired folds. | Whether approximate graph training changes performance on untouched exact specimens. Compare E1−E0 within each test study. |
| **X0**, external graph check | Train on all 66 exact smooth rows; test on Zhang alone or Glodež alone. The other graph source is excluded. Two folds. | Approximate, out-of-domain diagnostic; (R=0) is absent from exact training. Do not pool its score with E0. |
| **N0**, notch transfer | Train on smooth exact 66; test on nine Chen R5 notched specimens. One split. | Within-study geometry transfer, **not** independent source validation. Run only if a model accepts a documented notch/geometry and stress-basis descriptor. |

Nine frozen folds are listed in `study_holdout_folds_2026-10-02.csv`. E0 and E1 have exactly the same three test sets. Do not select a favourable fold, remove a difficult source after seeing results, or use row-random cross-validation as the headline analysis.

**Domain warnings.** Romano is the only exact study at (R=-1); holding it out asks a model trained at (R=0.1) to extrapolate in stress ratio. The graph studies use (R=0) and different processing, surface, geometry and frequency conditions. A study split tests transfer across all these changes together; it cannot identify a causal effect of any one factor. Chen contributes no runouts, so its test fold cannot directly check censor survival. Wu contributes eight of the nine exact runouts. Three exact studies do not support a robust population-level claim or a specimen-level confidence interval that ignores clustering.

## 3. Outcome and stress contract

- For an observed failure use (z_i=\log_{10} N_{f,i}) and event δ=1. For a runout use (c_i=\log_{10} C_i), event δ=0 and the recorded lower bound. Preserve the `>`/`≥` metadata; both yield (S_Z(c_i\mid x_i)) for a continuous model. Never treat the bound as a failure life.
- Wu's eight runouts have a 10⁷ lower bound, Romano has one ≥ bound, Zhang has five conservative 10⁸ bounds, and Glodež has one 4×10⁶ bound. For graph runouts the arrow's plotted x coordinate remains evidence, not the model bound.
- Use the same pretest stress representation for every fold, preferably stress amplitude with (R) supplied as a separate feature. (\sigma_a=(\sigma_{\max}-\sigma_{\min})/2); for (R=0), (\sigma_a=\sigma_{\max}/2). Do not use postfracture defect descriptors as pretest predictors. Preserve the `local maximum at notch` basis for Chen R5 and never silently mix it with smooth nominal stress.
- A missing build orientation stays missing; treatment, surface and geometry descriptors must reflect what the paper reports. Source identity may define a split but is not a predictive feature for an unseen study. Fit encoding, missing-value handling, scaling, any dimensionality reduction and any synthetic generator **inside each training fold only**.
- Any proposed algorithm must output a valid predictive density (f_Z(z\mid x)) and survival function (S_Z(c\mid x)) to enter the primary censor-aware comparison. A point-only algorithm may appear in a clearly labelled failure-only descriptive comparison, never as an equivalent censor-aware competitor.

## 4. Scoring and reporting

**Primary:** mean right-censored negative log-likelihood on the held-out experimental records, in log-cycle units:

\[
\overline{\mathcal L}=\frac{1}{n}\sum_i\left[-\delta_i\log f_Z(z_i\mid x_i) -(1-\delta_i)\log S_Z(c_i\mid x_i)\right].
\]

This uses observed failure density and survival probability beyond the documented censor bound. Right-censored log-likelihood is a proper score under its censoring assumptions [Rindt et al., AISTATS 2022](https://proceedings.mlr.press/v151/rindt22a.html). Record the number of failures and censored observations alongside every fold score. Compare models on the **same test specimens and same log-cycle density convention**. Present the three E1−E0 paired differences by study and their descriptive mean/median, without a significance claim.

**Secondary:** log-cycle MAE on failures only, explicitly labelled as incomplete-case and unable to score runouts. Also show the failure-density and runout-survival terms separately as diagnostics. Avoid a headline pooled C-index, IPCW Brier score or nominal 95% coverage claim with these sparse and heterogeneous censoring patterns. If later data permit such metrics, specify common horizons and censoring assumptions before calculation.

**Uncertainty:** for the graph tier, report center-read results and a bounded reading sensitivity using stored x/y pixel halfwidths. For failures, evaluate predeclared lower/center/upper life and stress readings without changing the outcome. For runouts, vary graph-read stress while leaving the paper-supported censor bound fixed. This is a robustness envelope, **not** a statistical confidence interval. Repeat E1 with flagged Zhang Z05 excluded and report the difference; do not infer Glodež specimens 3/4 or the unmatched mark as extra observations.

**Training and selection:** any tuning uses training studies only and never uses the held-out test study. With only two exact training groups in E0, an inner study split may make a proposed model impossible to fit; use a limited, declared configuration or report that the fold is infeasible. Do not replace it with row-level tuning leakage. Synthetic records, when developed, may be created from a fold's training data only, remain labelled synthetic, and have no role in test counts or test metrics.

## 5. Decision gate for the next manuscript task

Before fixing the new algorithm architecture, inspect the nine fold definitions and confirm that the planned predictors are actually available in every training and test source. Then implement one transparent probabilistic censor-aware baseline and its E0 predictions, followed by the paired E1 and X0 analyses. A method claim requires improvement on **untouched exact test sources**, plus clear limits for the unseen (R=-1) and (R=0) domains. No fixed specimen-count threshold guarantees journal acceptance.

### Primary inputs and methodological reference

- `data/cohorts/smooth_core_66.csv`; `data/cohorts/confirmed_outcomes_75.csv`.
- `data/graph_digitized/independent_sources_26_approximate.csv` and its [extraction audit](https://github.com/sreearravind/Synthetic-Augmentation-for-Censor-Aware-Fatigue-Life-Prediction-of-LPBF-Al/blob/main/docs/independent_graph_digitization_2026-10-01.md).
- [Rindt, Hu, Steinsaltz and Sejdinovic (2022), *Survival regression with proper scoring rules and monotonic neural networks*](https://proceedings.mlr.press/v151/rindt22a.html).
