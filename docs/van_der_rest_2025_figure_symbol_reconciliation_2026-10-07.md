# van der Rest 2025 figure-symbol reconciliation — 7 October 2026

**Decision.** Figures 6, 10, 11 and 13 were independently inspected against the actual three-page supplement S1–S3. The plotted failure marks are **not completely separable into 108 individual experimental lives**. Do not digitize an artificial complete specimen ledger, use fit curves as observations, or turn table multiplicities into identical failure lives. The 14 runouts remain **reported group/stress counts with a 10^7-cycle bound**, not original-ID records. The [48-stratum aggregate count CSV](../data/candidates/van_der_rest_2025_supplement_48_aggregate_strata_2026-10-07.csv) remains the exact machine-readable level.

## Sources and method

The [article PDF](https://drive.google.com/file/d/1zz-RarEIv4i1GWtZYrFVcLrKEQXBInwJ/view) and [supplement PDF](https://drive.google.com/file/d/1SI9OGfgYtVYqFwqoAABFQDTvFOKBHhzA/view) were rendered and checked against the embedded original figure raster. The graph image XObjects for article Figures 6, 10, 11 and 13 are approximately 773 pixels wide. Figures 10/11/13 use black = SRHT, red = SRHT + polished, blue = SRHT + sandblasted. Figure 6 recolors the three **SRHT** contour families and duplicates those same observations, providing a visual cross-check rather than more tests. Supplementary S4/S5 likewise replot the polished and sandblasted series.

A reproducible **recoverability diagnostic**, not a specimen digitizer, inspected a 15-pixel vertical band centered on each reported stress level (240, 220, 200, 180, 160, and for SRHT also 140 MPa). For each graph color, it counted contiguous horizontal components at least three pixels wide with at least nine strongly colored pixels in the band. The mask thresholds were black: each RGB channel <85; red: R>140, G<100, B<100, R>1.5G; blue: B>140, R<100, G<100, B>1.5R. Fits, antialiasing and cross-color overprints can affect this diagnostic. It is only an observed **marker-like component count**, so matching a denominator does not prove a clean specimen join. Runout arrows near 10^7 cycles were interpreted using S2/S3, never as extra failures. Visual inspection confirmed the principal undercounts and merges.

| Article figure, contour family | Treatment | Supplement failures by stress, descending MPa | Visually separable marker-like components, same order | Failure-containing strata with undercount |
| --- | --- | --- | --- | ---: |
| Fig. 10, 85–1200 rough | SRHT | 1, 3, 2, 3, 2, 3 (240→140) | 1, 2, 2, 2, 2, 2 | 3/6 |
| Fig. 10, rough | Polished | 1, 3, 2, 3, 3 (240→160) | 1, 2, 1, 3, 3 | 2/5 |
| Fig. 10, rough | Sandblasted | 1, 3, 3, 0, 1 | 0, 2, 3, 0, 1 | 2/4 |
| Fig. 11, 100–600 smooth | SRHT | 1, 3, 2, 3, 2, 3 | 1, 2, 2, 2, 1, 3 | 3/6 |
| Fig. 11, smooth | Polished | 1, 4, 4, 1, 0 | 1, 4, 3, 1, 0 | 1/4 |
| Fig. 11, smooth | Sandblasted | 1, 4, 6, 0, 1 | 1, 2, 6, 0, 1 | 1/4 |
| Fig. 13, 100–300 smooth with KHP | SRHT | 1, 3, 2, 3, 2, 3 | 1*, 2, 1, 3, 1, 3 | 3/6 |
| Fig. 13, KHP | Polished | 1, 3, 3, 3, 2 | 1, 3, 3, 2, 2 | 1/5 |
| Fig. 13, KHP | Sandblasted | 1, 4, 5, 1, 1 | 1, 3, 4, 1, 0† | 3/5 |

`*` The black 240 MPa mark is partially overprinted by a blue mark. `†` A blue failure near the 160 MPa, 10^7-cycle runout arrow is not individually separable in the original plotting; article Fig. 14(b) names a **160 MPa, 8.6×10^6-cycle failure**, so the failure exists even though the Figure 13 image alone cannot give an unambiguous separate center. That named fractograph is evidence for that single outcome, not a license to impute all hidden marks.

Totals: S1–S3 give **108 failures** across **45 failure-containing group/stress strata**; the narrow pixel diagnostic finds **88 marker-like components**, with an undercount in **19 strata**. These are not estimates of sample loss. Fused marks, overprinting and fitted curves account for a material part of the difference. Independent visual reads of Figure 6 show overlapping marks at the same stresses for SRHT, and cannot resolve the missing original IDs.

## Specific ambiguities and disposition

- Fig. 10, rough sandblasted, 240 MPa: S3 gives one failed sample, but no independent blue marker is distinguishable at that stress in the original image.
- Fig. 11, smooth sandblasted, 220 MPa: S3 gives four failures but only two distinct blue components are visible under the diagnostic. Assigning two more cycles from the overlapping red/blue curves would invent measurements.
- Fig. 13, KHP sandblasted, 200 MPa: S3 gives five failures; a broad blue component near the far right appears merged, yielding four distinguishable clusters. At 160 MPa the plotted arrow and the known 8.6×10^6 failure are close together.
- Fig. 10, rough polished, 200 MPa: S2 gives two failures but its red ink forms one broad component. This is a merged cluster, not a duplicate with identical life.
- S4/S5 show the **same** tests at a different grouping and may help locate a visible mark, but must not be counted as new experimental records.

No confidence-rated per-specimen life values are released from this diagnostic: even apparently clean glyphs have no original specimen ID, and a partial selection would require its own prespecified graph-reading tier, symbol-level second reader, and uncertainty interval. There is no per-specimen pretest roughness/XCT join in any case. **No augmentation, model fit, score or frozen-cohort change was performed.**

**Next source decision:** retain van der Rest as strong aggregate evidence of censoring and surface/contour effects for the manuscript discussion. A feature-plus-censor cohort still needs another open per-ID source; the graph figures alone cannot provide it.
