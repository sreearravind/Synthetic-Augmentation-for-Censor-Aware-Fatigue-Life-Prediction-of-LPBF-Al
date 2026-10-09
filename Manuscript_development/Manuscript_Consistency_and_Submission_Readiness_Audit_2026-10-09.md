# Manuscript consistency and submission-readiness audit

**Audit date:** 9 October 2026  
**Working title:** *Testing the limits of synthetic augmentation for censor-aware fatigue-life prediction in laser powder bed fused AlSi10Mg* (Option A).  
**Scope:** source-grounded editorial and scientific consistency review of the integrated Introduction (1.1–1.5), Methods (2.1–2.6), Results (3.1–3.3), Discussion (4.1–4.7), new Conclusions (§5), and the working Option A title/abstract. No model was refitted, source re-scored, reference invented, or existing locked protocol changed. The manuscript's **scientific prose is drafted**, but it is **not yet a submission-formatted, journal-checked article**. Journal quartile or acceptance cannot be inferred from prose quality.

## 1. Source and claim integrity — audit results

| Check | Verified source-grounded position | Assessment |
| --- | --- | --- |
| Experimental inventory | 199 unique, auditable **first-exposure** records from four underlying publication groups; 172 failures and 27 right-censored runouts | Consistent across Introduction, Methods and Conclusions |
| Primary evaluation | 192 original \(R=0.1\) observations: Wu 41 (33 failures, eight runouts), Chen 18 (18/0), Matušů 133 (115/18); **three** whole-publication holdouts | Consistent. Matušů platforms and series cannot be counted as separate publication holdouts |
| Separate ratio transfer | Seven Romano \(R=-1\) initial exposures (six failures, one runout), **inside** the frozen 199-record inventory, not a fourth primary fold | Consistent in Results §3.2 and Discussion; keep secondary/development designation |
| Further external source checks | Beretta 2022: **32** \(R=0.1\) first exposures, **25 failures/seven runouts at \(5\times10^6\)**. Al-Zuhairi 2026 preprint: **23** \(R=-1\) first-exposure **failures, no documented runouts** | Consistent in §3.3, Discussion and Conclusions. Do **not** pool with primary macro or Romano |
| Original model inputs | Stress amplitude is the **only fitted specimen-level covariate**. C1/S0/S1 marginalize a new-publication offset, fixed \(\tau=0.25\). No independent specimen-specific pore/roughness predictor or fitted stress-ratio coefficient | Consistent in Methods/Discussion. Audit labels and stratified diagnostics are not fitted features |
| Synthetic-arm identity | S0/S1 use same-teacher, training-only parametric pseudo-episodes; each source has total effective pseudo-likelihood weight **two**; S1 is a **prespecified training-source runout-support filter**, not a learned gate | Consistent. No new algorithmic superiority or independent physical dataset should be claimed |
| Primary model result | Equal-publication macro censored NLL: C0 **1.27714**, C1 **1.27299**, S0 **1.27449**, S1 **1.27330**. S0/S1 are **five-seed means** (13, 29, 47, 71, 101) | Consistent with archived [four-arm results](../docs/development_v2_four_arm_results_2026-10-06.md) |
| Fixed primary criterion | S1–C1 macro \(+0.00031\), only **one of three** folds improved, and both failure and runout macro NLL worsened; criterion **failed** | Correct in Results, Discussion, Conclusions and Option A abstract. S1 cannot be represented as a validated gain |
| Event-specific comparison | C0 failure/runout macros: **1.19403 / 2.23383**; C1 **1.22944 / 1.91623**; S0 **1.23261 / 1.90529**; S1 **1.22971 / 1.91716** | Preserve as **separate diagnostic means**; runout macro includes Wu/Matušů, not Chen |
| External NLL | Beretta C0/C1/S0/S1: **1.55455 / 1.48670 / 1.48490 / 1.48624**. Al-Zuhairi: **1.7300 / 1.6155 / 1.6038 / 1.6131** | Report as **separate single-campaign source means**, not two additional primary-fold replicates |
| External evaluation design | Outcomes were visible during source intake; model forecasts and score rules were fixed before keyed numerical outcome scoring | Accurately described as **post-intake, fixed-model prediction-before-score**, not prospective blinded validation |
| Novelty/causality | Supported: provenance-sensitive, censor-aware, grouped evaluation and limitations of fixed source-preserving augmentation. Unsupported: learned utility gate, statistically established augmentation superiority, prospective feature model, physical causality of source offset | Consistent and appropriately cautious |
| Future sources | Strauß–Löwisch and Kempf sources remain reserved/unscored, subject to extraction and overlap controls | Must remain reserved; no claims of results from those candidates |

**Scientific decision:** The article is a **limits/negative-and-mixed-results study** with a transparent data and validation methodology. Its novelty proposition should be the rigor of the source-audited, censor-aware study-level comparison and the informative failure-versus-survival trade-off, not an unimplemented algorithm. Additional observational campaigns alone cannot be used to imply statistically independent evidence for a learned synthetic gate.

## 2. Abstract and title reconciliation

**Current recommended title:** *Testing the limits of synthetic augmentation for censor-aware fatigue-life prediction in laser powder bed fused AlSi10Mg*. This matches the manuscript's implemented intervention and failure of the predefined S1 benefit rule. The alternative [Option B](../docs/manuscript_title_abstract_options_2026-10-08.md) title/abstract describes a **future hypothesis**; it is **not** a completed methods/results description and should not enter this submission.

The Option A abstract currently resides in [the title/abstract options document](../docs/manuscript_title_abstract_options_2026-10-08.md), **not** as the first section of an assembled full manuscript. It is approximately **187 words** and correctly reports 199 original observations, 192 primary \(R=0.1\) records (166 failures/26 runouts), three held-out publications, the four-arm design, and the C1/S0/S1 primary macro NLL values. It also correctly distinguishes the separately scored Beretta and Al-Zuhairi checks from confirmation of an augmentation advantage.

**Required at compilation:** Copy only the Option A title and final abstract into the assembled manuscript; ensure the explicit subject is the limits of **same-teacher stress-only augmentation**, not synthetic improvement in general. Add target-journal-compliant keywords (suggested topics, not locked keyword metadata: LPBF AlSi10Mg; fatigue life; right censoring; synthetic data augmentation; leave-publication-out validation; source heterogeneity). Check the journal's abstract word/structure limit and decide whether to mention the pooled C0 baseline explicitly. Do not invent an improvement percentage or p-value. Option A abstract can be edited for house style without changing its result statements.

## 3. References and source crosswalk

The integrated Introduction includes an **internal DOI reference ledger**, and the Discussion uses author–year references aligned to that ledger. This is **not a final numbered or fully formatted References section**. No manuscript-ready bibliography file was identified in the Manuscript_development directory at this audit. Preserve and consolidate the following *source-verified by repository-ledger* reference targets, then verify complete author lists, exact year, title, journal/preprint venue, volume, pages/article number and DOI against the chosen target journal's standards:

| Reference role | Manuscript cite / ledger | DOI or outstanding bibliographic work |
| --- | --- | --- |
| Defect/orientation primary and context | Wu et al. (2021) | [10.1016/j.ijfatigue.2021.106317](https://doi.org/10.1016/j.ijfatigue.2021.106317) |
| Roughness and subsurface porosity context | van der Rest et al. (2025) | [10.1016/j.msea.2025.148885](https://doi.org/10.1016/j.msea.2025.148885) |
| Process-setting modelling context | Ciampaglia et al. (2023) | [10.1016/j.ijfatigue.2023.107500](https://doi.org/10.1016/j.ijfatigue.2023.107500) |
| Process-to-defect ML context | Tridello et al. (2023b) | [10.3390/app13074294](https://doi.org/10.3390/app13074294) |
| VHCF interpolation precedent | Shi et al. (2023) | [10.1016/j.ijfatigue.2023.107585](https://doi.org/10.1016/j.ijfatigue.2023.107585) |
| Cross-material SMOTE precedent | Srinivasan et al. (2024) | [10.1016/j.matdes.2024.113355](https://doi.org/10.1016/j.matdes.2024.113355) |
| Physics-informed multi-fidelity context | Wang et al. (2025) | [10.1016/j.cma.2025.117924](https://doi.org/10.1016/j.cma.2025.117924) |
| Source-level negative augmentation precedent (steel welds) | Mülkoğlu et al. (2026) | [10.1007/s10845-026-02975-4](https://doi.org/10.1007/s10845-026-02975-4) |
| Censored fatigue likelihood/statistical scatter | Tridello et al. (2023a) | [10.1038/s41598-023-40249-8](https://doi.org/10.1038/s41598-023-40249-8) |
| Grouping/fatigue dataset methodological precedent | Di Maggio et al. (2025) | [10.1007/s00366-025-02139-7](https://doi.org/10.1007/s00366-025-02139-7) |
| Primary failure-only source | Chen et al. (2024) | [10.1016/j.ijfatigue.2024.108163](https://doi.org/10.1016/j.ijfatigue.2024.108163) |
| Primary workbook source | Matušů et al. (2026) | [10.1016/j.rineng.2026.112570](https://doi.org/10.1016/j.rineng.2026.112570) |
| Secondary original campaign | Romano et al. (2018) | [10.1016/j.engfracmech.2017.11.002](https://doi.org/10.1016/j.engfracmech.2017.11.002) — check final displayed publication year on publisher metadata |
| Numeric re-report of same Romano specimens | Tognan et al. (2023) | [10.1016/j.cma.2023.116521](https://doi.org/10.1016/j.cma.2023.116521) |
| External ESA original campaign | Beretta et al. (2022) | [10.1016/j.matdes.2022.110713](https://doi.org/10.1016/j.matdes.2022.110713) — related Sausto/Rusnati studies are **not** independent campaigns |
| External failure-only preprint | Al-Zuhairi (2026) | **Full preprint title, author list, persistent URL/version and bibliographic metadata still require final verification**. Do not fabricate a DOI |

**Bibliographic editorial requirements:** Establish a single citation style (author–year or numbered), reconcile the *Tridello 2023a/2023b* suffixes against final reference order, consistently retain “van der Rest” and the diacritic in “Matušů,” and cross-check every in-text citation against an actual References entry. Distinguish references that **supply original specimen observations** from those used for general mechanistic/methodological context. Titles/DOIs in the existing ledger are documented project references; the above is not a claim that all metadata were independently rechecked live during this editorial task.

## 4. Tables, figures and equation formatting

### Tables

The Results drafts use **eight sequential, numbered tables: 3.1–3.3 (primary), 3.4–3.5 (Romano), and 3.6–3.8 (Beretta/Al-Zuhairi)**. Their reported values match the locked study summaries and event counts. Table 3.3 and Table 3.8 explicitly display all synthetic seeds, including unfavorable ones; they must not be shortened in a way that hides those replicates. **Methods §2.1 contains an important dataset/provenance table that is currently not formally numbered or captioned**. Add a proper “Table 2.1” caption at manuscript assembly, reference it in §§2.1–2.3, and ensure no later renumbering collision. If the target journal requires sequential paper-wide table numbers, rename *all* captions and in-text references consistently at final typesetting; the present “3.x” convention is subsection-specific working numbering.

The primary macro weights three publications equally, whereas the secondary pooled 192-record mean is specimen-weighted. Failure macros include Wu, Chen and Matušů; runout macros include **Wu and Matušů only**. Each table caption should preserve this distinction and should mark S0/S1 values as **five-seed means**. Beretta as-built/machined subsets and Al-Zuhairi treatment subgroups must remain within their one respective source.

### Figures

**No figure file was found in the Manuscript_development folder in the repository tree at the time of this audit.** The manuscript prose contains no finalized numbered figure references. Therefore figure composition, resolution, publication permissions and caption–image matching have **not** been verified. For a stronger engineering-journal submission, build figures from the archived immutable CSV ledgers (not fabricated simulations):

1. **Figure 1 (proposed):** provenance and evaluation-role flow—199 frozen first exposures, three primary groups/192 \(R=0.1\), separate seven Romano \(R=-1\), and **two separately counted external campaigns** Beretta 32 and Al-Zuhairi 23. Clearly distinguish development records from external cohorts; a displayed total should not imply that all were independently pooled for model training.
2. **Figure 2 (proposed):** publication-level C0/C1/S0/S1 censored NLL for the three held-out primary sources and a separate failure versus runout macro panel. Use five-seed means and appropriate axis labels; never imply five independently held-out publications.
3. **Supplementary figure (optional):** seed-by-seed S0/S1 contrasts against C1 for primary and external sources, with each source kept separate. Avoid an arbitrary pooled cross-source metric and avoid uncertainty bars that treat seeds as independent fatigue campaigns.

This task **does not create** the figures or claim submission-ready imagery. Confirm whether the target journal prefers color-blind-accessible vector artwork, minimum-resolution raster exports, panel labels and source citations before producing them.

### Equations and nomenclature

Methods §2.4 presently describes the Weibull survivor, density, source integration and prediction largely in unnumbered inline/plain-text mathematical expressions; Methods §2.5 has working equation tags **(2.5a–e)** and §2.6 has **(2.6a–d)** in LaTeX-style Markdown. Before journal assembly, convert §2.4 formulas into consistent typeset mathematics, align all equation numbering/cross-references and use a notation table if space permits. Explicitly distinguish \(\log_{10}(N)\), \(\log_2(\sigma_a/100\ \mathrm{MPa})\) and natural-log NLL; avoid writing fatigue runouts as observed failure life. Clarify \(N_{\mathrm{stop}}\) as a source-supported censor lower bound and \(\tau=0.25\) as a fixed model assumption rather than a separately experimentally estimated variance.

The draft currently mixes textual \(R=0.1\), \(R = 0.1\), \(R=-1\), spelled out “stress ratio,” and differing forms of “negative log likelihood.” Standardize journal style without changing source ratio values, stress-amplitude basis or censor operators. Within Methods §2.4, move the concluding **Implementation record** line into the editorial/reproducibility ledger or a formal Data and Code Availability passage. Source-derived sample counts and ratios should retain the original exact meaning.

## 5. Manuscript architecture and reproducibility

- **Existing distinct prose sections:** Integrated Introduction §§1.1–1.5; Methods §§2.1–2.6, presently spread over four files; Results §§3.1–3.3, presently in three files; Discussion §§4.1–4.7; and newly completed Conclusions §5.
- **Not yet assembled:** a single clean article carrying the final Option A title/abstract, author affiliations, keywords, figures, consolidated tables, full numbered/author–year references and journal-specific front/back matter.
- **Editorial metadata:** Nearly every section file includes audit notes, working-draft dates, source links, task recommendations and implementation checklists. These are **excellent provenance records but not submission prose**. Remove them from the compiled manuscript; retain them in the repository/supplement. Preserve scientific explanations but eliminate repeated method statements across Sections 2.4, 2.6, 3.1, 3.3 and 4 where a compact cross-reference suffices.
- **Reproducibility:** The frozen [cohort](../data/cohorts/development_v2_199_2026-10-06.csv), [fold ledger](../data/validation/development_v2_grouped_fold_assignments_2026-10-06.csv), [protocol](../docs/development_v2_precomparison_protocol_2026-10-06.md), [four-arm outputs](../results/development_v2/fold_metrics.csv), and [external source summaries](../results/external_beretta_2022_2026-10-08/summary.csv) / [Al-Zuhairi summary](../results/external_al_zuhairi_30um_2026-10-07/summary.csv) support numerical traceability. Verify paths, commit state, licensing/reuse limits and reproducible environment at archive/release time.
- **Submission requirements pending journal selection:** Data and Code Availability, funding, author contributions, conflicts/declarations, ethics statement where applicable, supplemental provenance tables/ledgers, publication-quality figures, exact source permissions, journal reference style, abstract format and word limits. Do not manufacture these declarations; request missing author/journal details as needed.

## 6. Priority-ordered next actions

| Priority | Action | Why it matters | Can proceed without new experiment? |
| --- | --- | --- | --- |
| **P0** | Keep Option A **limits/negative-results** framing; preserve the fixed primary S1 failure and external roles | Integrity and defensible novelty | Yes |
| **P1** | Assemble all prose in one manuscript, transfer the 187-word Option A abstract, and remove editorial-only text | Readable submission architecture | Yes |
| **P1** | Produce a complete, cross-checked, journal-formatted reference list; verify Al-Zuhairi preprint metadata | Research traceability and accurate citations | Partly: source metadata checks required |
| **P1** | Number the Methods source table, harmonize §2.4 equations with §§2.5–2.6, standardize nomenclature | Technical typesetting consistency | Yes |
| **P1** | Prepare at least one publication-ready primary-results figure (plus a source-flow graphic if space permits) | Efficient communication of the study design and key trade-off | Yes, from archived outputs |
| **P2** | Confirm journal fit and author/affiliation/submission declarations; trim Discussion to journal limits | Editorial compliance | Requires target journal and author confirmation |
| **P2** | Run final QA for table–citation–figure cross-references, exact DOI metadata, reproducible release, and source reuse | Submission integrity | Yes after assembly |
| **Future research, not a manuscript repair** | Seek independently measured, specimen-matched pretest HCF predictors and reserve truly unscored sources for a later feature-guided method | Needed to justify a different **positive algorithm** claim | No; new evidence required |

**Final audit judgment:** The available Results support a coherent, cautious Option A article and a credible negative/mixed experimental finding. **Task 7 completes the final scientific prose section, not final submission formatting.** A top-quartile journal may value the rigorous out-of-source, censor-aware evaluation, but this audit does **not** establish Q1 readiness, novelty threshold, suitability to a particular journal or prospective confirmation of a superior algorithm. The next efficient task is a *single clean manuscript assembly and reference/figure integration pass* performed against the frozen evidence; do not revise the underlying experimental comparison simply to improve headline scores.
