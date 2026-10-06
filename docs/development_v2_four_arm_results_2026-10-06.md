# Development v2 four-arm comparison — 6 October 2026

**Status:** completed fixed-fold computational comparison, exploratory development evidence. Source and fold membership are the frozen 199-row v2 cohort, with 192 `R=0.1` experimental observations in the primary leave-publication-out track. The [precomparison protocol](development_v2_precomparison_protocol_2026-10-06.md), including its physical-cycle pre-score clarification, defines the arms and scores. The [implementation](../scripts/compare_development_v2.py) and [machine-readable outputs](../results/development_v2/) reproduce this report. Lower censored negative log likelihood (NLL), defined on the `log10` life density and runout survival probability, is better.

## Primary held-out publication scores

| Arm | Wu (41; 33 failures/8 runouts) | Chen (18; 18/0) | Matušů (133; 115/18) | Equal-publication macro NLL | Pooled 192-row NLL |
| --- | ---: | ---: | ---: | ---: | ---: |
| C0, pooled experimental Weibull | 1.64587 | 0.85725 | 1.32829 | 1.27714 | 1.35194 |
| C1, source-marginal experimental Weibull | 1.60490 | 0.91078 | 1.30327 | **1.27299** | **1.33089** |
| S0, all-source self-distillation, five-seed mean | 1.60536 | 0.91083 | 1.30726 | 1.27449 | 1.33375 |
| S1, observed-runout source filter, five-seed mean | 1.60475 | 0.91083 | 1.30431 | 1.27330 | 1.33158 |

S1−C1 macro NLL is **+0.00031**, while S0−C1 is **+0.00150** and S1−S0 is **−0.00119**. S1 is marginally better than C1 on Wu (−0.00015), worse on Chen (+0.00005) and Matušů (+0.00103). The fixed preliminary positive rule fails: S1 does not beat C1 on macro score or on two publications, and both its failure and runout macro NLLs are slightly higher than C1 (failure 1.22971 vs 1.22944; runout over Wu/Matušů 1.91716 vs 1.91623). Chen has no runout test record and is excluded from the runout macro.

| Seed | S0 macro NLL | S1 macro NLL | S1−S0 |
| ---: | ---: | ---: | ---: |
| 13 | 1.27546 | 1.27177 | −0.00369 |
| 29 | 1.27280 | 1.27457 | +0.00177 |
| 47 | 1.27592 | 1.27445 | −0.00148 |
| 71 | 1.27076 | 1.27193 | +0.00117 |
| 101 | 1.27748 | 1.27377 | −0.00371 |

The seed-level S1 macro range is 1.27177–1.27457. The five seeds are stochastic training replicates on **the same three real test publications**, not independent experiments. When Chen is held out, S0 and S1 are identical by design because both remaining training publications have documented real runouts. Reported means retain the precision of the stored per-row scores.

### Failure, runout and stress-support checks

C1 improves runout macro NLL relative to C0 (1.91623 versus 2.23383) while worsening failure macro NLL (1.22944 versus 1.19403). The S1 filter does not resolve that trade-off. On Wu's seven test stresses below the 30 MPa training minimum, C1 and S1 tail NLL are 1.34983 and 1.34952. On Matušů's 41 high-stress failures above the 99 MPa training maximum, they are 1.20896 and 1.21107. These are extrapolation subsets, so apparent aggregate differences cannot be read as within-support generalization.

## Secondary unseen-ratio transfer

Train all four arms on all 192 `R=0.1` rows and score the seven Romano `R=-1` first exposures **separately**, without fitted `R` effects or selection from these outcomes. Mean NLL is 5.40162 for C0, 3.27237 for C1, 3.24821 for S0 (five-seed mean; range 3.17143–3.29782), and 3.26747 for S1 (range 3.25317–3.27699). Romano's single runout incurs NLL 14.86710 under C1. These seven observations are a ratio/process transfer warning, not confirmation of synthetic augmentation and not part of the primary macro.

## Reproducibility and decision

The v2 reader verified the three frozen input blobs, 199 unique first exposures, publication folds, expected failure/runout counts, censor operators and source stops. Every primary source stayed out of its corresponding training set; Matušů's 11 series remained in its one publication. The weighted likelihood integrated synthetic and real contributions under the same source intercept. The analytic gradient agreed with an independent finite-difference check to `4.1×10⁻⁷`. All 48 fits converged without a boundary parameter; no predeclared seed was replaced or dropped. The maximum 161-versus-321-node training-objective difference was `1.47×10⁻⁷`; all predictive log-score checks were below `10⁻⁵`.

The primary output includes 2,304 real-test prediction rows (12 arm/seed combinations × 192 specimens), 36 fits, and 1,920 **training-only synthetic episodes**. The Romano challenge adds 84 real-test predictions, 12 fits and 960 separately logged synthetic training episodes. Four subcycle latent draws were rejected and redrawn before observation (two primary, two Romano); their counts are in the ledgers. An independent output audit checked event/bound identity against the frozen cohort, unique pseudo-IDs, measured parent stresses, source weights, no train/test source overlap, finite scores and quadrature tolerance. The `fit_problems.json` ledger is empty.

**Decision:** no observed primary augmentation advantage and no algorithm novelty claim from this M1-based self-distillation. The next research task is to investigate a mechanism bringing independently measured pretest/process or physics information, with further original campaigns and an untouched evaluation source. The already inspected Hamidi Nasab data remain development evidence; reserved sources were not scored in this comparison.
