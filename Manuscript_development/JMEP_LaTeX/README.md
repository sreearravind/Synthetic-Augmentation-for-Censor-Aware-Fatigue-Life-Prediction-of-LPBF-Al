# JMEP LaTeX manuscript — MiKTeX and XeLaTeX build guide

The corrected [main manuscript](main_JMEP_2026-10-09.tex) preserves the original scientific text, numerical results, equations, nine tables and two figures. **The main file now supports both pdfLaTeX (the MiKTeX default in the reported error log) and XeLaTeX.** It conditionally loads `fontspec` only when running with XeLaTeX or LuaLaTeX and instead uses T1-encoded Latin Modern fonts under pdfLaTeX. Both figures are drawn as vectors in TikZ directly from frozen results; Inkscape, `-shell-escape`, and SVG conversion are no longer required.

## Compile with MiKTeX on Windows

Download the latest `main_JMEP_2026-10-09.tex` from this folder (GitHub **Raw**), not an older local copy. Open a terminal **in that file's directory** and run:

```powershell
pdflatex -halt-on-error -interaction=nonstopmode main_JMEP_2026-10-09.tex
pdflatex -halt-on-error -interaction=nonstopmode main_JMEP_2026-10-09.tex
```

The second pass resolves references. If using TeXworks, select the **pdfLaTeX** typesetting engine and click Typeset. For TeXstudio, configure the default compiler to **pdfLaTeX** under Options → Configure TeXstudio → Build. It is no longer necessary to switch engines. Alternatively, XeLaTeX remains supported:

```powershell
xelatex -halt-on-error -interaction=nonstopmode main_JMEP_2026-10-09.tex
```

Enable automatic installation of missing packages in MiKTeX Console if prompted (particularly `tikz`/PGF and `newunicodechar`). Do not use bare `latex` producing DVI; use the named PDF-generating compiler.

## Why the earlier file failed

The log showed `This is pdfTeX` followed by `Fatal Package fontspec Error`. The earlier preamble had an unconditional `\usepackage{fontspec}`, a package which requires XeTeX or LuaTeX. The corrected preamble now detects the active engine with `iftex` and only loads that font package in the appropriate branch.

A second independent portability issue was that figures were included through `\includesvg`, which requires external SVG conversion (and usually shell escape). The figures now use native TikZ within the same `.tex` file. The original SVG files remain in [Figures](Figures/) as editable artwork for journal graphics preparation but are **not compilation dependencies**.

## Structure and source integrity

The current scientific manuscript is the integrated Option A study on the limits of stress-only synthetic augmentation. The original primary macro censored NLL values C0 1.27714, C1 1.27299, S0 1.27449 and S1 1.27330 are not changed. Tables 1–9, 16 source references, original author–year findings and both figure captions are preserved. All 16 bibliography entries are embedded in the file, so no BibTeX or Biber run is needed.

For final *Journal of Materials Engineering and Performance* submission, the author list, some bibliographic metadata, title length and journal-specific Word-based submission requirements still require review. This corrected source is a working manuscript, not a guarantee of journal acceptance.

**Build-check status:** The prior repo version was structurally inspected but not compiled; after this correction, the MiKTeX-compatible font and TikZ package branch was smoke-tested with local pdfLaTeX. A complete-manuscript automated build is being configured separately; check the repository's GitHub Actions PDF build before assuming the entire article has compiled without errors.
