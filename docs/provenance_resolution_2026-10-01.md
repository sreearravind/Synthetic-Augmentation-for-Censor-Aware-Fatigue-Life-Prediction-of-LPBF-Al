# Specimen history resolution — 2026-10-01

## Public-source checks and decision

| Source | Direct evidence | Decision |
| --- | --- | --- |
| Tognan et al. 2024, Table 1 | Sample 3: Δσ=220 MPa, N=8,889,311, “Runout”; sample 3*: Δσ=360 MPa, N=3,432, “Failed”. Table caption states starred specimens underwent earlier lower-stress testing. | Mark **sample 3 first exposure** as right-censored (`event=0`) at 8,889,311 cycles. Keep 3* outside independent master as dependent failure. |
| Tognan et al. 2024, Section 3.1 and Eq. 14 | “Runout” class is defined by N≥2×10⁶, and “failed” by N<2×10⁶ for the paper's classification problem. | Labels of samples 4, 8, 9, 10, 12 do not prove physical right-censoring. Preserve N and leave event blank. |
| Romano et al. 2018, Section 5.2 | Survivors were tested again at higher stress; post-retest fracture origins used for some defect evaluations. Fig. 7 has failure/runout symbols, but no direct specimen-to-marker key for the Tognan subset. | No further specimen event adjudication from graph coordinates alone. Samples 4 and 9 have especially suspicious proximity to filled failure symbols. |
| Roveda et al. 2024, Section 2.3 and Table 4 | Three 10⁷-cycle survivors were retested at highest stress; Table 4 gives 20 episodes without specimen IDs or linked sequence labels. | Preserve 17 failures and three runouts as **episodes**. No rows promoted to independent master. |

The Roveda and Tognan articles state that their underlying data are available on request. A check of the publisher article pages and institutional records found the articles but no public specimen-level file supplying the missing links. Absence of a located supplement is not evidence that the authors lack such records.

## Specific fields required

**Roveda:** For each Table 4 row, original specimen ID, condition (AB/HT1/HT2), test episode number and date/order, prior runout specimen ID if retested, actual stopping reason and cycle, stress range, whether the reported √area came from pretest CT or later fracture-surface inspection, and a specimen-matched pretest CT defect descriptor if shareable. The key minimum is a mapping of each of the three 10⁷-cycle runouts to its later high-stress failure.

**Romano/Tognan:** For Table 1 samples 4, 8, 9, 10 and 12, original specimen ID, stress range, reported N, whether N is failure cycle or stopped test, stop limit, any restart/retest linkage, and the corresponding Romano 2018 Fig. 7 marker or raw test row. For sample 3, confirmation of the recorded first stopping cycle and 3* pairing is welcome but no longer needed for provisional event coding.

## Request text for the researcher to send if desired

### Roveda / Serrano-Munoz

Subject: Request for specimen-level fatigue test history for AlSi10Mg study (Materials & Design 244, 113170)

Dear Dr. Serrano-Munoz,

I am compiling an attributed literature dataset for a study of censor-aware fatigue-life prediction in LPBF AlSi10Mg. Your 2024 paper reports three 10⁷-cycle runouts and states that these specimens were retested at the highest stress, while Table 4 does not show specimen IDs. Could you kindly share a specimen-level mapping between each runout and its retest, together with the original failure/censoring indicator and the test order? If available, the specimen-matched pretest CT defect measurements would also help distinguish predictive inputs from fracture-surface measurements. I would cite your paper and respect any conditions on reuse.

Sincerely,
Dr. Sreearravind Mani

### Romano / Tognan

Subject: Clarification of AlSi10Mg fatigue test outcomes for Tognan Table 1 / Romano Fig. 7

Dear Dr. Tognan,

I am constructing an attributed literature dataset for a censor-aware LPBF AlSi10Mg fatigue-life study. Your Table 1 classifies N≥2×10⁶ as “Runout”; for samples 4, 8, 9, 10 and 12, I cannot tell whether the listed N is a stopped test or a later fatigue failure. Could you kindly share the physical failure/censoring status, stopping cycle, and original specimen IDs or Romano Fig. 7 links for those five rows, including any prior or subsequent test episodes? I have kept sample 3 and its explicit 3* retest linked and separate. I would cite both the original experimental paper and your re-analysis.

Sincerely,
Dr. Sreearravind Mani

No message has been sent to the authors. These texts are prepared for the researcher's review.

## Primary sources

- [Tognan et al., CMAME 418 (2024) 116521](https://doi.org/10.1016/j.cma.2023.116521), author-hosted [PDF](https://air.uniud.it/retrieve/50eeea6f-b12b-460e-9109-fb2d960ffbe7/1-s2.0-S004578252300645X-main.pdf).
- [Romano et al., Engineering Fracture Mechanics 187 (2018) 165–189](https://doi.org/10.1016/j.engfracmech.2017.11.002).
- [Roveda et al., Materials & Design 244 (2024) 113170](https://doi.org/10.1016/j.matdes.2024.113170), [DLR record](https://elib.dlr.de/207898/).
