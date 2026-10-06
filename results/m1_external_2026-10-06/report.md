# M1 source-aware Weibull: external Figure 10 check

**Status: provisional graph-derived validation, 6 October 2026.** Model and score rule were locked before this run. The 46 Hamidi Nasab 2019 plotted positions were read by two computational methods operated by one analyst; an independent second human reading is pending. The three Wu/Romano/Chen development folds were examined in earlier tasks and remain exploratory.

## Verification before external scoring

- Exact smooth input hash matched the frozen 66 rows (57 failures, nine runouts): `29aff38de63880dbfbaf65d3b876b81bd5afabfaaaac1615e2e503fbfa661a30`.
- Source manifest hash matched `0df2fdec2399cae1c76c202a323691431bdc96bb9eb31fa278f6b307ac84eb91`. Each development fold had disjoint training/test studies and the frozen 66 membership records.
- Hamidi Nasab ledger Git blob matched `840b7855fdc0d51c988dc6d7816f9b54cb6e2276`: 49 stored positions, 46 primary positions (VF 16, SB 15, MP 15), three held merged glyphs. Events: 40 failures, six runouts at the paper-supported 5 × 10⁶ cycle bound. All figure maximum-stress values were converted to amplitude as 0.45 × maximum stress. External amplitude range was 38.33–110.29 MPa, inside the combined exact training range 22.5–200 MPa.
- The first 41-versus-81-node training fit failed the 1e-5 integration tolerance. Before external scoring the numerical-only amendment fixed all fits at 161 Gauss–Hermite nodes with a 321-node check. All nine development fits and all three full-source fits passed. The largest full-source objective difference was below 8 × 10⁻¹⁰; no model parameter hit the imposed beta or shape bounds. The software and input hashes are in `run_metadata.json`.

## Locked primary external comparison

The score is **mean right-censored negative log likelihood of log10 cycles**, lower being better. M1 uses fixed study-effect standard deviation `tau = 0.25` log10 cycles and integrates over a fresh study effect for each prospective test prediction. E0 is refit on exactly the same 66 training rows. A negative difference favors M1.

| Figure 10 stratum | Positions (failure/runout) | E0 NLL | M1 NLL | M1 − E0 |
| --- | ---: | ---: | ---: | ---: |
| All finishes | 46 (40/6) | 1.2074 | 1.1876 | **−0.0198** |
| Vibrofinished | 16 (14/2) | 1.1203 | 1.1357 | +0.0154 |
| Sandblasted | 15 (13/2) | 1.2238 | 1.1941 | −0.0296 |
| Machined and polished | 15 (13/2) | 1.2840 | 1.2363 | −0.0477 |

The modest overall improvement comes from the six runout survival contributions: their summed NLL falls from 15.5260 (E0) to 13.5378 (M1). The 40 observed failures move in the other direction: summed failure-density NLL rises from 40.0159 to 41.0913. Failure-only median-life absolute error also rises from 0.3651 to 0.3852 log10 cycles. M1 does **not** resolve the failure-versus-runout trade-off.

## Fixed sensitivity analyses

The nine coordinated graph-reading scenarios vary lower/center/upper stress and failure-life readings. The six runout bounds stay fixed at 5 × 10⁶ cycles. The ranges below are **reading envelopes**, not confidence intervals; they show the range of paired M1−E0 mean NLL.

| Study-effect SD tau | Center overall M1 − E0 | Nine-scenario overall range | VF center | SB center | MP center |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 0.10 | −0.0053 | −0.0061 to −0.0046 | +0.0023 | −0.0077 | −0.0112 |
| **0.25 (locked primary)** | **−0.0198** | **−0.0229 to −0.0166** | **+0.0154** | **−0.0296** | **−0.0477** |
| 0.50 | −0.0131 | −0.0190 to −0.0072 | +0.0503 | −0.0287 | −0.0652 |

The sign of the overall paired comparison persists across these declared assumptions, but its size depends on tau, and vibrofinished specimens favor E0 for every tau. There is one independent external campaign and graph-derived outcomes; specimen count does not establish a population-level effect.

For context, the previously inspected exact source holdouts at tau = 0.25 gave M1−E0 mean NLL of +0.4423 (Wu), −0.6058 (Romano), and +0.0265 (Chen). These were not fresh validation and show inconsistent transport among source protocols. No synthetic observations entered either model.

## Interpretation and next decision

The source-aware model gives a small, stable overall gain against E0 on this one external graph campaign, driven entirely by better runout survival and partly offset by worse failure density and median-life error. It is a conventional model comparator, **not** the manuscript's proposed algorithm or proof of a selective synthetic augmentation benefit. Retain the predeclared 46-position primary set, do not tune tau or choose finishes on this test, and do not describe the graph as independently human-validated yet. A second reader should check all glyph identities and the three held overlaps; any membership change needs a versioned deviation and separate reporting. Subsequent method changes require another unused campaign for a fresh confirmatory test.

Reproduce with `scripts/fit_m1_source_aware.py --stage validate` and then `--stage external`, passing the exact CSV, source manifest, reconciled external JSON and output directory. The detailed CSV files retain all 46 center predictions, the 3 × 9 × 4 scenario/stratum scores, exploratory fold scores and fitted parameters.
