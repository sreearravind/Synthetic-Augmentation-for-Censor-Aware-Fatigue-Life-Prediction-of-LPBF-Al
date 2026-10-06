# File-based Afroz pilot and Rahmdel data schema gate — 6 October 2026

**Status:** evidence screening only. Supersedes the access limitations in [the earlier access audit](afroz_rahmdel_access_and_pairing_audit_2026-10-06.md). No rows added to the frozen 199-row v2 cohort; no fitting, synthetic generation, scoring, or alteration of reserved sources. This deposit is a **quarantined candidate external campaign** pending protocol and overlap adjudication. The fatigue outcome workbook was inspected for structure and ID consistency, not used to choose model settings or calculate performance.

## Afroz: five paired graph glyphs

Source: [Afroz et al., DOI 10.1007/s40964-024-00759-x](https://doi.org/10.1007/s40964-024-00759-x); supplied publisher PDF, physical printed pages 2430 (Fig. 9) and 2432 (Fig. 11), PDF pages 8 and 10 (1-based). The paper says five gauge-line roughness measurements were averaged **per fatigue specimen** before its test (§2.5). Fig. 11a's legend identifies machined (filled symbols) at maximum applied stresses of 150 MPa (blue triangles) and 200 MPa (magenta diamonds), R=0.1. None of the five selected glyphs is labelled “No failure”; do not use adjacent runout symbols as failure data.

[Five-glyph pilot CSV](../data/candidates/afroz_fig9_fig11_five_glyph_pilot_2026-10-06.csv) records the separate reads. Fig. 11a was rasterized from the supplied PDF at 6×; its x ticks span pixel 159=0 and 1045=2500 nm, while y spans pixel 202=10^7 and 889=10^2 cycles. Filled-symbol pixel components gave the Ra and life estimates. Fig. 9a was read **separately** on a logarithmic x axis, approximately pixel 214=10^3 and 1215=10^7 cycles, at the corresponding maximum stress/finish. The two life readings agree to within ~1% for each selected glyph, markedly smaller than the conservative **±10% digitization interval**. Ra's conservative visual/read interval is ±35 nm; these bounds describe reading precision, not measured roughness uncertainty.

| Graph glyph | R | Finish | Maximum stress (MPa) | Ra from Fig. 11a (nm) | Life from Fig. 9a (cycles) | Life from Fig. 11a (cycles) |
| --- | ---: | --- | ---: | ---: | ---: | ---: |
| A_M150_1 | 0.1 | M | 150 | ~1251 | ~416,275 | ~412,179 |
| A_M150_2 | 0.1 | M | 150 | ~1032 | ~1,421,828 | ~1,423,432 |
| A_M150_3 | 0.1 | M | 150 | ~1077 | ~1,865,217 | ~1,857,574 |
| A_M200_1 | 0.1 | M | 200 | ~969 | ~46,809 | ~46,456 |
| A_M200_2 | 0.1 | M | 200 | ~1045 | ~81,675 | ~81,815 |

**Precision and identity:** These are five uniquely matchable plotted symbols in this stratum, not five identified source specimens with original IDs or exact measurements. They are a feasibility pilot, not exact-table rows. A separate human adjudicator has not reviewed the centroid assignments. Fig. 11c provides Rz for these same specimens but was not joined in this pilot; do not count that panel as more observations. Retain the original plotted units (nm; divide by 1000 for µm).

**Stress inconsistency requiring resolution:** Table 5 lists, for R=0.1, 150 MPa maximum stress and 82.5 MPa amplitude, and 200 MPa maximum stress and 110 MPa amplitude. The standard conversion with the stated R=0.1 gives 67.5 and 90 MPa respectively. Thus the printed amplitude equals 0.55 σmax, inconsistent with (1−R)σmax/2=0.45 σmax. No stress-amplitude values from Afroz should enter v2 until the loading convention/source error is adjudicated. The pilot preserves **published maximum stress**, as labelled in both figures.

## Rahmdel: the uploaded files, without TIFF

[Deposit DOI 10.17632/w4vsnk9z6w.1](https://data.mendeley.com/datasets/w4vsnk9z6w/1); user-provided [Drive folder](https://drive.google.com/drive/folders/1-PXD6Hh9FopEu5JznTXkuuL9hdQmOG0O?usp=drive_link). Two immediate subfolders are `Stress-Life Raw Data` and `XCT Results`; the latter separates AlSi10Mg from 17-4 PH. In the stress-life folder, [Fatigue results AlSi10Mg.xlsx](https://docs.google.com/spreadsheets/d/1JLU1XthF6YMQo4qRZWqPb7lpueTatFeS/edit?usp=drivesdk&ouid=108879325316895041323&rtpof=true&sd=true) is a single sheet (96×10) with two side-by-side table blocks. The right block H:J has 72 populated specimen-name rows, **70 distinct literal ID strings**; `T1L_2 (19)` and `T3S_5 (4)` each repeat, and `T1S`, `T1L`, `T3w` are truncated-looking entries that nevertheless have numeric fields. The table's life header says **“Reversals to Failure 2Nf”**; there is no explicit failure/runout flag or censor reason in that three-column block. Neither distinct row count nor `2Nf` can yet be called an independent first-exposure cycle count. The left A:C block has another specimen/stress/reversals layout and requires duplicate/extension adjudication before any union with H:J.

Nine AlSi10Mg XCT spreadsheets are available, one per named file, each a defect-component statistics export (`AfterErode`/similarly named tabs, ~877–4655 rows, ~35–38 columns). Headers include volume, surface, voxel counts, centroid, distance to surface, bounding dimensions, and ESD/ESR or ECR. Exports differ in **cm versus mm** surface/distance units and computed-volume columns. The spreadsheets alone contain no explicit scan date relative to fatigue, region/segmentation protocol, or unit audit sufficient to select an extreme defect prospectively.

A **literal or punctuation-normalized one-to-one filename match** to an ID in the fatigue workbook was found for only four XCT exports:

| XCT filename | Matched fatigue ID | Status |
| --- | --- | --- |
| `F_T1l_2_1.xlsx` | `F_T1L_2_1` | case-normalized match |
| `F_T2L_2_1.xlsx` | `T2L_2 (1)` | suffix format-normalized match |
| `F_T3W_8_1.xlsx` | `T3W_8 (1)` | suffix format-normalized match |
| `F_T3S_2_1.xlsx` | `T3S_2 (1)` | suffix format-normalized match |

The other five filenames (`F_T1W_2_1`, `F_T1S_2_1`, `F_T2S_1_1`, `F_T2W_1_1`, `F_T3L_2_1`) do not have that direct first-exposure ID match. Similar prefixes are insufficient. A matched filename only establishes **plausible identity**, not that the XCT scan preceded fatigue or that these four exports capture the gauge's complete prospective defect population.

**TIFF decision:** Omitting large TIFF stacks is entirely adequate for this **file-schema and candidate-link screen**. The nine statistics workbooks already show potential defect columns. It is **not yet adequate for a validated pretest XCT feature claim**: we need acquisition timing, voxel size, scanned region, mask/erosion definition, units and a source publication or README linking builds/specimens to the fatigue workbook. TIFFs would be useful later for image-based resegmentation or independent validation of an extreme-defect rule, but should not be transferred merely to count rows.

**Overlap and domain gate:** The 2024 Tahmasbi et al. [geometry/VHCF study](https://doi.org/10.1016/j.ijfatigue.2024.108544) involves Auburn coauthors, small and large blocks, 20 kHz, R=−1, and XCT of one fatigue specimen per geometry. Some context resembles this deposit; its five geometry types and described testing do not establish equivalence to this workbook's wall/small-block/large-block T1/T2/T3 layout. Verify campaign, batch, specimen ID and test protocol before calling the deposit independent, pooling it with conventional HCF, or scoring it externally.

## Gate and next task

1. **Afroz:** independent second-person or second-method verification of five centroids, then resolve the printed amplitude/R inconsistency. Keep graph-approximate status; do not replace exact outcomes.
2. **Rahmdel:** find a README/protocol or companion original paper documenting whether XCT scans are **before first fatigue exposure**, the voxel/ROI and units, whether `2Nf` is truly reversals, which values are runouts, and how the two workbook blocks relate. Resolve duplicate/truncated IDs and the five unmatched XCT filenames. Establish campaign independence and predeclare either a held-out test or a distinct training domain before outcome exploration.
3. Until those gates pass: **0 Mendeley rows and 0 Afroz pilot rows admitted to v2**. No new synthetic augmentation or model comparison.

This gate is about provenance and meaning. It is not an arbitrary SCI/Q1 minimum-row threshold.
