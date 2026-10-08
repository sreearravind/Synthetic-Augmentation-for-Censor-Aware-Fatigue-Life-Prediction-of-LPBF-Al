# 2.5 Training-only synthetic augmentation and fixed source-selection strategy

## 2.5.1 Source-conditioned generation of synthetic fatigue episodes

The synthetic-data comparison was designed to test whether additional training episodes drawn from an already fitted fatigue-life model altered prediction on an unseen publication. Within each outer publication-held-out fold, the source-marginal experimental-only model C1 (Section 2.4) was fitted exclusively to the original first-exposure records in the two training publications. Its fitted parameters, \(\widehat{\theta}_{C1}=(\widehat{\alpha},\widehat{\beta},\widehat{\kappa})\), defined the probabilistic teacher; \(k=\exp(\kappa)\), the source-effect standard deviation \(\tau=0.25\), and the stress coordinate \(x=\log_2(\sigma_a/100\ \mathrm{MPa})\) retain the definitions in Section 2.4. No held-out fatigue outcome, source offset, or specimen-specific information entered teacher fitting or subsequent generation.

For each training publication \(s\), a source offset was sampled once per generation replicate from its posterior conditional on *real training observations*:

\[
p(b_s\mid D_{s,\mathrm{real}},\widehat{\theta}_{C1})
\ \propto\
\phi(b_s;0,\tau^2)
\prod_{i\in D_{s,\mathrm{real}}}
f_Z(z_i\mid b_s)^{\delta_i}
S_Z(z_i\mid b_s)^{1-\delta_i}.
\tag{2.5a}
\]

The implementation approximated this posterior on the 161-point Gaussian–Hermite quadrature grid used for the C1 likelihood, then drew one offset shared by all synthetic episodes from that publication in that replicate. The publication offset was therefore not resampled independently for each pseudo-observation.

A total of \(n_s\) synthetic episodes was generated for each eligible training publication, where \(n_s\) denotes its number of original training observations. Generation preserved the number of observations allocated to each recorded within-publication condition series: for each synthetic episode in a series, a real parent was selected with replacement from that same training series, and its measured nominal stress amplitude was reused. Thus the generator did not interpolate to new stresses, introduce unseen process combinations, or extend the series-specific measured stress support. Publication identity and condition-series provenance were retained in the separate generator ledger, but stress amplitude remained the sole specimen-level predictor in the fitted models.

At the sampled stress \(\sigma_{a,j}^{*}\) and shared source offset \(b_s^{*}\), latent logarithmic fatigue life was drawn by the inverse-transform construction

\[
z_{j,\mathrm{latent}}^{*}
=
\widehat{\alpha}
+\widehat{\beta}
\log_2(\sigma_{a,j}^{*}/100\ \mathrm{MPa})
+b_s^{*}
+\frac{\log_{10} E_j}{\widehat{k}},
\qquad E_j\sim\operatorname{Exp}(1),\quad
\widehat{k}=\exp(\widehat{\kappa}).
\tag{2.5b}
\]

The pre-score implementation rule rejected and redrew any \(z_{j,\mathrm{latent}}^{*}<0\), at the same parent stress and sampled source offset, until the simulated life represented at least one cycle. This explicitly conditions the synthetic draw on a physically countable life; the rejection counts were logged. A non-finite draw or more than 10,000 such rejections caused a replicate to be flagged rather than silently accepted.

## 2.5.2 Synthetic outcomes and the two augmentation arms

The three primary training publications document a common \(10^7\)-cycle testing stop, although the selected Chen records contain failures only. Each accepted latent draw was converted into a synthetic *observed* failure or right-censored episode at that stop:

\[
(\delta_j^{*},N_{j,\mathrm{obs}}^{*})
=
\begin{cases}
(1,10^{z_{j,\mathrm{latent}}^{*}}),
& z_{j,\mathrm{latent}}^{*}\leq 7,\\[2pt]
(0,10^7),
& z_{j,\mathrm{latent}}^{*}>7.
\end{cases}
\tag{2.5c}
\]

A synthetic runout accordingly represents survival to the specified bound, not failure at \(10^7\) cycles. The stopping decision was evaluated in logarithmic space to avoid exponentiating extremely long finite latent lives. Latent life and observed event/bound were kept distinct in the generation audit; only the latter contributed to student fitting.

Two augmentation arms were evaluated with the same source-marginal Weibull accelerated failure time model as C1. **S0**, the unrestricted self-distillation control, retained synthetic episodes from every training publication with the documented common stopping policy. **S1**, the fixed censor-support filter, retained only episodes belonging to a training publication with at least one *observed real training runout* at its documented stop. Under the frozen primary cohort, Wu and Matušů met this rule when present in training, whereas Chen did not. S1 omitted Chen-derived episodes even though Chen's methods describe the source-wide stopping policy; it did not select individual episodes on the basis of their generated failure/runout outcomes. For each fold and seed, S0 and S1 drew from the identical generated episode pool, so the arm difference was the predetermined source-eligibility rule rather than separate random generations. When Chen was held out, both remaining training publications met the rule, and S0 and S1 used identical synthetic observations.

The five generation seeds (13, 29, 47, 71 and 101) were fixed before comparison and applied separately within each outer training fold, with source-specific random streams. They represent stochastic repetitions of training augmentation on the same physical data, not additional experimental campaigns. S1 was a *fixed, source-level filter*, not a gate learned from test performance or a specimen-level utility model.

## 2.5.3 Weighted source-marginal student likelihood

Every original experimental training record retained unit likelihood weight. Within each eligible publication \(s\), every generated episode received weight \(w_{sj}=2/n_s\), such that the total *effective synthetic likelihood weight* per publication was two. This limit prevented a publication with more generated rows from receiving proportionally greater synthetic influence solely because of its original sample count. In S1, episodes from an ineligible publication were omitted (equivalently, assigned zero synthetic weight). The numerical count of generated rows was never interpreted as an increase in independent experimental specimens.

For augmentation arm \(a\in\{S0,S1\}\), the student was fitted by minimizing the negative log of the weighted source-marginal likelihood

\[
\mathcal{L}_{s}^{(a)}(\theta)
=
\int \phi(b;0,\tau^2)
\left[\prod_{i\in D_{s,\mathrm{real}}}
\ell_i(\theta,b)\right]
\left[\prod_{j\in D_{s,\mathrm{syn}}}
\ell_j^{*}(\theta,b)^{\,w_{sj}^{(a)}}\right]\,db,
\quad
\ell(z,\delta\mid\theta,b)=
f_Z(z\mid\theta,b)^{\delta}
S_Z(z\mid\theta,b)^{1-\delta},
\tag{2.5d}
\]

\[
\widehat{\theta}_{a}
=\arg\min_{\theta}
\left\{-\sum_{s\in\mathrm{training\ publications}}
\log\mathcal{L}_{s}^{(a)}(\theta)\right\}.
\tag{2.5e}
\]

Here \(D_{s,\mathrm{real}}\) contains original training outcomes, \(D_{s,\mathrm{syn}}\) contains that publication's generated episodes, and \(w_{sj}^{(a)}\) is \(2/n_s\) for an included episode and zero otherwise. The source-offset integral encloses the *joint* real and weighted synthetic conditional likelihoods for the publication: each pseudo-episode was not treated as a separate source with an independent random effect. Fractional synthetic weights make this a training-weighted likelihood intervention rather than a conventional likelihood for newly observed independent specimens. The original C1 teacher was not replaced by synthetic-only fitting; each S0 or S1 student was refitted to the same original training observations with the indicated additional weighted terms. The parameters, source-effect variance, numerical integration rules and optimization bounds followed Section 2.4.

## 2.5.4 Data separation and implementation safeguards

Teacher fitting, source-offset posterior calculation, parent sampling, stochastic generation, source filtering and student fitting were repeated *inside each outer training partition*. The excluded publication contributed neither observed outcomes nor generated episodes to fitting; its source offset was not inferred from its test data. The four fitted arms were evaluated only on original, held-out experimental records using the same censor-aware failure-density and runout-survival score defined in Section 2.4 and further specified in the validation protocol (Section 2.6).

The implementation checked frozen cohort and fold identities, first-exposure membership, publication disjointness, stress and censor-operator validity, source-stopping bounds, synthetic-ID uniqueness, numerical finiteness, optimizer convergence and 161-versus-321-node quadrature agreement. Synthetic records were stored separately from the experimental master with their fold, seed, publication, series, parent stress identifier, latent and observed lives, event indicator, stopping bound, sampled source offset, rejection count and arm-specific weights. The fitted-parameter and real-test prediction ledgers were likewise archived. No seed, effective-weight cap, eligibility rule or C1 source-effect variance was selected from outer-test results. Because the generator and student used the same parametric family and no independent pre-fatigue physical features, the augmentation arms assess self-distillation and weighting effects, **not** acquisition of new fatigue evidence or a learned selective-augmentation algorithm.

---

## Evidence and editorial notes (not part of manuscript prose)

- **Frozen implementation:** [\`scripts/compare_development_v2.py\`](../scripts/compare_development_v2.py); source posterior in \`posterior_offset\`, series-preserving generation in \`generate\`, weighted source likelihood in \`weighted_objective_grad\`, and study-held-out fitting in \`main\`.
- **Precomparison lock:** [\`docs/development_v2_precomparison_protocol_2026-10-06.md\`](../docs/development_v2_precomparison_protocol_2026-10-06.md), including its pre-score clarification for subcycle/very-long latent lives. This Methods description reports the completed implementation, not a proposed alternative algorithm.
- **Data and validation:** [\`data/cohorts/development_v2_199_2026-10-06.csv\`](../data/cohorts/development_v2_199_2026-10-06.csv); [\`data/validation/development_v2_grouped_fold_assignments_2026-10-06.csv\`](../data/validation/development_v2_grouped_fold_assignments_2026-10-06.csv). Only the 192 R=0.1 first-exposure records from Wu, Chen and Matušů enter the primary three-fold evaluation; the seven Romano R=−1 records were evaluated in a separately labelled ratio-transfer challenge.
- **Archived outputs:** [\`results/development_v2/\`](../results/development_v2/) includes the real-test prediction ledger, fit coefficients, synthetic generation ledger, Romano challenge ledger and convergence/problem records. The earlier reported primary four-arm findings are in [\`docs/development_v2_four_arm_results_2026-10-06.md\`](../docs/development_v2_four_arm_results_2026-10-06.md); Results belong in a later manuscript section, not in Section 2.5.
- **Important distinction:** The implementation draws a synthetic parent stress *from an existing measured series*, not an interpolated stress. It samples *one quadrature-supported source offset per publication per seed*, not one per synthetic row. S1 removes Chen's generated episodes based on real training-runout availability, not on whether the pseudo-episode is a simulated runout.
- **Equation notation:** Equations (2.5a)–(2.5e) are draft anchors only; renumber them when the full manuscript is typeset. In Eq. (2.5d), for runouts \(z\) is the recorded log10-cycle bound, consistent with Section 2.4's \(c_i\).
- **Next single task:** Draft Section 2.6, specifying primary publication-held-out and secondary ratio-transfer evaluation, censored NLL and its two event-type contributions, publication macro-averaging, stress-support diagnostics, the fixed preliminary-positive decision rule, and the provenance/limitations of separately scored external campaigns. Do not rerun, retune or pool prior results during drafting.
