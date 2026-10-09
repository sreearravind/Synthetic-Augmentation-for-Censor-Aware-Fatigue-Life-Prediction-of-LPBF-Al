# Selective synthetic augmentation: feasibility and evidence gate

**Status: design assessment, 6 October 2026.** This is the next manuscript-method task after the user reviewed the Hamidi Nasab extraction and M1 was scored. It is not an implemented generator, a performance result, or a frozen novelty claim. The purpose is to decide what the present evidence can support before adding synthetic rows.

## 1. What the current experiments can identify

| Independent original study | Evidence | Records (failure/runout) | R | Major source-linked conditions |
| --- | --- | ---: | ---: | --- |
| Wu 2021 | Printed specimen table | 41 (33/8) | 0.1 | Ground/polished, stress relieved, 85 Hz; orientation varies within source |
| Romano 2018, including Tognan re-report | Printed specimen values | 7 (6/1) | −1 | Machined; distinct study and protocol, missing orientation |
| Chen 2024 smooth | Printed specimen values | 18 (18/0) | 0.1 | Machined/ground, 20 Hz, vertical; no runout |
| Zhang 2022 | Approximate graph readings | 20 (15/5) | 0 | Distinct surface/processing protocol; 10⁸-cycle bound |
| Glodež 2020 | Exact stress, graph life | 6 (5/1) | 0 | Separate processing and 4 × 10⁶-cycle bound |

The **exact primary cohort is 66 specimens but only three independent studies**. Stress ratio −1 is present in only one exact source. Surface/heat treatment and test frequency are largely tied to study, while Chen provides no censoring information. Wu supplies eight of the nine exact runouts. The two graph sources add independent campaigns but also a lower precision tier, R=0 domain and different censor stops; Zhang contributes 20 of their 26 observations. These facts prevent reliable separation of a transferable treatment or stress-ratio effect from source differences, and make a learned source-general augmentation gate fragile.

The M1 external result on Hamidi Nasab 2019 is already inspected: M1−E0 mean censored NLL was −0.0198 across 46 visible positions at the locked tau=0.25, driven by better runout survival while failure density worsened. This campaign may be cited as **previously used development evidence** in later algorithm design, but it cannot be reused as an untouched confirmation of a synthetic algorithm motivated by that result. User review of its ledger is recorded separately; no row-by-row independent second-reader digitization is documented.

## 2. Candidate augmentation mechanism to investigate

The proposed contribution remains a **selective train-time use of synthetic observations**. A conservative candidate has four components:

1. **Within-source generator.** On each training split, fit a censor-aware teacher using *only* its original experimental studies. Draw stresses within each eligible training source's measured support, condition on recorded pretest variables only, and draw latent failure life from the teacher's survival distribution. Apply that source's documented censoring stop to produce either an observed synthetic failure or a right-censored synthetic lower bound. Preserve source, stress basis, R, geometry, evidence tier and a `synthetic=true` flag. Do not invent a new independent study or turn a runout bound into a failure.
2. **Support and precision filter.** Reject candidates outside measured stress/covariate support and candidates requiring an unidentified treatment or stress-ratio effect. Keep exact and graph-derived experimental rows separate. The current hand-set graph reading intervals are bounded sensitivities, **not** a calibrated probability distribution for sampling graph measurement error.
3. **Study-level utility rule.** Compare a student model trained with each permitted synthetic stratum against the identical experimental-only student on training-only held-out original studies. A synthetic stratum can receive positive weight only if it helps censored NLL without an unacceptable deterioration in its failure-density and runout-survival components under a predeclared rule. Weight selection and all teacher/student fitting must be nested inside the outer source holdout. A future method can learn a gate only when enough distinct training studies support it; otherwise use a fixed, declared accept/reject rule and describe the exercise as exploratory.
4. **Real-only evaluation.** Score original experimental specimens on studies not used by the teacher, generator, gate, preprocessing, or student. Keep synthetic rows out of test counts, calibration plots and reported experimental sample size. Compare with E0 and M1, a no-augmentation student, and a conventional equal-count synthetic augmentation control. Match the test positions and censor-aware metric; report failure/runout terms separately.

Generating labels from an M1 teacher does **not** create independent information. Any benefit to a student would be regularization or a changed training emphasis and must survive a new-study comparison. “More rows” alone is not a scientific novelty claim. A trained gate selected on the three already inspected exact source folds would be especially susceptible to their source-specific patterns.

## 3. Decision before coding or claiming novelty

**Do not yet train a learned gate or optimize its thresholds on Wu/Romano/Chen/Hamidi Nasab outcomes and call the resulting score external validation.** The viable next data task is to establish at least one genuinely unused, original experimental campaign for a future algorithm test and expand the independent training campaigns. No fixed count of specimens or studies guarantees a journal tier; the relevant evidence is distinct sources, traceable first-exposure outcomes, supported censor bounds, overlapping covariates and out-of-source performance.

Screen candidate papers with this extraction contract: experimental campaign and specimen provenance; duplicate/re-report links; first-exposure failure cycles or explicitly stated runout stop; per-specimen event glyph or table row; stress maximum/range/amplitude and R for conversion; nominal versus local/notch stress; geometry, orientation, finish, thermal condition and frequency; reading interval and independent reader evidence for graphs. Hold unresolved repeat tests or arrow-only stopping cycles out of censor-aware scoring.

Previously identified leads have different roles: Muhammad et al. 2023 has useful two-ratio/finish experiments but its runout stop is unverified in the available inspection; Fernandes et al. 2024 has smooth R=0 series with an unverified censor stop; Fini et al. 2025 states a 10⁶-cycle stop but rotating bending and overlaps make digitization harder. These are **screening leads**, not approved cohorts. Choose and lock the role of each source before examining its prospective algorithm score. New sources with explicit specimen tables and censor bounds should take priority.

**Next single task:** screen the available unscored original studies for extractable first-exposure records and explicit runout bounds, label each prospective campaign as additional training, untouched test, or exclusion, and record overlap and stress-basis checks. Only after that source decision should generator and utility-rule parameters be frozen and implemented.
