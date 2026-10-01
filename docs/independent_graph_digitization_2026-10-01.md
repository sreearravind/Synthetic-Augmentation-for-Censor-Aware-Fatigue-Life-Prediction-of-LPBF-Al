# Independent S–N graph digitization: AlSi10Mg

Date: 2026-10-01. This is a separately labelled, approximate experimental tier. The 26 rows are **not** part of `smooth_core_66.csv` or `confirmed_outcomes_75.csv`; no synthetic records were generated here.

| Primary experiment | Original evidence | Accepted rows | Outcomes | Method |
| --- | --- | ---: | --- | --- |
| Zhang et al. (2022), [DOI 10.1016/j.ijmecsci.2022.107336](https://doi.org/10.1016/j.ijmecsci.2022.107336) | Fig. 4, PDF physical p. 5 | 20 | 15 failures, 5 right-censored | Three build directions; stress and plotted cycles from colored glyphs. Paper states R=0, 85 Hz, and artificial stopping beyond 10⁸ cycles. |
| Glodež et al. (2020), [DOI 10.1016/S1003-6326(20)65403-6](https://doi.org/10.1016/S1003-6326(20)65403-6) | Table 2, PDF physical p. 4; Fig. 10, PDF physical p. 8 | 6 | 5 failures, 1 right-censored | Exact stress amplitude from Table 2; plotted cycles read from distinct filled/open circles. Paper states R=0, 25 Hz, and 4×10⁶ stopping cycles. |

The studies are independently authored and use different printing systems, surface preparations, specimen geometries and frequencies. They do not duplicate the Wu, Romano/Tognan or Chen source studies in the exact cohort. The Romano and Tognan reports are treated as one underlying experiment elsewhere in the project.

## Pixel calibration and outcomes

Zhang Fig. 4 was cropped from the rendered PDF and enlarged 2×. In crop pixels, the logarithmic abscissa uses 10⁵ at x=118 and 10⁸ at x=1073: `log10(N) = 5 + (x−118)/318.5`. The ordinate is maximum stress in MPa: approximately `sigma_max = 220−y/10.08`. A colored glyph with a rightward arrow is censored. A colored glyph without one is recorded as a failure, including Z05 on the 10⁸ line, which remains explicitly flagged for visual recheck. For every censored row, the model lower bound is the paper-supported conservative 10⁸ cycles, regardless of the arrowhead's position on the plot.

Glodež Fig. 10 was cropped and enlarged 2×. Its log cycle axis uses 10³ at x=28 and 10⁶ at x=906: `log10(N) = 3 + (x−28)/292.5`. Filled circles are failures and an open circle is a runout. Table 2 has `sigma_a = sigma_m` for R=0, so `sigma_max = 2 sigma_a`. Runout G05 is lower-bounded by 4×10⁶ cycles; its chart coordinate is only a visual cross-check.

For failure lives, `cycles_plotted_approx` and `cycles_for_censor_model` both represent the graph-read value. For runouts, `cycles_plotted_approx` is the graphic's plotted coordinate, while `cycles_for_censor_model` is the documented conservative survival lower bound. `event_failure=1` means failure, `0` means right censoring. Pixel centers and halfwidths are stored to generate the `log10N_read_low/high` and stress bounds. These are reading intervals, not statistical confidence intervals. Glodež stress bounds are the exact printed loading level, whereas the life bounds remain graphic reading intervals.

## Quarantine and analysis gate

- Glodež specimens 3 and 4 have printed maximum stresses 125.8 and 126.8 MPa, respectively. They cannot be reliably paired with two distinct life glyphs at this resolution. Neither life is inferred.
- A thick mark around Glodež crop `(x≈785, y≈375)` has a graph ordinate around 139 MPa with no matching Table 2 loading. It may be a curve overlay; it is not treated as a specimen.
- The Zhang 0° marker Z05 is on the 10⁸ boundary and lacks an arrow. It is included as a plotted failure with a flag for manual image recheck before a final manuscript claim. Adjacent colored glyphs have widened reading bounds.
- Use the 26 rows only in a prespecified approximate-tier sensitivity or external-source analysis, grouped by study in any split. Compare with the exact cohort rather than silently pooling. Fit transformations and synthetic generators only on training groups. A runout bound is never used as an observed failure time.

This is a source extraction and uncertainty ledger. It does not establish model validity or Q1 journal sufficiency.
