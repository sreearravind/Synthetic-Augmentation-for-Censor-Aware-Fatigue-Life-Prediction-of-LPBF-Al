# Task 8 — journal-neutral manuscript integration and technical QA

**Integration date:** 9 October 2026. **Status:** complete journal-neutral assembly; target-journal and author metadata remain open. This is an editorial/reproducibility handoff and **not** a substitute for scientific peer review, journal acceptance, or a new experimental result.

## Deliverables

1. [Integrated Option A manuscript](Manuscript_Integrated_Option_A_2026-10-09.md): Option A title, original evidence-bounded abstract (187 words), keywords, Introduction §§1.1–1.5, Methods §§2.1–2.6, Results §§3.1–3.3, Discussion §§4.1–4.7, Conclusions §5, consolidated source bibliography, data/code availability and linked SVG figures. Approximately 14,900 whitespace-separated words, including mathematical expressions, embedded tables and references. No source section was rewritten to claim a positive S1 result.
2. [References](References_Option_A_2026-10-09.md): 16 source-grounded citations with DOIs or the identified preprint URL. Editorial metadata checks remain **explicit**, especially complete Matušů 2026 published-article author ordering, Al-Zuhairi preprint citation/version and journal-specific Tridello 2023a/b handling.
3. [Figure 1 — cohort/provenance SVG](Figures/Figure_1_Cohort_Provenance_Validation_Roles.svg): separates 199 development first exposures (192 primary, seven Romano) from two *additional*, separately scored external campaigns (Beretta 32; Al-Zuhairi 23).
4. [Figure 2 — primary NLL and event-type SVG](Figures/Figure_2_Primary_Publication_and_Event_Specific_NLL.svg): direct depiction of held-out Wu/Chen/Matušů mean scores and separate failure/runout publication macros; [traceable plotting-value CSV](Figures/Figure_2_Frozen_Data_2026-10-09.csv). The plotted values are derived from the frozen [per-fold results](../results/development_v2/fold_metrics.csv); the figure labels are rounded for visual legibility and the manuscript tables retain more precision.
5. The original [Task 7 audit](Manuscript_Consistency_and_Submission_Readiness_Audit_2026-10-09.md) remains a historical pre-integration record, including items that Task 8 has now addressed; this handoff supersedes its figure-availability and bibliography-assembly status.

## Integration actions and checks

| Check | Integration action | Result |
| --- | --- | --- |
| Scientific data | Read only the approved nine original source-section drafts and previously frozen numerical summaries; no new fitting, pseudoepisode generation, re-scoring or membership changes | Preserved |
| Research framing | Use Option A limits/negative-or-mixed-outcome title and abstract; S1 remains a fixed support filter, not a learned gate | Preserved |
| Full article structure | One file with sections 1–5, abstract, keywords, complete source-grounded bibliography, data/code availability | Assembled |
| Table numbering | Label the experimental source table **Table 1**; map Results Tables 3.1–3.8 onto paper-wide **Tables 2–9** in the integrated copy, including prose references | Nine sequential tables |
| Mathematical presentation | Convert the key Weibull distribution expressions in Methods §2.4 to Markdown-compatible LaTeX displays, retain original model parameters and conditional/marginal likelihood; leave Methods §2.5/2.6 historical equation tags as drafted | Improved; final typesetting should renumber equations consistently |
| Visuals | Add two accessible textual-captioned UTF-8 SVG figures, built from frozen source counts and existing scores; no invented experimental observations | Added |
| Editorial separation | Strip source-file evidence-ledger paragraphs and task recommendations from the assembled manuscript; retain them in original working files | Preserved repository audit trail |
| Source-relation honesty | Count Wu/Chen/Matušů as three primary holdouts, Romano as one internal ratio challenge, Beretta as one external campaign with seven runouts, Al-Zuhairi as one failure-only preprint | Preserved |
| Claim arithmetic | C0 1.27714; C1 1.27299; S0 1.27449; S1 1.27330 for equal-publication primary macro; event-specific contrast and all external source roles unchanged | Passed against source drafts and frozen report |
| Reproducibility | Keep earlier input hashes and protocols untouched; all manuscript files are separately committed to repository history | Traceable |

**Editorial caveat:** The bibliography is a *consolidated* 16-entry working list rather than a completed journal-specific citation export. One article's full coauthor sequence and the preprint identifier require final metadata confirmation; neither should be guessed. The two SVG sources have been saved and read back as text, but final target-journal vector/export checks and visual proofing should be carried out before submission.

## Items still requiring author/journal input

- **Author and corresponding-author details:** exact author sequence, affiliations, ORCIDs and contact author; do not infer these from GitHub username or earlier conversations.
- **Target journal:** journal name, author instructions, whether it uses author–year or numbered citations, word limits, equation and table formatting, figure dimensions and allowed artwork formats. “Q1” by itself does not specify these requirements.
- **Declarations:** real funding acknowledgements, conflicts of interest, individual author contributions, ethical/data permissions statements and source supplementary-file redistribution rights.
- **Bibliography:** verify exact full Matušů article author list, published preprint metadata/version, and Tridello suffixes under house style. Preserve original experimental source/protocol DOIs and do not invent bibliographic fields.
- **Final compression and production QA:** approximately 15k-word draft may require a shorter Discussion and supplementary migration depending on article type. Copyedit equation tags, check rendering of mathematical displays and both SVGs, check table captions and page breaks, and verify every citation in the finalized bibliography against the article.
- **Scientific caveat:** only three independent primary publication holdouts. No statistically established augmentation superiority, no learned synthetic gate, and no component-design qualification are supported. Reserved Strauß–Löwisch/Kempf scores remain untouched.

## Recommended next task

**Task 9 — journal targeting and submission-grade formatting.** Identify one primary journal and a realistic alternate compatible with transparent negative-results / reliability modelling, then adapt this assembled draft to one journal's precise template. Verify DOI metadata and preprint status, produce final figure proof sheets, streamline repetitive discussion passages if page constraints require, and request the author-only declarations. Avoid any change to the locked score comparisons purely to improve the presentation.
