# MMTA topical-collection manuscript — 27 October 2026

**Journal:** *Metallurgical and Materials Transactions A* (MMTA), Springer/ASM/TMS  
**Collection:** *Microstructural Evolution, Degradation Mechanisms, and Failure Analysis in Structural Metals and Alloys*  
**Advertised deadline:** 31 October 2026 (verify submission availability at the portal).  
**Article role:** Topical Collection Article, **original research**; not a review or claim of a new specimen-level defect model.  
**Editorial status:** author-review draft, NOT ready for submission without completing the blockers below.

## What was revised

- [main_MMTA_2026-10-27.tex](main_MMTA_2026-10-27.tex) is derived from the successfully compiling JMEP LaTeX manuscript. The earlier JMEP file has not been modified.
- Materials-reliability title and 158-word abstract; no new specimen records or altered scores.
- New evidence-bounded paragraphs tying manufacturing-source context, surface/defect variation and fatigue assessment to the current model's *limits*. No claim that microstructure, porosity, roughness or residual stress was fitted as a numeric predictor.
- Single-column U.S. English, page numbers, **continuous line numbers**, notation table, **Roman table numbers I–IX** (including linked Roman numerals in the running text), and editable table text near first discussion. Tables I, II and VII now fit portrait pages rather than landscape; Figure 1 has simplified noncrossing connectors and the independent EPS graphic was updated.
- References are **numerical in first-citation order**, with journal-title abbreviations and journal article titles omitted; the source reference entries retain DOI URLs. The journal requires COMPLETE author lists. One unresolved entry is explicitly labelled below.
- **User-confirmed sole author and affiliation** are on the title page. A sole-author contribution statement and **no-external-funding** statement are present; the unused Acknowledgments section is omitted. Corresponding-author email and conflict-of-interest declaration still require confirmation.
- Separately named vector EPS illustrations: [Fig1.eps](Fig1.eps) (cohorts) and [Fig2.eps](Fig2.eps) (primary and event-specific NLL). They use the same frozen counts and comparison values as the embedded TikZ figures. The EPS artwork needs final font-embedding, exact export-size, and quality preflight.

## Compile and submit with the correct file roles

From inside this directory, using MiKTeX pdfLaTeX or TeX Live:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main_MMTA_2026-10-27.tex
```

The repository also runs an automated PDF build in [MMTA GitHub Actions](https://github.com/sreearravind/Synthetic-Augmentation-for-Censor-Aware-Fatigue-Life-Prediction-of-LPBF-Al/actions/workflows/mmta-latex-build.yml). Download the PDF artifact from a **successful run on this source**.

**Important file roles from the uploaded author guide:** Upload the **compiled full-manuscript PDF as the Article file**, the corresponding `.tex` as **LaTeX Supplementary Files**, and separate, production-appropriate high-resolution figure files. This is different from the earlier JMEP packaging. Do not upload the EPS artwork as captioned figures: captions are already typeset within the manuscript.

**Topical collection portal:** https://mmta.msubmit.net/ . Select Topical Collection article type, then the precise collection *Microstructural Evolution, Degradation Mechanisms, and Failure Analysis in Structural Metals and Alloys* on the subsequent collection-choice screen. Name the collection in the required cover letter. Authors will receive verification email links and must approve the manuscript conversion.

## Author-required submission blockers

1. **Title-page identity and consent:** The user confirmed **Sreearravind Mani** as sole author and **Department of Mechanical Engineering, J.J. College of Engineering and Technology, Tiruchirappalli - 620009, Tamil Nadu, India** as affiliation. Corresponding-author email remains to be supplied. The sole author must review and approve the final version before submission.
2. **Contribution statement:** A sole-author contribution description has been drafted for Sreearravind Mani before the conflict section. The author should confirm it accurately reflects all research/software/analysis/writing responsibilities.
3. **Conflicts and funding:** The author confirmed no applicable funding or acknowledgments; the manuscript states **no external funding** and omits Acknowledgments. **Conflict-of-interest status remains unconfirmed** and must be supplied. Ensure original/public-source specimen tables' licensing and reproduction permissions are appropriate.
4. **Reference audit:** The Matušů 2026 journal entry still says `and coauthors`, disallowed by MMTA. Verify the **full published-paper list and exact order** from the publisher, not only the differently ordered Zenodo dataset-creator list. Cross-check all 16 journal names against the CAS abbreviation index, exact years, article IDs/volumes, and Al-Zuhairi's 2026 preprint version and citation.
5. **Figure production preflight:** Our independent `Fig1.eps` and `Fig2.eps` sources are vector, but EPS text uses standard PostScript font references that are **not independently verified as embedded**. Make final EPS or TIFF exports with embedded fonts, legible line-art labels, correct panel labels, and physical width 84 or 174 mm (maximum height 234 mm). Confirm submitted artwork visually matches the PDF's two embedded figures.
6. **Scientific fit check:** MMTA and this topical collection foreground microstructure, degradation and metallurgical mechanisms. This manuscript has only a stress-amplitude fitted specimen-level predictor. Source variation cannot be interpreted as a measured defect mechanism. Its negative/mixed augmentation finding must not be rebranded as an experimental microstructure model. Editorial consideration is uncertain; avoid claiming acceptance or guaranteed thematic fit.
7. **Final copyedit:** The manuscript currently retains a long text body. Check completeness, clarity, English (U.S.), citation continuity, Table of Symbols, equation numbering, figure/table references, production PDF and line-number continuity. This draft has not been checked by journal editors.
8. **Supporting files:** If the submission depends on any unpublished manuscript, provide it as a Related Manuscript File, not ESM. Published data and public reproducibility ledgers can be cited with verified archive links; don't upload proprietary or third-party supplementary data without permission.
9. **Required cover letter:** Provide importance of findings, source of originality and fit, and the precise topical collection name; a draft [cover letter](Cover_letter_MMTA_topical_draft.md) is supplied separately for author approval.

The official instruction document supplied by the author was the controlling reference. Current public guidance: https://link.springer.com/journal/11661/submission-guidelines ; collection: https://link.springer.com/journal/11661/updates/27848628 .

## Reproducibility controls

No models were refitted; no extra physical tests, microstructural measurements, performance metrics, or speculative significant improvements were added. Original primary 192 at R=0.1 (166 failures, 26 runouts); C0 1.27714, C1 1.27299, S0 1.27449, S1 1.27330. Romano belongs to the development inventory; Beretta and Al-Zuhairi are two differently scoped post-intake score checks. The earlier JMEP manuscript remains available as the source snapshot.

**Next gate:** Author review and completion of blockers, then journal-specific production validation and review of the final compiled PDF. No submission to MMTA has been initiated.
