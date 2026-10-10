# JMEP working LaTeX package — 9 October 2026

This directory holds a **faithful LaTeX conversion of the current integrated Option A research manuscript**, not a final ScholarOne submission file. No cohort, experimental outcome, numerical model result, scientific conclusion or literature claim was rewritten for the conversion.

## Package contents

- [main_JMEP_2026-10-09.tex](main_JMEP_2026-10-09.tex) — full manuscript: preserved title, ~187-word abstract, seven working keywords, Introduction, Methods, Results, Discussion, Conclusions, embedded numbered references, data/code availability, nine table floats and two figure floats.
- [Figures/Figure_1_Cohort_Provenance_Validation_Roles.svg](Figures/Figure_1_Cohort_Provenance_Validation_Roles.svg) — first-exposure source provenance and evaluation roles.
- [Figures/Figure_2_Primary_Publication_and_Event_Specific_NLL.svg](Figures/Figure_2_Primary_Publication_and_Event_Specific_NLL.svg) — publication-held-out NLL and censored failure/runout decomposition.

To obtain the whole package, clone or download the GitHub repository and keep this folder's `main_JMEP_2026-10-09.tex` and the `Figures/` directory together.

## Compile locally / Overleaf

This is a **single-column XeLaTeX working manuscript using the standard LaTeX `article` class**, not a claim to be the official JMEP production template. It uses standard TeX Live packages, `fontspec`, `newunicodechar`, `amsmath`, `svg`, `tabularx`, `pdflscape` and `hyperref`. No separate BibTeX database is necessary because the sixteen source references are in `thebibliography` inside the main file.

Set your editor's compiler to **XeLaTeX** and enable shell escape for SVG conversion by Inkscape. From within this directory, run:

```bash
latexmk -xelatex -shell-escape -interaction=nonstopmode main_JMEP_2026-10-09.tex
```

In Overleaf: upload the `.tex` and both SVGs, choose XeLaTeX, and ensure SVG conversion is supported. If an environment disallows `-shell-escape`, convert both SVG files to vector PDF outside LaTeX and replace the two `\includesvg` commands with `\includegraphics` commands using the converted PDFs. The figure content comes from the archived analysis, not newly generated experimental values.

**Validation completed:** full main file and two SVGs were committed and read back; file structure, paired LaTeX environments, 12 equation blocks, 9 tables, 2 figures, 16 bibliography items and all 16 citation keys were checked. **Full-document XeLaTeX compilation and visual page proofing have not been performed on this exact repository source**; do not infer a PDF build was tested solely from structural checks.

## JMEP-specific author-instruction check

Primary journal: *Journal of Materials Engineering and Performance* (JMEP).

Official instructions: https://link.springer.com/journal/11665/submission-guidelines

Current instructions say:

1. JMEP's described manuscript submission workflow primarily requests a **Word manuscript file** with manuscript text, references, figure captions and tables in one document; tables/figures are placed after the reference list, and high-quality figure files are separate. This LaTeX version is an editable working source; convert to Word or confirm LaTeX upload support in ScholarOne before submission.
2. Title maximum **15 words**. The original currently retained title is **16 words**; shorten it at journal-formatting stage without altering scientific findings.
3. Abstract **fewer than 200 words**; the retained abstract is approximately **187 words**.
4. **Four to seven keywords** (with two or three drawn from the journal's submission-menu categories). Seven working keywords are present, pending journal-menu selection.
5. Journal references should include the article titles and the **full author list**. The current working bibliography retains the existing unresolved Matušů author list ("and coauthors") and should not be used as final journal copy before metadata verification; double-check the Al-Zuhairi preprint identity and Tridello 2023a/b order.
6. JMEP requests figures that remain clear in black and white; for final line art it specifies high-resolution separate artwork. The SVGs are vector sources; prepare production proof/export in an accepted artwork format.
7. Actual author/affiliation/contact data, funding, acknowledgments and declarations must be supplied by the authors. None were invented here.

Reference-only Springer Nature LaTeX resources: https://www.springernature.com/gp/authors/campaigns/latex-author-support . Springer provides a generic `sn-jnl` journal template, but the original JMEP guidelines should take precedence over general Springer guidance.

## Known conversion boundary

The converted `.tex` keeps the original manuscript's section text, scores and end-of-article bibliography but maps Markdown tables to standard numbered LaTeX floats. Narrative author–year citations were changed into `\cite{...}` where systematically identifiable, without deleting the original study names. The numeric citation order and full reference bibliography require a final JMEP-specific copyedit. The current figures remain SVGs bundled with the source rather than already checked 1200-DPI exports.

Source baseline (unchanged): [integrated Option A Markdown](../Manuscript_Integrated_Option_A_2026-10-09.md). If manuscript content is revised later, the LaTeX source and figures must be re-synchronized with that authoritative manuscript.
