# Hamidi Nasab 2019 Figure 10: independent method readings and reconciliation

**Status, 2 October 2026:** graphical source extraction and reconciliation completed; external model holdout remains sealed. The count below is of **resolvable plotted symbol positions**, not a verified count of physical specimens. No model fit, prediction, hyperparameter choice, or score used this source.

## Source and method

Milad Hamidi Nasab et al., *Effect of Surface and Subsurface Defects on Fatigue Behavior of AlSi10Mg Alloy Processed by Laser Powder Bed Fusion (L-PBF)*, [Metals 2019, 9, 1063; DOI 10.3390/met9101063](https://doi.org/10.3390/met9101063), Figure 10 on PDF page 10 and fatigue methods §2.4. [User-supplied Drive PDF](https://drive.google.com/file/d/1kzsnmm6JooGgoHAjdWfvVgBPwwlbe5SP/view). Its Drive filename names a different paper; the internal title and DOI above are authoritative. The PDF SHA-256 is `caf08c6ba88e9edebce30b4b9dcc8d49ae8f39a15cabcdb1b73fb98559c6cd8f`.

The paper reports axial constant-amplitude tests at **R = 0.1**, 30 Hz, in three finish conditions. The paper's runout stop is **5 × 10⁶ cycles**. Figure 10's ordinate is **maximum stress**. The prepared workbook calculates amplitude by `σa = (1 - R) σmax / 2 = 0.45 σmax`; no plotted ordinate is directly assumed to be stress amplitude.

Two distinct computational reads were made without consulting the prior fitted models:

1. **A, vector:** extracted each colored open-marker outline from page 10 PDF paths. The PDF contains an earlier clipped set of drawing paths; an outline was retained only if its color actually appears at the predicted position in the rendered page. Exactly coincident marker paths were recorded as multiplicity evidence, not silently counted as extra specimens.
2. **B, raster:** independently found marker centers in a 5× rendering using color-specific symbol templates and local maxima. The red circle, blue triangle and black diamond templates were seeded from isolated visible markers. No vector path positions were input to this detector.

The matched A/B centers differ by a mean **0.88 image pixels** (maximum **1.60 pixels**) among 46 matches; the matching gate was 3.2 pixels. This is agreement between extraction methods, not a calibrated laboratory measurement-error model or a claim of two independent human readers.

## Reconciliation and inclusion

| Finish | Vector-distinct visible positions | Independently matched primary positions | Primary failures | Primary runouts |
| --- | ---: | ---: | ---: | ---: |
| Vibrofinished (VF) | 17 | 16 | 14 | 2 |
| Sandblasted (SB) | 17 | 15 | 13 | 2 |
| Machined and polished (MP) | 15 | 15 | 13 | 2 |
| **Total** | **49** | **46** | **40** | **6** |

`HN2019_VF_15`, `HN2019_SB_05`, and `HN2019_SB_10` are **held from the primary test**: separate vector outlines exist, but their raster outlines overlap adjacent symbols too closely to isolate them independently. Their values and exact locations remain in the `Reading audit` worksheet for a prespecified sensitivity analysis if a human adjudication supports them. They are not model training examples.

Eight further vector outline paths lie **exactly on top of already visible runout symbols** (VF 3, SB 2, MP 3 additional paths). They may represent separately tested specimens sharing the same stress and stopping cycle, but the published figure does not identify specimen IDs. The primary cohort counts one row at each visible position and does not assert eight extra physical specimens. Any multiplicity-weighted sensitivity analysis must be declared as such and cannot replace the primary result.

All six primary symbols at the graph's 5 × 10⁶-cycle boundary are recorded as right-censored runouts with the paper's **fixed lower-bound cycle count**. Their horizontal arrowheads and marker widths are not failure times. The 40 other primary symbols are failures. Neither dashed fitted curves nor aggregate Table 5 fatigue limits generated any data row.

## Reading interval and usage limits

The log-life plot runs from 10⁴ to 10⁷ cycles. The plotted axes were calibrated in PDF coordinates at `x=187.0` (10⁴), `x=434.2` (10⁷), `y=547.6` (300 MPa), and `y=711.4` (0 MPa). A conservative half-glyph span of **1.92 PDF points** yields a failure-life reading interval of **±0.0233 log10 cycles** and maximum-stress span of **±3.52 MPa**. For a runout, only its stress gets a graphical interval; its paper-defined survival threshold remains 5 × 10⁶ cycles. These are **reading bounds**, not confidence intervals, a probability kernel, or an estimate of physical fatigue scatter.

The workbook preserves separate A/B centers, path counts, marker classifications, graph intervals, source DOI, include/hold decisions, and the stress conversion formula. Published figures are accessible to analysts, so “sealed” means that no holdout **numerical values or scores** inform model development, graph-error calibration, or synthetic training. The two methods were executed by one analyst. A second human reader should verify the marker ledger and the three overlapping areas before the final manuscript calls this independently reader-validated data.

To reproduce from the original PDF, use the two repository scripts with `--pdf <local PDF path> --output <reading directory>` for the first script and `--readings-dir <same directory>` for the second. The first script verifies the PDF SHA-256 before rendering or reading. The resulting `reconciled_records.json` contains every included and held position and the original path/reader evidence. The Excel workbook is named `AlSi10Mg_Nasab_2019_Figure10_Independent_Read_Ledger.xlsx`.

**Decision:** freeze the **46 agreed positions** as the primary independent experimental graph holdout (40 failures, six runouts), retaining 3 blended positions and 8 extra coincident drawing paths in a separate audit tier. The number of genuinely independent external **studies** represented here is one. Report treatment-specific and overall performance only after the model and metric rules are frozen.
