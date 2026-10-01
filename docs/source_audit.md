# Primary-table extraction audit

## Chen et al. 2024 — candidate inclusion

DOI: `10.1016/j.ijfatigue.2024.108163`. Tables 3 and 4 (PDF p. 7) and Table 5 (PDF p. 8) provide **nine failed specimens per group**, 27 exact failure records. Original specimen identifiers are not printed; local IDs encode group, table, and row order. The methods give tension–tension loading at `R=0.1`, 20 Hz, and a stop at `10^7` cycles for runouts. The tabulated records describe fractured specimens only; **no numerical runouts are added from these tables**.

L40 and L10 are smooth, ground specimens with nominal gauge length 40 and 10 mm, diameter 6 mm. R5 is notched, root radius 5 mm, diameter 6 mm, `Kt=1.27`. Table 2 reports group-level `V80`/`S80`: L40 1334 mm³/894.8 mm², L10 479.9/329.3, R5 23.73/49.62. Section 3.2 explicitly uses **local maximum stress** for R5. Preserve that basis and geometry when modelling; do not treat R5's reported `Sm` as an unqualified nominal smooth-specimen stress. The stress range and amplitude columns are derived from the reported maximum using `R=0.1`, so `Δσ=0.9 Sm` and `σa=0.45 Sm`.

The defect diameter, roundness, location and type are SEM measurements of the fatigue initiator **after fracture** (Section 2.3). They are audit/descriptive columns only. Using them as pretest predictors would leak information from the outcome. One L10 failure is attributed to a gas pore; the remaining 26 are attributed to lack-of-fusion defects.

## Roveda et al. 2024 — hold from independent master

DOI: `10.1016/j.matdes.2024.113170`. Table 4 (PDF p. 9) lists 20 exact fatigue test episodes across AB (6), HT1 (7: 265 °C for one hour), and HT2 (7: 300 °C for two hours). Seventeen entries have printed failure lives; one per group is a runout at exactly `10,000,000` cycles. Section 2.3 specifies `R=0.1`, 30 Hz, and says that 10-million-cycle survivors were **retested at the highest stress**. No specimen identifiers or runout-to-retest links are printed in Table 4. Its highest-stress failure in each group is marked only as a possible retest candidate, never treated as a confirmed link. Do not count the 20 episodes as 20 independent specimens.

The original stress column is **stress range**, not maximum or amplitude. Derived `σmax=Δσ/0.9`, `σa=Δσ/2`. The √area in Table 4 represents the killer defect determined on fracture surfaces; the paper separately reports that gauge volumes were scanned by CT before fatigue. These are different feature timings. Even when a √area is shown beside a runout, do not use Table 4's postfracture killer size as a pretest CT feature.

## Previous master and modelling gate

The previous 53-row exact master has 41 Wu first-exposure rows and 12 Romano/Tognan first-exposure rows. The latter are a re-report of Romano's underlying experiment and are not a separate study. Their six reported “runouts” are a **Tognan ≥2-million-cycle threshold class**. One of these can now be resolved: Table 1 lists specimen 3's runout at 8,889,311 cycles at Δσ=220 MPa and explicitly links the subsequent failed retest 3* at Δσ=360 MPa. Its first exposure was therefore right-censored at the observed stopping cycle; the 3* failure remains a dependent episode outside the master. The other five actual event indicators remain blank, especially where Romano Fig. 7 original filled symbols appear near samples 4 and 9. Eight Wu runouts are explicitly right-censored. Fifty-two approximate, potentially overlapping Fig. 7 glyphs remain separate from the exact master.

Chen adds 27 tabulated failures to make 80 candidate rows, with outcomes `66 failure / 9 confirmed censored / 5 unresolved`. This is a traceable candidate inventory, not a claim that 80 independent, harmonized examples suffice for any particular Q1 journal. **Synthetic rows must carry their own generation provenance, be fitted on training studies only, and never enter held-out evaluation as experimental observations.**
