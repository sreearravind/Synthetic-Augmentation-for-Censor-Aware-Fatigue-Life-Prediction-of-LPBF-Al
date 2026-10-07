# van der Rest 2025 supplementary-table access and source screen — 7 October 2026

**Target.** Camille van der Rest, Rodrigo Arturo Manzano Navarrete, Aude Simar, Olivier Poncelet, “Influence of roughness and subsurface porosity on the fatigue life of AlSi10Mg produced by Laser Powder Bed Fusion,” *Materials Science and Engineering: A* 944 (2025) 148885. [Publisher DOI](https://doi.org/10.1016/j.msea.2025.148885); [UCLouvain open article](https://research.dial.uclouvain.be/entities/publication/b14c73bf-cc3a-4fe7-8c49-f559488ee175).

## Verification from the article

- The article describes three AlSi10Mg contour families (85–1200 rough; 100–600 smooth; 100–300 smooth with keyhole pores) and stress-relieved, polished, or sandblasted conditions. These are process/treatment groups, not automatically individual numerical features.
- Main-text Table 4 gives roughness parameters `Ra`, `Rz`, `Rv`, and `Rp` as **group summaries** (mean ± spread). No original specimen identifier joins an individual roughness value to a fatigue observation in that table.
- Main-text Table 7 and Figures 10–13 document failure-initiation categories and multiple runouts. The figures mark runouts with arrows, and the article describes the `10^7`-cycle stop. The stress levels discussed are **maximum stress** in MPa; do not relabel them stress amplitude.
- The paper explicitly says supplementary **Table S1** provides fatigue-initiation sites by stress level; **Tables S2 and S3** are cited for further initiation-site detail in polished and sandblasted specimens. Their precise columns, row counts, and any specimen identifiers are **unverified** here.
- The article's data-availability statement says data will be made available on request. The UCLouvain publication record exposes a PDF of the article; it does not list S1–S3 as separate files on the record inspected.

## Access attempts and decision

Exact title, DOI, PII `S0921509325011098`, `mmc1`, and supplementary-table searches were checked against the public publisher/index and institutional record. The available web retrieval did not return the actual S1–S3 attachments; direct Elsevier CDN candidate URLs were inaccessible through the retrieval service. A name search in the user's connected Drive did not identify a matching supplement. **The supplementary tables were not read.** No conclusions about their undisclosed columns, exact rows, pretest timing, or identifier joins are justified.

| Gate | Evidence as of this audit | Status |
| --- | --- | --- |
| Independent first-exposure specimens | Main article describes a new contour/treatment campaign, but original IDs and overlap with other publications need a row-level check. | Pending supplement and provenance |
| Per-specimen numeric pretest roughness/XCT | Group roughness summaries in Table 4; supplementary contents unknown. Initiation-site labels are postfailure and cannot serve as prospective predictors. | Not established |
| Stress, life, event, runout bound | Main figures show marked `10^7` runouts and stress maxima; exact rowwise event values/IDs may or may not be in supplements. | Partial, no exact ledger |
| Eligibility for feature-plus-censor model | Requires all of the above joined on the same original specimen. | **Not admitted** |

**Next input needed to resolve this gate:** the actual publisher Supplementary Materials file(s) containing Tables S1–S3, obtainable from the article’s “Supplementary data” section at the [publisher DOI](https://doi.org/10.1016/j.msea.2025.148885). Once present, audit their columns and provenance; if they only give initiation categories, treat them as outcome annotations, never as pretest XCT or roughness. No author data request is necessary for this first inspection. The [v2 cohort](../data/cohorts/development_v2_199_2026-10-06.csv) and fixed comparisons remain untouched.
