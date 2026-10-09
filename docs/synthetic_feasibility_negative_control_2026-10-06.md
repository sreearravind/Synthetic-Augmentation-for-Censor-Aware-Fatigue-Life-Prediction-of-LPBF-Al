# Censor-aware synthetic feasibility: a train-only negative control

**Status:** exploratory computational probe, 6 October 2026. This is **not** the proposed manuscript algorithm and does not establish a synthetic augmentation benefit. It follows the previously inspected exact folds; no prospective external campaign was scored.

## Generator and boundaries

For each exact leave-study-out fold, the base fit is the M1 source-marginal Weibull AFT model trained on the exact training studies plus the 53 new graph-derived **failures**, with both new graph sources capped at five effective likelihood contributions. Study-effect SD remains fixed at τ=0.25. The generator itself uses only **original exact Wu training rows**, when Wu is in the training fold. It samples one Wu source offset from its posterior conditional on those original training outcomes, resamples an observed Wu stress level, samples a Weibull latent log10 life, and records a failure at that life or a right-censored runout at **10⁷ cycles**. Wu's eight original runouts have that bound. The same sampled source offset is used for all 20 synthetic episodes in one replicate; synthetic observations remain grouped with Wu during fitting. Each synthetic episode is explicitly flagged in a separate ledger.

There are five fixed seeds and two synthetic total weight caps, 2 or 5 per 20-row replicate. Exact rows retain unit likelihood weight, graph rows retain the previous cap, and a synthetic row receives cap/20. The augmented model is refitted and scored **only** on the same untouched exact test rows as its paired graph-assisted base fit. The generator and its posterior use training outcomes only; no held-out stress/outcome enters generation. Five random draws are sensitivity replicates, **not five independent experimental cohorts**. All synthetic outcomes use the model that is subsequently refitted, so this is a self-distillation control rather than a source of new physical information.

The Romano 8,889,311-cycle runout bound is documented for **one first-exposure specimen**. It was not applied as a cohort-wide stop for synthetic episodes. Chen has no documented runout in the frozen exact cohort. Consequently, the Wu holdout has no eligible source for this generator and **zero synthetic training rows**; its zero difference is a design result, not evidence of model equivalence on Wu.

## Paired held-out NLL changes across five seeds

Changes are *synthetic model minus graph-assisted base* mean right-censored NLL on log10 life. Negative is better. Each fold's base fit is fixed; seeds generate distinct training-only pseudo-episodes.

| Held-out exact study | Base NLL | Cap 2: mean [min, max] Δ | Cap 5: mean [min, max] Δ | Synthetic rows per fit |
| --- | ---: | ---: | ---: | ---: |
| Wu 2021 (33 failures, 8 runouts) | 1.3041 | 0.0000 [0, 0] | 0.0000 [0, 0] | 0 |
| Romano 2018 (6 failures, 1 runout) | 2.0536 | −0.0010 [−0.0111, +0.0052] | −0.0018 [−0.0250, +0.0133] | 20 Wu-derived |
| Chen 2024 (18 failures, 0 runouts) | 1.0223 | +0.0004 [−0.0028, +0.0053] | +0.0006 [−0.0067, +0.0117] | 20 Wu-derived |

The five Wu-derived replicates had 15–18 simulated failures and 2–5 runouts in the Chen-held-out fits, and 16–18 failures and 2–4 runouts in the Romano-held-out fits. Each synthetic row in a replicate has one of the original Wu stress levels and its source's stop; the generated records are **never** counted as additional experimental specimens. The score differences are small, of both signs, and seed-dependent. The Wu fold, which contains most of the exact runouts and showed the strongest prior failure/runout trade-off, cannot test the synthetic mechanism with this generator because Wu must remain wholly held out.

## Numerical and scientific decision

All 20 nonempty augmented fits converged, stayed inside the slope/shape bounds, and passed 161-versus-321-node quadrature objective and predictive log-score checks at 10⁻⁵. The other 10 fold×seed×cap cells correctly had zero synthetic rows and identical scores. Hashes of the frozen exact data, split manifest, 53 graph rows and base results are recorded in `run_metadata.json`. The ledger has 200 **training-only synthetic** episodes from 10 fold×seed draws; it is separate from the original-data master.

**Decision:** do not claim a novel algorithm or improvement from model-generated pseudo-replication. The legitimate next design constraint is a source-supported censor mechanism and a method that adds information absent from the stress-only M1 self-model, such as externally justified physics or independently measured process/defect variables. Obtain more original failure/runout experiments with explicit stopping cycles and overlapping processing domains before specifying that method. Keep the Strauß–Löwisch and Kempf tests unscored until the generator, comparators, metrics and inclusion rules have a credible prospective lock. This negative control belongs in method development, not a manuscript efficacy figure.

Reproduce with `scripts/prototype_censor_aware_synthetic_feasibility.py`. Output files: `synthetic_feasibility_scores_30.csv`, `synthetic_training_episodes_200.csv`, `paired_exact_predictions_660.csv`, and `run_metadata.json`.
