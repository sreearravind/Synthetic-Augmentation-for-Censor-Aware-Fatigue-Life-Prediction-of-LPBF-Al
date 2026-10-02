# Exact-only probabilistic baseline for LPBF AlSi10Mg fatigue life

**Run date:** 2 October 2026. This is the prespecified **E0** exact-only, leave-one-study-out baseline. It uses the 66 confirmed smooth-specimen first exposures (57 failures, nine right-censored observations), the frozen study membership, and no graph-digitized, synthetic, notched, ambiguous or dependent-retest records.

## Model and objective

At a given pretest stress amplitude \(\sigma_a\), cycles to failure \(N\) follow a Weibull distribution with shape \(k>0\) and scale \(\lambda\). The one-feature accelerated failure-time relation is

\[
\log_{10}\lambda=\alpha+\beta\log_2(\sigma_a/100\,{\rm MPa}),\qquad\beta\leq0.
\]

Each training fold estimates \(\alpha,\beta,k\) by maximum observed-data likelihood. A failure contributes its probability density in \(z=\log_{10}N\); a runout contributes the survival probability beyond its documented lower bound. The fixed parameter search bounds are \(\alpha\in[0,12]\), \(\beta\in[-12,0]\), and \(\log k\in[-4,3]\). Three deterministic starting points help detect local optimizer failure; none of the selected fits sits on a constraint boundary. This baseline deliberately does **not** use \(R\), orientation, surface, thermal condition, or source identity as a predictor. Consequently, its predictions across stress ratios or source conditions are diagnostics of transfer, not evidence that these factors are irrelevant.

## Held-out results

Lower censored negative log-likelihood (NLL) is better. NLL uses the **log10-cycle density** for failures and survival at the recorded censor bound for runouts. Failure-only MAE is descriptive because it omits runouts.

| Held-out study | Test records (fail/runout) | Mean censored NLL | Failure-only MAE, log10 cycles | Test stresses outside training range | Unseen \(R\) |
| --- | ---: | ---: | ---: | ---: | ---: |
| Wu 2021 | 41 (33/8) | 1.345 | 0.586 | 32/41 | 0/41 |
| Romano 2018 | 7 (6/1) | 2.640 | 0.356 | 6/7 | 7/7 |
| Chen 2024 smooth | 18 (18/0) | 1.058 | 0.287 | 0/18 | 0/18 |

The Romano runout alone contributes 13.020 NLL units, corresponding to predicted survival at its bound of about \(2.2\times10^{-6}\). It is a conspicuous failure of this stress-only baseline on that specimen; six Romano stresses also exceed the training range, and the entire Romano test fold has \(R=-1\) while its training studies have \(R=0.1\). Wu's training set has only one runout, and 32 Wu stresses lie outside its training range. Chen's test fold contains no runouts, so it provides no direct test of censor survival. These three study scores should be read separately rather than combined into a generalization claim.

| Held-out study | Training records (fail/runout) | \(\alpha\) | \(\beta\), log10 scale per stress doubling | Weibull shape \(k\) |
| --- | ---: | ---: | ---: | ---: |
| Wu 2021 | 25 (24/1) | 5.449 | −0.960 | 0.541 |
| Romano 2018 | 59 (51/8) | 5.234 | −1.011 | 0.601 |
| Chen 2024 smooth | 48 (39/9) | 5.444 | −0.848 | 0.461 |

## Reproducibility and limits

- `fit_parameters_E0_3.csv` stores the fitted coefficients and optimizer diagnostics; `fold_metrics_E0_3.csv` stores unrounded scores, outcome counts and extrapolation counts; `heldout_predictions_E0_66.csv` stores each untouched test specimen's prediction and loss components.
- `run_metadata_E0.json` records exact input hashes, the fixed model equation, parameter bounds and software versions. The script checks the smooth cohort against the frozen split-input hash and checks that E0 held-out studies are disjoint.
- The log-cycle density and censor survival implementation was independently checked against SciPy's Weibull density/survival calculations and numerical derivatives of the objective. All three held-out scores were finite; this checks the computation, not the model's external validity.
- The fitted Weibull shapes are all below one. This stress-only model may be absorbing heterogeneous production and testing conditions into its tail; the shape estimates should not be interpreted as material constants.
- No confidence interval, hypothesis test or claim of superior performance is justified by these three exact study groups. The proposed algorithm, graph-assisted training and synthetic augmentation remain untested in this report.

**Next comparison:** run the already frozen **E1** fits with graph-tier rows added to training only, while leaving these exact held-out test IDs and this scoring convention unchanged. Before interpreting E1, audit the mixed-source stress representation and graph reading bounds.
