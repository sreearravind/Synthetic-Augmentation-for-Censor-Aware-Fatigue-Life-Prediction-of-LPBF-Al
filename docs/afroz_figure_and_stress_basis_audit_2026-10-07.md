# Afroz figure reconciliation and stress-basis gate — 7 October 2026

**Scope and decision:** Audit the [five-glyph pilot](../data/candidates/afroz_fig9_fig11_five_glyph_pilot_2026-10-06.csv) from [Afroz et al., DOI 10.1007/s40964-024-00759-x](https://doi.org/10.1007/s40964-024-00759-x). These remain graph-approximate **candidate observations, not v2 training or external scoring rows**. Frozen v2 membership remains 199. No model fitting or synthetic generation was performed. The uploaded Springer version-of-record PDF (19 pages) is the figure source, printed pp. 2430 and 2432 (PDF pages 8 and 10).

## Second rendering and cross-figure reconciliation

I separately rasterized the original PDF at **250 dpi** and manually read Fig. 9a's logarithmic cycle axis and Fig. 11a's logarithmic life and linear Ra axes. This is a **second rendering/reading by the same analyst**, not an independent second-person adjudication. The [second-read ledger](../data/candidates/afroz_five_glyph_second_render_check_2026-10-07.csv) preserves both reads and differences relative to the earlier 6× rendering; figures are not reproduced in the repo. All five glyphs are filled M markers at reported R=0.1 and maximum stress 150 or 200 MPa. The selected points are away from the explicitly labelled "No failure" cluster at 10^7 cycles.

| Candidate | Maximum stress (MPa) | Second Ra (nm, approximate) | Second Fig. 9 life (cycles, approximate) | Second Fig. 11 life (cycles, approximate) | Largest difference from first reading |
| --- | ---: | ---: | ---: | ---: | ---: |
| A_M150_1 | 150 | 1250 | 411,000 | 417,000 | 1.3% |
| A_M150_2 | 150 | 1030 | 1,430,000 | 1,450,000 | 1.9% |
| A_M150_3 | 150 | 1080 | 1,860,000 | 1,920,000 | 3.4% |
| A_M200_1 | 200 | 970 | 46,300 | 45,400 | 2.3% |
| A_M200_2 | 200 | 1040 | 81,200 | 80,900 | 1.1% |

The first pilot's ±10% life and ±35 nm Ra **reading** bounds enclose the second reading. Fig. 9a and Fig. 11a life coordinates cross-check their same-stress, same-finish glyphs, but there are no source specimen IDs. The three M/150 Fig. 9 second-read lives average about 1.234×10^6 cycles, consistent with Table 5's **rounded group mean** 1.23×10^6; the mean is only an aggregate check, never a fourth record or a replacement for specimen life. The two M/200 glyphs are only part of that group's plotted points, so their mean is not comparable to the Table 5 mean.

No symbol-by-symbol roughness pairing is formally documented by specimen identifier; uniqueness here derives from matching figure life/stress/finish coordinates. A second human or independent vector-coordinate adjudication is still desirable before release as specimen-level graph data. Fig. 11c's Rz panel re-plots the same tests and must not be counted as additional specimens.

## Stress audit

Section 2.2 and Table 4 call the relevant test **tension–tension, R=0.1**, and give maximum stress 150 and 200 MPa. Fig. 9a and Fig. 11a repeat those maximum-stress labels. For the standard definition R=σmin/σmax, σa=(σmax−σmin)/2=(1−R)σmax/2; hence the implied amplitudes are **67.5 MPa** at 150 and **90 MPa** at 200. Table 5 instead prints **82.5 and 110 MPa**, or 0.55σmax at both levels. If these amplitudes were applied literally, the implied R would be −0.1, inconsistent with the paper's stated tension–tension R=0.1. This is a diagnostic equivalence, **not** a claim about the machine's actual loading.

Fig. 9a's right-hand secondary axis does not fix the discrepancy: on the rendered figure its amplitude ticks do not consistently align with either the nominal-stress ticks or Table 5 values (for instance, the 150-MPa row aligns near the secondary 88-MPa tick, rather than the listed 82.5 MPa). It therefore cannot be used to infer the true applied amplitude. Fig. 9b at R=−1 and Table 5's R=−1 amplitudes are consistent with σa=σmax; that agreement does not adjudicate panel a.

| Field | Usable statement | Gate |
| --- | --- | --- |
| Maximum stress | 150 or 200 MPa, explicitly reported in Table 4 and both figure legends | Preserve verbatim, with figure locator |
| Load ratio | Reported R=0.1 | Preserve as *reported*, flag contradictory derived amplitude |
| Amplitude | Table 5 prints 82.5/110 MPa; standard R=0.1 yields 67.5/90 MPa | **Unresolved**; do not substitute either silently |
| Life and event | Approximate individual graph failure glyphs; published 10^7 no-failure marks are separate | Graph precision, no exact specimen ID |
| Ra | Approximate individual gauge roughness from Fig. 11a | Paper says five gauge lines per fatigue specimen; measurement timestamp relative to first loading is not explicit |
| Pore predictor | Paper includes before/after XCT on selected specimens | No per-glyph pretest XCT join established |

No correction or supplementary raw fatigue table was identified on the publisher article page at this audit. Its data-availability statement says the supporting data are within the article. Absence of a correction in this targeted check is not proof none exists.

**Eligibility decision:** Retain the five paired glyphs as a reproducible **feasibility pilot only**. Do not pass them through the amplitude-only v2 reader, claim exact specimen measurements, imply independently confirmed pretest Ra timing, infer pretest pore features from postfracture defects, or use the 10^7 no-failure points as failures. If source clarification becomes available, resolve the load ratio/amplitude and measurement timing first; then predeclare how graph precision, source grouping and right censoring would be represented before testing any model. If clarification is unavailable, maximum-stress-based descriptive comparisons may cite these plotted points, explicitly quarantined from the locked model evaluation.

**Next task:** Seek a source-author correction/protocol or a genuinely independent report of the machine load ratio/stress amplitude and roughness acquisition order. In parallel, identify another published original campaign with specimen-level pretest inputs and clear failure/runout flags; do not make model-selection decisions from this quarantined pilot.
