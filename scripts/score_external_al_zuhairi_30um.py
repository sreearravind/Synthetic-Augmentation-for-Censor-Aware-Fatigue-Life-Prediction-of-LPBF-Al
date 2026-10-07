#!/usr/bin/env python3
"""Two-phase, frozen-parameter external score for Al-Zuhairi 30 um records.

Forecast writes a distribution representation without reading fatigue lives.
Score requires that saved forecast and joins exact source outcomes by ID.
Run from the repository root:
  python scripts/score_external_al_zuhairi_30um.py forecast --root .
  python scripts/score_external_al_zuhairi_30um.py score --root .
"""
import argparse
import csv
import hashlib
import json
import math
import platform
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np
import scipy

from fit_m1_source_aware import (
    CHECK_NODES, FIT_NODES, e0_logterms, median_e0, median_m1,
    prediction_checks,
)

COHORT = Path("data/cohorts/development_v2_199_2026-10-06.csv")
INPUT = Path("data/validation/al_zuhairi_2026_30um_external_prediction_inputs_23_2026-10-07.csv")
SOURCE = Path("data/candidates/al_zuhairi_2026_s1_s6_35_exact_outcome_candidate_2026-10-07.csv")
PARAMS = Path("results/development_v2/romano_transfer_fit_parameters.csv")
COMPARE = Path("scripts/compare_development_v2.py")
HELPER_M1 = Path("scripts/fit_m1_source_aware.py")
HELPER_C0 = Path("scripts/fit_weibull_exact_baseline.py")
OUT = Path("results/external_al_zuhairi_30um_2026-10-07")
FORECAST = "forecasts_23x12.csv"
MANIFEST = "forecast_manifest.json"
BLOBS = {
    str(COHORT): "ee9f6451e60b290c89c44f681b471b3c007c6f74",
    str(INPUT): "5079cdebfe22f6a6a57311c18e1487723c7ee7e1",
    str(SOURCE): "3847d10f768ee695fff8c2d22f13c73fc8a2af1d",
    str(PARAMS): "72bb25ca79d72effd2c2bbac4c30fffcbc80ed19",
    str(COMPARE): "f9b76f3457d4823845f3e3567131738d15236440",
    str(HELPER_M1): "0a4fabe03bde4d0bad693cba2ac8ab4abd21ec87",
    str(HELPER_C0): "921c19a8a1bac5a15a6dc557fad89ce80d46bba7",
}
SEEDS = (13, 29, 47, 71, 101)
GROUPS = {"30um_V_AB": 5, "30um_V_T6": 6, "30um_H_T6": 6, "30um_45_T6": 6}
TAU = 0.25


def blob(path):
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def read(path):
    with path.open(newline="", encoding="utf-8") as stream:
        return list(csv.DictReader(stream))


def write(path, rows):
    if not rows:
        raise ValueError(f"Empty output: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def files_check(root, include_source):
    for name, expected in BLOBS.items():
        if not include_source and name == str(SOURCE):
            continue  # Forecast must not open the outcome ledger.
        actual = blob(root / name)
        if actual != expected:
            raise ValueError(f"Locked blob changed: {name}: {actual}")


def inputs_check(root):
    inputs = read(root / INPUT)
    if len(inputs) != 23 or len({r["prediction_id"] for r in inputs}) != 23:
        raise ValueError("External IDs/count changed")
    if Counter(r["condition"] for r in inputs) != Counter(GROUPS):
        raise ValueError("External condition membership changed")
    if any(r["layer_thickness_um_audit_only"] != "30"
           or r["stress_ratio_R_audit_only"] != "-1"
           or r["within_train_stress_range"] != "1"
           or r["publication_group_id"] != "AlZuhairi_2026"
           or float(r["stress_amplitude_MPa"]) <= 0 for r in inputs):
        raise ValueError("External feature/provenance contract failed")
    if any(set(r) & {"observed_cycles_NB", "event_failure", "cycles_failure_or_bound"}
           for r in inputs):
        raise ValueError("Outcome column leaked into prediction input")
    training = [r for r in read(root / COHORT)
                if r["publication_group_id"] in {"Wu_2021", "Chen_2024", "Matusu_2026"}]
    if (len(training), sum(r["failure_event_1"] == "1" for r in training),
        sum(r["failure_event_1"] == "0" for r in training)) != (192, 166, 26):
        raise ValueError("Training membership changed")
    if any(float(r["stress_ratio_R"]) != .1 for r in training):
        raise ValueError("Training R changed")
    lo = min(float(r["stress_amplitude_MPa"]) for r in training)
    hi = max(float(r["stress_amplitude_MPa"]) for r in training)
    if (lo, hi) != (22.5, 160.0):
        raise ValueError("Training stress range changed")
    if any(not lo <= float(r["stress_amplitude_MPa"]) <= hi for r in inputs):
        raise ValueError("External stress support changed")
    return inputs


def fit_rows_check(root):
    rows = read(root / PARAMS)
    selected = [r for r in rows if r["fold"] == "Romano_2018_transfer"]
    keys = [(r["arm"], r["seed"]) for r in selected]
    expected = [("C0", ""), ("C1", "")]
    expected += [(arm, str(seed)) for seed in SEEDS for arm in ("S0", "S1")]
    if len(selected) != 12 or len(set(keys)) != 12 or set(keys) != set(expected):
        raise ValueError("Archived full-192 parameter membership changed")
    for r in selected:
        if (r["n_real"] != "192" or r["optimizer_success"] != "True"
                or r["beta_at_constraint"] != "0"
                or r["shape_at_constraint"] != "0"):
            raise ValueError(f"Invalid archived fit: {r['arm']} {r['seed']}")
        if any(not math.isfinite(float(r[k])) for k in ("alpha", "beta", "log_shape")):
            raise ValueError("Nonfinite parameter")
    return selected


def forecast(root):
    files_check(root, include_source=False)
    inputs = inputs_check(root)
    fits = fit_rows_check(root)
    script_path = Path(__file__).resolve()
    out = root / OUT
    out.mkdir(parents=True, exist_ok=True)
    rows = []
    for fit in fits:
        params = np.array([float(fit[k]) for k in ("alpha", "beta", "log_shape")])
        arm, seed = fit["arm"], fit["seed"]
        tau = 0. if arm == "C0" else TAU
        for item in inputs:
            stress = float(item["stress_amplitude_MPa"])
            median = (median_e0(params, stress) if arm == "C0"
                      else median_m1(params, tau, stress))
            if not math.isfinite(median):
                raise ValueError("Nonfinite forecast")
            rows.append(dict(
                prediction_id=item["prediction_id"],
                original_specimen_id=item["original_specimen_id"],
                condition=item["condition"],
                source_file=item["source_file"],
                source_row_1based=item["source_row_1based"],
                stress_amplitude_MPa=stress,
                stress_ratio_R_audit_only=item["stress_ratio_R_audit_only"],
                arm=arm, seed=seed, alpha=params[0], beta=params[1],
                log_shape=params[2], tau=tau,
                median_log10_cycles=median,
                density_measure="log10_cycles",
                offset_rule="none" if arm == "C0" else "fresh_normal_prior",
            ))
    if len(rows) != 276:
        raise AssertionError("Forecast shape")
    write(out / FORECAST, rows)
    metadata = dict(
        status="forecast_saved_without_outcomes",
        cohort="one_preprint_23_30um_failures",
        locked_blobs={k: v for k, v in BLOBS.items() if k != str(SOURCE)},
        expected_outcome_blob=BLOBS[str(SOURCE)],
        forecast_blob=blob(out / FORECAST),
        script_blob=blob(script_path),
        n_specimens=len(inputs), n_distributions=len(fits),
        n_forecasts=len(rows), arms=["C0", "C1", "S0", "S1"],
        seeds=list(SEEDS), offset_tau=TAU, training_R=.1, external_R=-1,
        software=dict(python=platform.python_version(), numpy=np.__version__,
                      scipy=scipy.__version__),
    )
    (out / MANIFEST).write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(dict(phase="forecast", rows=len(rows),
                          blob=metadata["forecast_blob"])))


def keyed_outcomes(root, inputs):
    source = read(root / SOURCE)
    if len(source) != 35 or len({r["original_specimen_id"] for r in source}) != 35:
        raise ValueError("Source ledger not 35 unique IDs")
    by_id = {r["original_specimen_id"]: r for r in source}
    expected = {r["original_specimen_id"] for r in inputs}
    if len(expected) != 23 or not expected <= set(by_id):
        raise ValueError("Exact specimen join failed")
    outcomes = {}
    for item in inputs:
        key = item["original_specimen_id"]
        r = by_id[key]
        for src, inp in (("source_file", "source_file"),
                         ("source_row_1based", "source_row_1based"),
                         ("condition", "condition"),
                         ("stress_amplitude_MPa", "stress_amplitude_MPa")):
            if r[src] != item[inp]:
                raise ValueError(f"Keyed source mismatch: {key} {src}")
        if (r["layer_thickness_um"] != "30" or r["event_failure"] != "1"
                or r["censor_bound_cycles"] or r["cohort_status"] != "candidate_only"
                or r["publication_overlap_status"]
                   != "distinct_process_from_Lehner_2024_30um_only"):
            raise ValueError(f"Unexpected outcome status: {key}")
        cycles = int(r["observed_cycles_NB"])
        if cycles <= 0:
            raise ValueError(f"Invalid failure life: {key}")
        outcomes[key] = cycles
    return outcomes


def score(root):
    out = root / OUT
    meta = json.loads((out / MANIFEST).read_text(encoding="utf-8"))
    if (meta.get("status") != "forecast_saved_without_outcomes"
            or meta.get("script_blob") != blob(Path(__file__).resolve())
            or meta.get("forecast_blob") != blob(out / FORECAST)
            or meta.get("expected_outcome_blob") != BLOBS[str(SOURCE)]):
        raise ValueError("Forecast phase/hash gate failed")
    files_check(root, include_source=True)
    inputs = inputs_check(root)
    fit_rows_check(root)
    forecast_rows = read(out / FORECAST)
    if len(forecast_rows) != 276:
        raise ValueError("Forecast row count changed")
    expected_keys = {(r["prediction_id"], r["arm"], r["seed"])
                     for r in forecast_rows}
    if len(expected_keys) != 276:
        raise ValueError("Forecast key duplication")
    outcomes = keyed_outcomes(root, inputs)
    scores = []
    forecasts_by_arm = defaultdict(list)
    for f in forecast_rows:
        forecasts_by_arm[(f["arm"], f["seed"])].append(f)
    if len(forecasts_by_arm) != 12:
        raise ValueError("Incomplete forecast arms")
    for (arm, seed), fs in forecasts_by_arm.items():
        if len(fs) != 23:
            raise ValueError("Incomplete forecast IDs")
        params = np.array([float(fs[0][k]) for k in ("alpha", "beta", "log_shape")])
        if any(any(float(f[k]) != params[j] for j, k in
                   enumerate(("alpha", "beta", "log_shape"))) for f in fs):
            raise ValueError("Inconsistent parameters within arm")
        stresses = np.array([float(f["stress_amplitude_MPa"]) for f in fs])
        lives = np.array([outcomes[f["original_specimen_id"]] for f in fs])
        events = np.ones(23, dtype=int)
        if arm == "C0":
            logdensities = e0_logterms(params, stresses, lives, events)
            delta = 0.
        else:
            logdensities, delta = prediction_checks(
                params, TAU, stresses, lives, events)
        for f, cycles, log_density in zip(fs, lives, logdensities):
            med = float(f["median_log10_cycles"])
            log_density = float(log_density)
            if not math.isfinite(log_density) or delta > 1e-5:
                raise ValueError("Numerical score invalid")
            bias = med - math.log10(int(cycles))
            scores.append(dict(
                prediction_id=f["prediction_id"], original_specimen_id=f["original_specimen_id"],
                condition=f["condition"], arm=arm, seed=seed,
                stress_amplitude_MPa=float(f["stress_amplitude_MPa"]),
                observed_failure_cycles=int(cycles),
                event_failure=1, log_density_log10_cycles=log_density,
                nll_log10_life_density=-log_density,
                median_log10_cycles=med, signed_error_log10=bias,
                abs_error_log10=abs(bias), quadrature_max_delta=delta,
            ))
    if len(scores) != 276:
        raise AssertionError("Score shape")
    write(out / "scores_per_record.csv", scores)
    grouped = defaultdict(list)
    for r in scores:
        for condition in ("overall_23", r["condition"]):
            grouped[(condition, r["arm"], r["seed"])].append(r)
    details = []
    for (condition, arm, seed), rs in sorted(grouped.items()):
        expected_n = 23 if condition == "overall_23" else GROUPS[condition]
        if len(rs) != expected_n:
            raise AssertionError("Group count")
        details.append(dict(
            condition=condition, arm=arm, seed=seed, n=len(rs),
            mean_nll=sum(float(x["nll_log10_life_density"]) for x in rs)/len(rs),
            mean_abs_error_log10=sum(float(x["abs_error_log10"]) for x in rs)/len(rs),
            mean_signed_error_log10=sum(float(x["signed_error_log10"]) for x in rs)/len(rs),
        ))
    write(out / "scores_by_arm_seed_condition.csv", details)
    summaries = []
    for condition in ("overall_23", *GROUPS):
        d = [r for r in details if r["condition"] == condition]
        c1 = next(r for r in d if r["arm"] == "C1")
        for arm in ("C0", "C1", "S0", "S1"):
            z = [r for r in d if r["arm"] == arm]
            assert len(z) == (1 if arm in ("C0", "C1") else 5)
            v = [float(r["mean_nll"]) for r in z]
            summaries.append(dict(
                condition=condition, arm=arm, n=int(z[0]["n"]),
                number_of_seeds=len(z), mean_nll=sum(v)/len(v),
                min_seed_mean_nll=min(v), max_seed_mean_nll=max(v),
                mean_nll_minus_C1=sum(v)/len(v)-float(c1["mean_nll"]),
                mean_abs_error_log10=sum(float(r["mean_abs_error_log10"]) for r in z)/len(z),
                mean_signed_error_log10=sum(float(r["mean_signed_error_log10"]) for r in z)/len(z),
            ))
    write(out / "summary.csv", summaries)
    result = dict(
        status="scored_as_locked_external_outcome_only",
        forecast_blob=meta["forecast_blob"], forecast_manifest_blob=blob(out / MANIFEST),
        outcome_blob=BLOBS[str(SOURCE)], score_blob=blob(out / "scores_per_record.csv"),
        score_count=len(scores), unique_specimens=len(outcomes),
        event_failures=23, documented_runouts=0,
        max_quadrature_difference=max(float(r["quadrature_max_delta"]) for r in scores),
        no_training_or_recalibration=True, no_source_offset_update=True,
        one_preprint_publication=True, interpretation="R_shift_failure_life_transfer_only",
    )
    (out / "score_manifest.json").write_text(json.dumps(result, indent=2) + "\n",
                                              encoding="utf-8")
    print(json.dumps(dict(phase="score", n=23, summaries=[
        {k: r[k] for k in ("arm", "mean_nll", "mean_nll_minus_C1")}
        for r in summaries if r["condition"] == "overall_23"])))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("phase", choices=("forecast", "score"))
    parser.add_argument("--root", type=Path, default=Path("."))
    args = parser.parse_args()
    root = args.root.resolve()
    if args.phase == "forecast":
        forecast(root)
    else:
        score(root)


if __name__ == "__main__":
    main()
