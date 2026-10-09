# Beretta 2022 ESA: fixed-model external outcome-and-runout comparison

**Date:** 8 October 2026. Completed the [pre-score overlap and role lock](beretta_2022_esa_overlap_and_external_role_lock_2026-10-08.md) with **no refit or Beretta study-offset update**. This is a prediction-before-score comparison on a source whose outcomes were inspected at extraction; it is one external experimental campaign, not a blind prospective trial.

## Execution and integrity

The [masked input](../data/validation/beretta_2022_esa_external_prediction_inputs_32_2026-10-08.csv) contains 32 unique first-exposure composite IDs with no outcome column. Forecasts were generated from the archived [192-row R=0.1 fits](../results/development_v2/romano_transfer_fit_parameters.csv) and saved as [384 fixed distributions and medians](../results/external_beretta_2022_2026-10-08/forecasts_32x12.csv), blob `733a84a7c66ddb11a90a4360fb58be337e0e7487`. The [forecast manifest](../results/external_beretta_2022_2026-10-08/forecast_manifest.json), blob `61f2d76bfc01592baaf19a17e93a52daa47a794b`, and the [scorer](../scripts/score_external_beretta_2022.py), blob `4e748a37563cd48a1fa603440f682d0f4fc137d8`, were committed and read back **before** joining the candidate outcome file. The scorer's forecast phase excludes that candidate file from its file checks and does not open it.

The subsequent exact join required agreement on composite specimen ID, surface, batch, stress range Δσ, derived amplitude Δσ/2 and R=0.1. It verified 40 source-table exposures, retained 32 first exposures (25 failures and seven `≥5×10^6` runouts), and excluded eight retest exposures. All 32 stress amplitudes (22.5–105 MPa) are within the numerical 22.5–160 MPa training stress span. The 5×10^6 runout bound is documented in the main article and inherited for supplement rows marked run-out. The reported 5.6×10^6 **failure** of AB:FN1-245 was kept verbatim, with the prespecified exclusion sensitivity below.

There are [384 per-specimen scores](../results/external_beretta_2022_2026-10-08/scores_per_record.csv), [72 arm/seed/stratum scores](../results/external_beretta_2022_2026-10-08/scores_by_arm_seed_stratum.csv), a [summary](../results/external_beretta_2022_2026-10-08/summary.csv) and a [score manifest](../results/external_beretta_2022_2026-10-08/score_manifest.json). All uploads were read back against local Git blobs. Maximum difference between 161- and 321-node predictive log likelihoods was `1.78×10^-15`, below the locked `10^-5` threshold. C0 uses no study offset; C1/S0/S1 integrate a fresh prior offset with fixed τ=0.25.

## Fixed comparison

The metric is mean negative **natural log** likelihood: density of observed `log10(N)` for failures, survival at the recorded bound for runouts. Lower is better. S0/S1 are averages across the five predetermined seeds, each a stochastic fit of the same 192 experimental training rows, not five external campaigns. The Δ column is mean NLL minus C1 in the same stratum.

| Stratum | n (fail/runout) | C0 | C1 | S0 mean (Δ vs C1) | S1 mean (Δ vs C1) |
| --- | ---: | ---: | ---: | ---: | ---: |
| **All first exposures** | 32 (25/7) | 1.55455 | **1.48670** | 1.48490 (−0.00180) | 1.48624 (−0.00046) |
| Failures, density | 25 (25/0) | 1.44968 | 1.45581 | 1.45627 (+0.00046) | 1.45568 (−0.00012) |
| Runouts, survival | 7 (0/7) | 1.92912 | 1.59703 | 1.58715 (−0.00988) | 1.59535 (−0.00169) |
| As-built, descriptive | 19 (15/4) | 1.43020 | 1.44049 | 1.44186 (+0.00137) | 1.44044 (−0.00004) |
| Machined, descriptive | 13 (10/3) | 1.73630 | 1.55425 | 1.54781 (−0.00643) | 1.55316 (−0.00108) |
| **Exclude flagged failure** | 31 (24/7) | 1.57528 | **1.50366** | 1.50172 (−0.00194) | 1.50317 (−0.00049) |

No arm was refitted for the 31-row sensitivity. The five seed scores on all 32 observations are:

| Seed | S0 | S1 |
| ---: | ---: | ---: |
| 13 | 1.48342 | 1.48518 |
| 29 | 1.48650 | 1.48584 |
| 47 | 1.48735 | 1.48682 |
| 71 | 1.48654 | 1.48702 |
| 101 | 1.48070 | 1.48632 |
| **Five-seed mean** | **1.48490** | **1.48624** |
| **Range** | **1.48070–1.48735** | **1.48518–1.48702** |

## Interpretation and next decision

C1 is 0.06785 NLL lower than C0 overall. Its runout NLL is 0.33208 lower, while its failure NLL is 0.00613 higher. S0's 0.00180 aggregate reduction relative to C1 combines a small runout improvement with **slightly worse failure density**; S1 changes the aggregate by only 0.00046. S0 seeds 47 and 71, and S1 seed 71, score worse than C1 overall. The anomalous failure's exclusion does not materially change that pattern. These are descriptive observations on **one** publication; no superiority test or claim of learned synthetic-data utility is supported. The earlier three-publication development comparison did not meet its predeclared S1 advantage rule, and these Beretta results do not reverse that finding.

The locked model uses stress amplitude alone. Finish and batch are audit strata, not fitted features; roughness values may reflect outcome-dependent selection near fracture origins and were excluded. This check adds a documented **R=0.1 external censor test** with 5×10^6 bounds to the existing failure-only Al-Zuhairi transfer check, but cannot establish specimen-level feature prediction or algorithm novelty. The next manuscript decision should evaluate whether the defensible contribution is a transparent negative/limits study of stress-only synthetic augmentation, or whether a genuinely pretest feature cohort and a method adding information beyond self-distillation can be obtained. Do not tune on this now-scored campaign and present it again as untouched validation.
