# 2.6 Publication-held-out validation, censor-aware scoring and external evaluation

**Option A working manuscript draft, 9 October 2026.** The manuscript prose comprises Sections 2.6.1–2.6.6. Evidence notes after the divider are editorial, not manuscript prose. This task does not introduce new fits, comparisons or selection rules.

## 2.6.1 Primary publication-held-out evaluation

The primary analysis evaluated predictive transfer to a publication excluded from fitting, rather than randomly withholding specimens from a known publication. The 192 original first-exposure observations at stress ratio \(R=0.1\) contained 166 failures and 26 right-censored runouts. They formed three leave-one-publication-out folds: Wu et al. (2021), 41 specimens (33 failures and eight runouts); Chen et al. (2024), 18 failures; and Matušů et al. (2026), 133 specimens (115 failures and 18 runouts). For each fold, the complete held-out publication, including every processing platform, condition series and runout, was excluded from training. The Matušů platform families and 11 series remained within one publication group rather than constituting multiple independent holdouts.

The other two publications supplied the experimental-only training observations for C0 and C1 (Section 2.4) and the training-only source-conditioned generation and fitting data for S0 and S1 (Section 2.5). Model estimation, teacher source-offset posterior calculations, synthetic parent selection, generation and student refitting were repeated within each fold without using that fold's test outcomes. All arms were scored on the identical original real-specimen test records; synthetic episodes never entered the evaluation cohort. C0 and C1 were evaluated once per fold, whereas S0 and S1 used the five prespecified random seeds 13, 29, 47, 71 and 101. Publication identifiers defined held-out units and source-effects groups, not transportable specimen-level predictors.

## 2.6.2 Censored predictive negative log likelihood

The primary endpoint was censored predictive negative log likelihood (NLL) on original held-out experimental first exposures. Let \(z_i=\log_{10}(N_i)\) be the recorded logarithmic failure life, \(c_i=\log_{10}(N_{\mathrm{stop},i})\) the recorded right-censoring lower bound, and \(\delta_i=1\) for a fracture and \(\delta_i=0\) for a runout. For model arm \(m\), the per-record loss was

\[
L_{i,m}=-\delta_i\ln \widehat f_{Z,m}(z_i\mid\sigma_{a,i})
-(1-\delta_i)\ln \widehat S_{Z,m}(c_i\mid\sigma_{a,i}),
\tag{2.6a}
\]

where \(\widehat f_{Z,m}\) is a predictive density **with respect to \(\log_{10}\) cycles**, \(\widehat S_{Z,m}\) is predictive survival at the documented censoring bound, and \(\ln\) denotes the natural logarithm. Lower NLL indicates better predictive likelihood for the recorded event or survival information. The original runout operator (\(>\) or \(\geq\)) was preserved in the provenance ledger; runouts were never recoded as failures at their stopping cycle.

The C0 predictive density and survivor used the pooled Weibull accelerated failure time model without publication effects. For C1, S0 and S1, a new unobserved publication offset \(b_{\mathrm{new}}\sim\mathcal N(0,0.25^2)\) was integrated over its *prior* distribution for every predictive density or survivor, following Section 2.4. A held-out publication offset was not estimated or updated from any of its failure or runout outcomes. Integration was performed on the density or survival probability before applying the logarithm. Recorded test censoring bounds were used for outcome scoring, not as new training evidence.

## 2.6.3 Publication macro, event-specific diagnostics and paired comparisons

For held-out publication \(s\) with \(n_s^{\mathrm{test}}\) original test observations, its mean NLL and the primary equal-publication macro NLL were

\[
\overline L_{s,m}
=\frac{1}{n_s^{\mathrm{test}}}\sum_{i\in D_{s,\mathrm{test}}}L_{i,m},
\qquad
L_{\mathrm{macro},m}
=\frac{1}{3}\sum_{s\in\mathcal P}\overline L_{s,m},
\quad \mathcal P=\{\mathrm{Wu,Chen,Matusu}\}.
\tag{2.6b}
\]

Each held-out publication contributed equally, irrespective of specimen count. The overall specimen-weighted mean over 192 test observations was also reported as a separate descriptive statistic because Matušů contributed 133 of the 192 records. The equal-publication macro, not the pooled specimen-weighted mean, was the predeclared primary statistic.

To identify compensating changes in predictive performance, failure-density scores and runout-survival scores were summarized separately within each publication. The failure macro averaged the publication-specific failure means over all three publications. The runout macro averaged the runout means over **Wu and Matušů only**, because Chen had no runouts in its selected test set. These event-specific scores were diagnostics of the same NLL, not independent fitting targets.

The primary experimental-only reference was C1. On paired original test observations and their unchanged event indicators and bounds, comparisons were expressed as

\[
\Delta_{i,m-C1}=L_{i,m}-L_{i,C1},
\qquad
\Delta_{\mathrm{macro},m-C1}
=L_{\mathrm{macro},m}-L_{\mathrm{macro},C1}.
\tag{2.6c}
\]

A negative difference represents an improvement in censored likelihood for the first named model, whereas a positive difference represents deterioration. S1 was additionally compared with S0 using the same test records. For S0 and S1, each fixed seed's held-out-publication and macro score was retained and reported, followed by the arithmetic mean and minimum–maximum over the five seeds. These seeds were repeated stochastic fits involving the same real test observations; they were not regarded as additional physical experiments or publication-level independent replicates. Mean absolute error of the predictive median in \(\log_{10}\)-cycle units was retained only as a secondary descriptive metric for actual failures, not for right-censored records.

## 2.6.4 Training stress support and the fixed augmentation decision rule

A whole-publication holdout may produce observations at stresses outside those available to the training publications. For each fold, the minimum and maximum stress amplitudes were determined solely from original real training records. Each test stress was flagged as within the training numerical support when

\[
\sigma_{a,\min}^{\mathrm{train}}
\leq \sigma_{a,i}^{\mathrm{test}}
\leq \sigma_{a,\max}^{\mathrm{train}}.
\tag{2.6d}
\]

Stress values below or above these limits were counted as out-of-support, and within-range and outside-range NLLs were reported separately. Numerical inclusion within the stress span was not assumed to establish physical-domain equivalence across process windows, heat treatments, specimen finishes, stress ratios or fatigue protocols. Stress-support diagnoses did not alter the primary macro, fitting rules or seed selection.

The precomparison protocol specified a conjunctive **preliminary-positive** criterion for selective augmentation. The five-seed mean S1 macro NLL had to be lower than **both** the C1 experimental-only macro and the S0 unrestricted synthetic macro; S1 also had to improve over C1 in at least two of the three held-out publication means; and neither its failure macro nor its runout macro could be higher than C1. If any element failed, the augmentation finding had to be reported as a trade-off or absence of consistent improvement, not a successful new algorithm based on one favorable seed, publication or event subtype. The primary analysis contained only three independent held-out publications, so the criterion was treated as an exploratory decision rule rather than a publication-level statistical superiority test.

## 2.6.5 Secondary ratio-transfer challenge and independent-source checks

The seven Romano et al. (2018) first exposures at \(R=-1\) (six failures, one runout) were evaluated as a **secondary ratio-transfer challenge**. The four arms were fitted on all 192 original \(R=0.1\) development records; synthetic training remained conditional on those same primary development publication groups. The seven Romano outcomes did not enter fitting, synthetic generation or model selection. Romano was already included in the 199-row frozen development inventory, so its challenge result was neither a fourth primary fold nor an untouched external validation study. The ratio shift was documented without fitting a stress-ratio coefficient absent from the primary stress-only model.

Two later, separately scored external sources reused the **archived all-192-record model fits** from the Romano-transfer fitting stage: one C0, one C1 and five fixed-seed fits each of S0 and S1. The model parameters and source-effect standard deviation were not refitted, calibrated or updated using either external source. For both sources, an outcome-masked file established the prediction membership and stress inputs. Full predictive parameters and medians were saved and committed **before** a strict specimen-identified outcome join and NLL calculation. This was a prediction-before-score procedure, not a fully outcome-unseen prospective trial: source outcome tables had already been inspected during literature intake.

**Beretta et al. (2022).** The source supplied 32 unique first-exposure cylindrical-specimen records from one experimental ESA campaign at \(R=0.1\): 25 failures and seven runouts censored at its documented \(5\times10^6\)-cycle stopping point. Eight later loading episodes on previously tested specimens were excluded. Original reported stress range \(\Delta\sigma\) was converted to nominal amplitude as \(\sigma_a=\Delta\sigma/2\) and cross-checked against the source ledger. The 32-record mean censored NLL was reported with separate 25-failure and seven-runout contributions; as-built and machined group comparisons were only descriptive strata within that one campaign. A reported failure at \(5.6\times10^6\) cycles beyond the stated source stop was retained without alteration in the main comparison, with a prespecified 31-record exclusion sensitivity using the same fixed models. All Beretta stress amplitudes were numerically inside the all-192 training stress span; finish and batch metadata were not fitted specimen predictors. Related ESA reanalyses were not counted as distinct experimental campaigns.

**Al-Zuhairi (2026 preprint).** The second source contained 23 specimen-identified 30 µm-process first-exposure **failures**, without documented runouts, at \(R=-1\). The included vertical as-built, vertical T6, horizontal T6 and 45° T6 conditions belonged to one preprint campaign, not four independent sources. Twelve 60 µm candidate records were excluded under the recorded overlap protocol; an unreported sixth vertical as-built record was not imputed. Failure-density NLL, median-life error and signed median prediction bias were descriptive metrics; no runout-survival score could be calculated. Stress amplitudes were numerically inside the all-192 training span, but the shift from \(R=0.1\) to \(R=-1\), orientation and treatment differences, and process conditions were not encoded as fitted effects.

These two external campaigns were reported separately from each other, from Romano and from the primary three-publication macro. S0/S1 external summaries retained all five original seed-level fits rather than choosing a favorable fit. The earlier Hamidi Nasab graph-based comparison used a different 66-record development fit of E0/M1 and was not an external check of the present S0/S1 protocol. Reserved Strauß–Löwisch and Kempf sources remained unscored. Differences from the fixed external checks were interpreted as descriptive transport observations, not an independent demonstration of synthetic augmentation superiority.

## 2.6.6 Auditability and limitations of validation

Reproducibility was supported by frozen cohort and fold tables, source-provenance ledgers, original Git blob identifiers, recorded exclusion and censoring rules, saved fit parameters, per-record held-out predictions, seed-specific metrics, synthetic-generation ledgers, and external forecast and score manifests. Input integrity, unique first-exposure IDs, true failure/runout coding, train–test publication separation, source-level stopping rules, stress basis, synthetic provenance and weights were checked. Bounded model fitting used 161-node Gaussian–Hermite integration with a separate 321-node numerical check. Absolute log-objective and prediction log-score differences were required to remain below \(10^{-5}\); convergence and exception checks were recorded without substituting new random seeds.

The primary evidence was limited by three independent publication groups, differences in runout frequency and incomplete specimen-linked prospective surface/defect metadata. The stress-only models did not identify causal effects of processing, heat treatment, orientation, stress ratio or pore characteristics. Synthetic episodes derived from the same fitted model family carried no independent material measurements and therefore tested a weighted self-distillation intervention, not a learned data-utility gate. The externally scored campaigns differed in loading domain, outcome mix and source-selection conditions and were not pooled to manufacture a larger publication count. These constraints set the interpretation boundary for the subsequent Results and Discussion.

---

## Evidence and editorial notes (not manuscript prose)

- **Frozen primary specification and code:** [Development v2 precomparison protocol](../docs/development_v2_precomparison_protocol_2026-10-06.md); [v2 comparison implementation](../scripts/compare_development_v2.py); [grouped fold assignments](../data/validation/development_v2_grouped_fold_assignments_2026-10-06.csv) and [fold feasibility](../data/validation/development_v2_grouped_fold_feasibility_2026-10-06.csv). The validation strategy, scoring definitions, group macro, stress-support flags, original five seeds, and three-part augmentation decision rule originate here.
- **Archived outputs and numeric checks:** [Development v2 results directory](../results/development_v2/), [run metadata](../results/development_v2/run_metadata.json) and [four-arm results audit](../docs/development_v2_four_arm_results_2026-10-06.md). The full development run contains 36 primary fits plus 12 Romano-transfer fits, all converged without fit problems; the reported 161/321-node differences met the prespecified tolerance. Primary macro scores belong in Results, not in Section 2.6.
- **Beretta fixed-model lock and results:** [External source role lock](../docs/beretta_2022_esa_overlap_and_external_role_lock_2026-10-08.md), [Beretta external results](../docs/beretta_2022_esa_external_censor_aware_results_2026-10-08.md), [scorer](../scripts/score_external_beretta_2022.py), and [forecast manifest](../results/external_beretta_2022_2026-10-08/forecast_manifest.json). Outcomes were seen at intake, while the 32 x 12 model forecasts were fixed before numerical outcome scoring.
- **Al-Zuhairi protocol and results:** [External 30 µm protocol](../docs/al_zuhairi_30um_external_outcome_only_protocol_2026-10-07.md), [Al-Zuhairi results](../docs/al_zuhairi_30um_external_outcome_only_results_2026-10-07.md), [scorer](../scripts/score_external_al_zuhairi_30um.py), and [forecast manifest](../results/external_al_zuhairi_30um_2026-10-07/forecast_manifest.json). The 23 x 12 forecasts were frozen before numerical scoring; this one preprint source contains no runouts.
- **Claim scope:** [Claim-evidence reconciliation](../docs/manuscript_claim_evidence_reconciliation_2026-10-08.md). Do not report the distinct primary, Romano, Beretta, Al-Zuhairi or older Hamidi Nasab scores as a single pooled NLL, or treat simulated seeds as experimental replication.
- **Editorial check:** The provisional equation tags (2.6a–d) should be renumbered with previous sections at journal typesetting. The arm index \(m\) is distinct from the stress-amplitude subscript \(a\). Align named-paper citations with the integrated introduction bibliography.
- **Next task:** Draft Results §3.1 from the frozen three-fold C0/C1/S0/S1 metrics, including publication-level and equal-publication macro scores, the distinct failure and runout macro diagnostics, seed-level variation, and the predeclared criterion's result. Treat Romano and both external sources in separately labelled later Results subsections; do not refit or rescore.
