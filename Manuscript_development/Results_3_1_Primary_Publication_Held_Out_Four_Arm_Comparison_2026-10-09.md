# 3.1 Publication-held-out performance of experimental-only and synthetic-augmented models

**Option A Results and Discussion working draft, 9 October 2026.** Only Sections 3.1.1–3.1.4 and Tables 3.1–3.3 are manuscript prose. The evidence/figure-planning notes following the horizontal rule are editorial records. This draft reports the existing frozen primary v2 comparison; **no additional fits, scores, cohort changes or retrospective parameter selection** were made.

## 3.1.1 Predictive performance across the three held-out publications

The primary leave-one-publication-out evaluation used 192 original, numerically reported first-exposure fatigue records at stress ratio \(R=0.1\): 166 observed failures and 26 right-censored runouts. All models predicted the same real records from Wu et al. (2021; \(n=41\)), Chen et al. (2024; \(n=18\)) and Matušů et al. (2026; \(n=133\)) while each publication was excluded in turn from its training partition. Table 3.1 reports mean censored negative log likelihood (NLL; lower is better). C0 and C1 were fitted using real training observations only; the S0 and S1 entries are arithmetic means over the five prespecified training-generation seeds.

**Table 3.1.** Publication-held-out censored predictive NLL for the four frozen models. The primary macro is the unweighted mean of the three held-out-publication means. The pooled mean weights each of the 192 individual test records equally and is secondary. The S0 and S1 numbers are five-seed averages, not five independent experimental replications.

| Model arm | Wu (41; 33 failure / 8 runout) | Chen (18; 18 / 0) | Matušů (133; 115 / 18) | **Equal-publication macro NLL** | Pooled 192-record NLL |
| --- | ---: | ---: | ---: | ---: | ---: |
| C0 — pooled experimental Weibull AFT | 1.64587 | 0.85725 | 1.32829 | 1.27714 | 1.35194 |
| **C1 — source-marginal experimental Weibull AFT** | **1.60490** | 0.91078 | **1.30327** | **1.27299** | **1.33089** |
| S0 — all-source parametric self-distillation | 1.60536 | 0.91083 | 1.30726 | 1.27449 | 1.33375 |
| S1 — fixed observed-runout source filter | 1.60475 | 0.91083 | 1.30431 | 1.27330 | 1.33158 |

The experimental-only source-marginal model C1 attained the lowest **mean primary macro** NLL, 1.27299, compared with 1.27714 for the simpler pooled experimental model C0. That aggregate difference was not uniform across publications. C1 reduced the Wu score from 1.64587 to 1.60490 and the Matušů score from 1.32829 to 1.30327, but increased the Chen score from 0.85725 to 0.91078. The contrast shows that accounting for source-to-source variation changed the likelihood assigned to genuinely held-out fatigue outcomes in a publication-dependent way; the direction was not consistently favorable for every source.

Adding teacher-generated episodes did not reduce the five-seed mean macro NLL below C1. The unrestricted S0 mean was 1.27449, an increase of \(+0.00150\) relative to C1; the prespecified runout-supported S1 filter yielded 1.27330, an increase of \(+0.00031\) relative to C1. S1 was lower than S0 by 0.00119 NLL, but this relative gain over an augmented control did **not** amount to a gain over the real-only C1 reference. Relative to C1, S1 changed the three publication scores by approximately \(-0.00015\) on Wu, \(+0.00005\) on Chen and \(+0.00103\) on Matušů. Thus only **one of the three** held-out publications improved with S1. In the Chen-held-out fold, S0 and S1 were identical for each fixed seed because the two remaining training publications both contained observed real runouts and therefore both passed the fixed S1 eligibility rule.

The specimen-weighted NLL displayed the same broad ordering (C1, 1.33089; S1, 1.33158; S0, 1.33375; C0, 1.35194), although its numerical values differ from the publication macro because Matušů provides most of the individual test records. For that reason, the unweighted publication macro remains the principal cross-source metric; pooling individual records would otherwise give the single largest publication a disproportionate influence.

## 3.1.2 Failure-density and runout-survival trade-offs

The event-specific breakdown showed that the overall model rankings masked an important contrast between predicted failure density and predicted survival at documented stopping cycles. Table 3.2 gives separately the equal-publication mean NLL of observed failures and of right-censored runouts. The failure macro averages the three publication-specific failure scores. The runout macro averages **Wu and Matušů only** because the 18 selected Chen outcomes were all failures. These two quantities therefore have different contributing publication sets and should not be interpreted as a single uniformly weighted partition of the overall macro.

**Table 3.2.** Event-specific primary publication-held-out NLL (lower is better). For S0 and S1 the values are means over the five prespecified synthetic seeds. A failure contributes density in \(\log_{10}\) life; a runout contributes predictive survival at its source's documented bound.

| Model arm | Failure-density macro NLL (three publications) | Runout-survival macro NLL (Wu and Matušů) |
| --- | ---: | ---: |
| C0 | **1.19403** | 2.23383 |
| C1 | 1.22944 | 1.91623 |
| S0 | 1.23261 | **1.90529** |
| S1 | 1.22971 | 1.91716 |

Moving from C0 to C1 reduced the runout-survival macro NLL from 2.23383 to 1.91623, while increasing the failure-density macro from 1.19403 to 1.22944. The improved runout likelihood therefore coexisted with less favorable likelihood for observed failures. This trade-off is important in an experimental cohort with recorded runouts: the overall NLL alone would not reveal which event class drove the improvement.

Unrestricted S0 self-distillation reduced runout-survival macro NLL modestly relative to C1 (1.90529 versus 1.91623), but its failure-density macro worsened (1.23261 versus 1.22944) and its overall primary macro NLL increased. The fixed-filter S1 arm did not retain that small runout advantage: relative to C1, its failure macro rose from 1.22944 to 1.22971, and its runout macro rose from 1.91623 to 1.91716. The effect of synthetic training was consequently dependent on both the generation eligibility rule and the type of real fatigue outcome being scored. These results do not support the claim that preserving a real-runout source in a fixed synthetic filter is sufficient to improve performance on unseen publications.

## 3.1.3 Variation among the five fixed synthetic-generation seeds

The stochastic generation protocol used the same five predetermined seeds for S0 and S1, and all of them were retained. Table 3.3 reports the equal-publication macro NLL for each generation seed. C1, the fixed experimental-only comparator, remained at 1.27299 regardless of seed. A lower seed-specific score does not constitute a separate validation experiment because all seeds re-use the same three held-out original publications.

**Table 3.3.** Primary equal-publication macro NLL across fixed synthetic-generation seeds. The final column is S1 minus S0; a negative value favors S1 over S0 for that seed.

| Generation seed | S0 macro NLL | S1 macro NLL | S1 − S0 |
| ---: | ---: | ---: | ---: |
| 13 | 1.27546 | 1.27177 | −0.00369 |
| 29 | 1.27280 | 1.27457 | +0.00177 |
| 47 | 1.27592 | 1.27445 | −0.00148 |
| 71 | 1.27076 | 1.27193 | +0.00117 |
| 101 | 1.27748 | 1.27377 | −0.00371 |
| **Five-seed mean** | **1.27449** | **1.27330** | **−0.00119** |

S0 varied from 1.27076 to 1.27748 across the five seeds; S1 varied from 1.27177 to 1.27457. The direction of the S1–S0 contrast changed with the seed: S1 was better than S0 for seeds 13, 47 and 101, but worse for seeds 29 and 71. Some individual S0 and S1 seeds fell below the fixed C1 reference despite the respective **five-seed means** remaining above it. Selecting only those favorable realizations would therefore give a misleading picture of augmentation utility.

The seed comparison is also consistent with the limited intervention made by the filter. S1 used the same generated episodes as S0 but omitted synthetic contributions from Chen whenever Chen was a training publication; it did not learn a continuous specimen-level selection weight. Seed-level variation should consequently be understood as sensitivity to the fixed train-time self-distillation draw and source-eligibility decision, not as reproducibility across new physical experimental campaigns.

## 3.1.4 Stress-support diagnostics and primary decision

Publication-held-out testing exposed extrapolation relative to the stresses measured in the two training publications. Seven Wu test observations fell below the 30 MPa training-fold minimum, whereas 41 Matušů test failures exceeded the 99 MPa training-fold maximum. All 18 Chen test observations were within the training-fold stress span. These classifications were determined from the original real training stresses before evaluation and did not change the primary fold scores or macro.

For the seven below-range Wu records, the C1 and S1 mean censored NLL values were 1.34983 and 1.34952, respectively. For the 41 above-range Matušů failures, the corresponding values were 1.20896 and 1.21107. The S1 difference was therefore very small and of opposite sign in these two out-of-range subsets. The lower numerical NLL of either out-of-range subset compared with some in-range records should not be interpreted as evidence that extrapolation is intrinsically easier; the subsets comprise different stresses and potentially different fatigue-outcome compositions. A simple numerical stress boundary also does not account for publication-linked differences in processing, surface preparation or other unmodelled factors.

The predeclared preliminary-positive rule required the **five-seed mean** S1 macro NLL to be below both C1 and S0, improvement against C1 on at least two of three held-out publications, and no increase in either the failure or runout macro relative to C1. S1 was lower than S0 overall but higher than C1; it improved over C1 on only Wu, and it slightly increased both event-specific macros. The rule was therefore **not satisfied**. The experimental-only C1 model was retained as the primary comparison anchor rather than promoting a favorable seed or changing the source filter after inspection.

Taken together, the three-publication analysis demonstrates a reproducible, provenance-preserving comparison in which source-marginal modeling changed the balance between failure-density and runout-survival likelihood, while same-model synthetic self-distillation offered **no consistent out-of-publication advantage** under the fixed protocol. The finding applies to the implemented stress-only Weibull model family, three primary publication groups, recorded censoring policies and predetermined generation weights; it is not a conclusion that every form of physics-informed or feature-guided synthetic augmentation must fail. The separately scored \(R=-1\) Romano challenge and the later Beretta and Al-Zuhairi checks have different roles and are not included in this Section 3.1 primary macro.

---

## Evidence, consistency and figure-planning notes (not manuscript prose)

- **Authoritative measured values:** [Four-arm frozen comparison report](../docs/development_v2_four_arm_results_2026-10-06.md), checked against the machine-readable [fold-metrics ledger](../results/development_v2/fold_metrics.csv). Tables 3.1–3.3 reproduce the fixed numeric values at five-decimal display precision, and the event-specific S0 failure/runout macros were computed by applying the already-frozen Section 2.6 aggregation rule to that ledger, not by re-scoring fatigue outcomes. The underlying record-level predictions are archived in [results/development_v2/predictions_real_test.csv](../results/development_v2/predictions_real_test.csv).
- **Frozen decision rule:** [Development v2 precomparison protocol](../docs/development_v2_precomparison_protocol_2026-10-06.md). The required conditions were recorded before fitting. The primary S1 macro difference versus C1 is +0.00031 (worse), the S0 difference versus C1 is +0.00150 (worse), and the S1 difference versus S0 is −0.00119 (better); signs follow the Section 2.6 definition of first arm minus comparator. The S0 runout macro 1.90529 is lower than C1's 1.91623 even though the S0 overall macro is higher.
- **Membership and grouping:** The real primary test cohort contains 41 Wu, 18 Chen and 133 Matušů first exposures; 192 original records in total. Matušů's three platforms are part of one publication. The seven Romano records in the frozen 199-row inventory are part of a *separate* development ratio challenge and do not enter Tables 3.1–3.3.
- **Integrity:** [Run metadata](../results/development_v2/run_metadata.json), [fit parameters](../results/development_v2/fit_parameters.csv) and [fit-problem ledger](../results/development_v2/fit_problems.json) document the fixed seeds, original input blobs, training-only synthetic weights, and successful fit checks. The completed audit reports 36 primary fits (plus 12 secondary Romano fits), no optimizer problem, a primary maximum 161/321-node training-objective difference of \(1.47\times10^{-7}\), and predictive log-score discrepancies below \(10^{-5}\). These integrity results can be placed in a short reproducibility note or supplement when the full article is assembled.
- **Suggested eventual main figure (not generated in this task):** A compact, legible two-panel graphic could show (a) C0/C1/S0/S1 mean NLL by Wu, Chen and Matušů, with the equal-publication macro separately marked, and (b) C0/C1/S0/S1 failure versus runout macros. Label the S0/S1 estimates “five-seed means,” avoid error bars implying five independent publications, identify the absent Chen runout term, and do not present the small NLL contrasts as significance. If journal page limits demand it, retain Table 3.1 in the article and move Table 3.3 to supplementary material. No plotting was performed here.
- **Claim alignment:** [Manuscript evidence reconciliation](../docs/manuscript_claim_evidence_reconciliation_2026-10-08.md) and [Option A title and abstract](../docs/manuscript_title_abstract_options_2026-10-08.md). Neither the fixed S1 rule nor the same-teacher S0/S1 intervention is a learned augmentation algorithm; external cases cannot be represented as fresh independent confirmation of an advantage.
- **Next manuscript task:** Draft Section 3.2 from the separately archived seven-record Romano \(R=-1\) transfer metrics, preserving its status as a development-domain warning rather than new external confirmation. Then draft Section 3.3 for the Beretta and Al-Zuhairi fixed-model checks, keeping them in separate source panels/tables and not pooling NLL across fundamentally different tests.
