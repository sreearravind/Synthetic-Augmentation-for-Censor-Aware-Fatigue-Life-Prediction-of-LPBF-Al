# Diagnosing the graph-assisted failure/runout trade-off

**Status: exploratory diagnosis, 2 October 2026.** This analysis reuses exact held-out studies already inspected in E0 and E1. It supports a modelling hypothesis; none of the variants below is an unbiased confirmatory result or a selected algorithm. No synthetic records were generated.

## 1. What changed in E1

The stress-only Weibull E1 fit added 26 independent graph-derived experimental observations (Zhang 20: 15 failures, five runouts; Glodež six: five failures, one runout) to each training fold. It retained all 66 exact test identities across the three source holdouts. Relative to E0, E1 worsened the log-density contribution for **all 57 exact failures** and improved survival at the lower bound for **all nine exact runouts**. The global Weibull shape decreased in every fold, consistent with a broader fitted life distribution at a fixed stress. This is a fitted-model description, not evidence of a single physical cause.

The sources occupy different domains:

| Study | Data tier | Fail/runout | Stress amplitude, MPa | \(R\) | Reported runout bounds |
| --- | --- | ---: | ---: | ---: | --- |
| Wu | exact | 33/8 | 22.5–90.0 | 0.1 | 10⁷ cycles |
| Romano | exact | 6/1 | 90.0–200.0 | −1 | ≥8,889,311 cycles |
| Chen smooth | exact | 18/0 | 67.5–99.0 | 0.1 | none |
| Zhang | graph | 15/5 | 54.1–99.2 | 0 | conservative 10⁸ cycles |
| Glodež | graph life, exact stress | 5/1 | 57.0–79.8 | 0 | 4×10⁶ cycles |

The graph study with 20 rows can exceed the **25 exact training rows** in the Wu holdout. The graph-only \(R=0\) protocols also differ in manufacture, finishing, geometry and frequency. Their role cannot be isolated by a single pooled stress coefficient.

## 2. Source and event ablation

Each row uses the **same E0 Weibull fit function**, frozen exact test rows and mean right-censored NLL (lower is better). The two event-selected ablations deliberately remove one kind of graph outcome and are **mechanism probes only**; they must never be presented as defensible candidate training sets.

| Training addition to the exact sources | Graph rows added | Wu NLL | Romano NLL | Chen NLL |
| --- | ---: | ---: | ---: | ---: |
| None (E0 control) | 0 | 1.345 | 2.640 | 1.058 |
| Zhang alone | 20 | 2.325 | 1.652 | 1.447 |
| Glodež alone | 6 | 1.354 | 2.773 | 1.032 |
| Both graph sources, failures only | 20 | 1.613 | 1.833 | 1.166 |
| Both graph sources, runouts only | 6 | 2.289 | 1.652 | 1.514 |
| Both graph sources (E1) | 26 | 2.149 | 1.648 | 1.417 |

Zhang alone reproduces most of E1's direction, while Glodež alone has much smaller effects, with a slight Chen gain. Graph runouts alone cause a large shift: in Wu they worsen the summed exact-failure NLL by **50.94** units but improve summed exact-runout NLL by **12.20**; graph failures alone worsen exact-failure NLL by **19.09** and improve runout NLL by **8.09**. These are changes in a small, selected experiment, and the ablations alter the stress and life distributions together. The result supports investigating source heterogeneity and censoring pressure; it does not identify a causal effect of runout status.

## 3. How source should enter the next model

**Target:** predict an unseen original experimental study, keeping all of its specimens out of fitting, preprocessing, graph digitization calibration and synthetic generation. Source identity is a training grouping variable, not a deployable one-hot predictor for an unseen study.

**Candidate model for a later, independently tested analysis:** let \(Z_i=\log_{10}N_i\) have a Weibull AFT distribution with

\[
\mu_{is}=\alpha+\beta_\sigma\log_2(\sigma_{a,i}/100\,\mathrm{MPa})+b_s,
\qquad \beta_\sigma\leq0,\qquad b_s\sim\mathcal N(0,\tau_b^2).
\]

Use the failure density for events and survival beyond the paper-supported bound for runouts. Fit the study offsets \(b_s\) with partial pooling on **training studies only**. For a new study, integrate over a new offset \(b_{\mathrm{new}}\) rather than borrowing the held-out study's fitted offset. This is a standard way to represent clustered survival heterogeneity, not a novel algorithm by itself ([Crowther et al., 2014](https://doi.org/10.1002/sim.6191)); right-censored log-likelihood supplies the probabilistic evaluation basis ([Rindt et al., 2022](https://proceedings.mlr.press/v151/rindt22a.html)).

With only two exact training studies in an E0 fold, \(\tau_b\) and separate source effects are weakly identified. A fixed small range of shrinkage assumptions must be stated before a **new** external test; parameter sensitivity should be reported. A fixed study-intercept lookup for held-out specimens is invalid. Model extra study-specific slopes or shape parameters only after more independent studies are available.

**Stress ratio:** \(R=-1\) appears only in Romano, \(R=0\) only in the graph studies, and \(R=0.1\) in Wu and Chen. A stress-ratio coefficient is confounded with study and treatment. Record \(R\) and disclose the out-of-domain tests, but do not infer a transferable \(R\) effect from these five sources. Additional independent experiments with overlapping \(R\) conditions are needed before treating it as an identifiable material relation.

## 4. How graph-reading precision should enter

| Evidence tier | Available precision | Next-model treatment |
| --- | --- | --- |
| Exact source-table failures/runouts | Printed stress and observed life or censor bound | Standard density/survival contribution; retain source group and stress basis. |
| Glodež graph failure | Printed stress amplitude; life read from Fig. 10 | Exact stress; retain log-life reading interval and test the result at lower/center/upper readings. |
| Zhang graph failure | Stress and life read from Fig. 4 | Retain both stress and life reading intervals; evaluate bounded perturbations without pretending they are additional specimens. |
| Graph runout | Stress may be graph-read; survival threshold specified by paper | Keep the reported censor bound fixed; perturb only graph-read stress. Never substitute the arrowhead coordinate or a failure time. |

The current reading bounds quantify plausible **digitization**, not physical specimen scatter or a calibrated probability distribution. Zhang's median recorded failure-life interval is about **0.063 log10 cycles**, and median amplitude interval width is about **2.95 MPa**; Glodež's corresponding life interval is about **0.082 log10 cycles**, with exact printed stress. E1's nine coordinated reading scenarios did not reverse its source-level score directions, but they do not measure uncertainty in the outcome glyph, source bias or a new-study effect.

For a likelihood that *integrates* graph-reading uncertainty, first have independent readers re-digitize each selected glyph and use their differences to calibrate a measurement kernel for plotted stress and life. A graph failure would then marginalize its event density over the calibrated reading process; a graph runout would marginalize survival at its **fixed censor bound** over stress reading uncertainty. Do not convert the present hand-set bounds into an assumed uniform error density without that calibration. Until then, retain exact-only inference as the primary reference and graph results as separate sensitivity evidence. Downweighting graph rows by an arbitrary quality factor is a diagnostic choice, not a validated precision model.

## 5. Confirmation and synthetic-data gate

The Wu, Romano and Chen holdouts have been repeatedly inspected during E0, E1 and these ablations. **A model architecture or graph weight chosen in response to these scores cannot claim fresh, unbiased validation on those same holdouts.** Freeze the subsequent design and obtain at least one genuinely unused independent experimental study for a confirmatory test; ideally collect several, including explicit runouts and overlapping stress-ratio conditions. If that is not feasible, label later tests as exploratory and keep claims narrow. The graph studies have already entered training and their labels informed this diagnosis, so they cannot be silently repurposed as untouched confirmation.

Only after the model and external-test rule are fixed should synthetic generation be specified. Every generator, imputation step and source offset fit must use training studies alone; synthetic observations cannot be scored as experimental tests. A generator must preserve the distinction between failures and survival lower bounds, stress-ratio/source domains, and exact versus digitized evidence tiers.

**Decision from this task:** investigate a simple partially pooled censor-aware model, preserve graph precision as a separate observation process/sensitivity tier, and seek new unused experiments before making a novelty or superiority claim. This is a design specification arising from diagnostics, not yet the manuscript's novelty statement.

### Reproducibility files

`ablation_fold_metrics_18.csv` and `ablation_parameters_18.csv` contain six diagnostic variants × three frozen exact holdouts. `source_summary_5.csv` documents source domains. `run_metadata_diagnostic.json` records hashes and software versions. The script reuses the E0 Weibull fitter and the E1 graph mapping and verifies the zero-graph control against E0.
