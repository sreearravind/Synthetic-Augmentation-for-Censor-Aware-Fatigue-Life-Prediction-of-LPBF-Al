# Afroz pairing and Rahmdel deposit access audit — 6 October 2026

**Decision:** No specimen rows added; v2 199-row membership and all model comparisons remain frozen. This is an access/provenance audit, not a new cohort or an external score.

## Rahmdel Mendeley deposit (10.17632/w4vsnk9z6w.1)

Primary landing page: https://data.mendeley.com/datasets/w4vsnk9z6w/1 (version 1, 19 August 2026, Keivan Rahmdel, Auburn University, CC BY 4.0). Its description advertises raw fatigue results, XCT data and fracture images for **both** AlSi10Mg and 17-4 PH, wall/small-block/large-block geometries and three sizes each. This is a claim about deposit scope, **not** a verified inventory, column schema or specimen count.

The web rendering exposes an empty `Files` heading and a `Download All` button without individual links. Mendeley's documented public-file endpoint (`GET /datasets/publics/{id}/files?version=1`) was attempted at `https://api.data.mendeley.com/datasets/publics/w4vsnk9z6w/files?version=1` and could not be resolved through the available web retrieval route. Direct command-line network access was unavailable. Thus **zero filenames, file headers, specimen IDs, scan timestamps or outcomes were inspected**. No inference that the deposit lacks files is justified. A web search found no primary, specimen-linked article unambiguously identifying this deposit's campaign; a same-institution or same-author association is insufficient for overlap adjudication.

**Quarantine rule:** do not ingest, train on or score this deposit. On acquiring the files, first list filenames, sizes, hashes, README and headers without reading life values into a modeling notebook. Resolve material, campaign/build, geometry, nominal versus local stress, loading mode, test frequency, first exposure, censoring and pretest scan timing. Reconcile specimen IDs with source publications and existing Auburn/other cohort families. Decide development or untouched external role **before** exploring outcome distributions.

## Afroz et al. (10.1007/s40964-024-00759-x): published evidence check

Primary article and PDF: https://link.springer.com/article/10.1007/s40964-024-00759-x and https://link.springer.com/content/pdf/10.1007/s40964-024-00759-x.pdf.

- Each fatigue specimen had five gauge-line roughness measurements averaged to Ra and Rz (§2.5). These are measured before fatigue and are plausible same-specimen predictors.
- Axial HCF was performed at R=0.1 and R=−1 on as-built (AB), machined (M) and, for R=−1, machined-and-polished (M&P) specimens. Fig. 9 shows S–N symbols; Fig. 11 plots each specimen's life against Ra or Rz, stratified by R, with stress encoded graphically.
- **Table 5 reports average life per stress/finish/R group**, not individual observations. It marks 10^7-cycle runouts at R=0.1, 120 MPa M and 100 MPa AB/M, and at R=−1, 80 MPa M/M&P. These entries cannot be duplicated as individual specimen records, and average values cannot be joined to a particular Fig. 11 roughness measurement.
- Fig. 11's Ra/Rz scales are **nm**, whereas discussion gives examples in **µm**. Units must be converted explicitly. The same plotted point appears in Ra and Rz panels; count once, not twice.
- The accessible figure/PDF web route exposed caption and text, but no downloadable raster/vector data for calibrated glyph reading in the present execution environment. The plotted symbols do not carry unique printed specimen IDs. Therefore no independently checked five-glyph coordinate ledger or one-to-one Fig. 9/Fig. 11 match can be certified in this audit. We did not invent coordinates, round mean lives into individual lives, classify an unlabeled runout, or infer a pore feature from posttest evidence.

### Pilot acceptance sheet for the next file-based read

Record **two independent reads** of each candidate Fig. 11 Ra and N glyph (and Rz as a consistency check), with panel, glyph centroid or marked image crop, axis calibration, units and reading interval. From Fig. 9 separately read maximum stress, life and failure/runout glyph; reconcile by R, finish, stress colour/shape, and life interval. Require a unique matching candidate; ties/overprints go to an exclusion ledger. Verify every runout bound against a printed arrow or test stop, not Table 5's average alone. A first pilot of up to five truly unique matches is sufficient to assess feasibility; five is **not** an imputed quota. The article should remain outside v2 until a prospective, same-specimen feature join passes this rule and source independence is audited.

| Check | Current result | Consequence |
| --- | --- | --- |
| Afroz specimen roughness measured | Yes, five lines per specimen | Feature timing plausible |
| Published paired life/roughness plot | Yes, Fig. 11 | Candidate for image-based pilot |
| Exact per-specimen values and IDs | No table found | Graph-precision only if readable |
| Independent Fig. 9/Fig. 11 coordinate match | Not certified here | **0 accepted new rows** |
| Mendeley file list and headers | Not exposed to current retrieval | **0 screened files** |
| Mendeley independent campaign and role | Unknown | Quarantined |

**Next single task:** obtain the Afroz PDF or full-resolution Fig. 9 and Fig. 11 images plus the Mendeley deposit's file archive/inventory as local/Drive-accessible files. Then perform the five-symbol double read and schema/overlap gate. Keep both outside the training notebook until the gate is signed.
