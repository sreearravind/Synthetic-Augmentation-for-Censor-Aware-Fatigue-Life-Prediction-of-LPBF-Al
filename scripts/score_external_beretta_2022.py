#!/usr/bin/env python3
"""Fixed-parameter Beretta external check. Run forecast, commit it, then score."""
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
    e0_logterms, median_e0, median_m1, prediction_checks,
)

COHORT = Path("data/cohorts/development_v2_199_2026-10-06.csv")
INPUT = Path("data/validation/beretta_2022_esa_external_prediction_inputs_32_2026-10-08.csv")
SOURCE = Path("data/candidates/beretta_2022_esa_cylindrical_32_specimens_40_exposures_candidate_2026-10-07.json")
PARAMS = Path("results/development_v2/romano_transfer_fit_parameters.csv")
M1 = Path("scripts/fit_m1_source_aware.py")
C0 = Path("scripts/fit_weibull_exact_baseline.py")
COMPARE = Path("scripts/compare_development_v2.py")
OUT = Path("results/external_beretta_2022_2026-10-08")
FORECAST = "forecasts_32x12.csv"
BLOBS = {
    str(COHORT): "ee9f6451e60b290c89c44f681b471b3c007c6f74",
    str(INPUT): "c0ea81a023154e09cc59577ac28f88fd50cbed5e",
    str(SOURCE): "88387a39fd4bf873272b32948ebd94ad70f615c6",
    str(PARAMS): "72bb25ca79d72effd2c2bbac4c30fffcbc80ed19",
    str(M1): "0a4fabe03bde4d0bad693cba2ac8ab4abd21ec87",
    str(C0): "921c19a8a1bac5a15a6dc557fad89ce80d46bba7",
    str(COMPARE): "f9b76f3457d4823845f3e3567131738d15236440",
}
SEEDS = (13, 29, 47, 71, 101)
TAU = 0.25
ANOMALY = "Beretta_2022:AB:FN1-245"


def blob(path):
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def checked(root, with_outcome):
    for name, expected in BLOBS.items():
        if name == str(SOURCE) and not with_outcome:
            continue
        actual = blob(root / name)
        if actual != expected:
            raise ValueError(f"Locked blob mismatch: {name} {actual}")


def read_csv(path):
    with path.open(newline="", encoding="utf-8") as stream:
        return list(csv.DictReader(stream))


def write_csv(path, rows):
    if not rows:
        raise ValueError(f"No rows for {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def inputs(root):
    rows = read_csv(root / INPUT)
    if len(rows) != 32 or len({r["specimen_key"] for r in rows}) != 32:
        raise ValueError("Expected 32 unique composite IDs")
    if Counter(r["surface_condition"] for r in rows) != {"as_built": 19, "machined": 13}:
        raise ValueError("Surface membership changed")
    if set(rows[0]) != {"specimen_key", "surface_condition", "batch",
                        "stress_range_MPa", "stress_amplitude_MPa_derived",
                        "R", "exposure_index"}:
        raise ValueError("Masked input columns changed")
    for r in rows:
        if (r["exposure_index"] != "1" or float(r["R"]) != .1
                or int(r["batch"]) not in (242, 243, 245)
                or not math.isclose(float(r["stress_range_MPa"]) / 2,
                                    float(r["stress_amplitude_MPa_derived"]), abs_tol=1e-12)):
            raise ValueError(f"Input convention changed: {r['specimen_key']}")
        if not 22.5 <= float(r["stress_amplitude_MPa_derived"]) <= 160:
            raise ValueError("External stress outside numeric support")
    cohort = read_csv(root / COHORT)
    training = [r for r in cohort if r["publication_group_id"] in
                {"Wu_2021", "Chen_2024", "Matusu_2026"}]
    if ((len(cohort), len(training),
         sum(r["failure_event_1"] == "1" for r in training),
         sum(r["failure_event_1"] == "0" for r in training)) != (199, 192, 166, 26)
            or any(float(r["stress_ratio_R"]) != .1 for r in training)
            or min(float(r["stress_amplitude_MPa"]) for r in training) != 22.5
            or max(float(r["stress_amplitude_MPa"]) for r in training) != 160
            or any("Beretta" in r["record_id"] or
                   r["source_doi"] == "10.1016/j.matdes.2022.110713" for r in cohort)):
        raise ValueError("Frozen development source membership changed")
    return rows


def fits(root):
    rows = read_csv(root / PARAMS)
    selected = [r for r in rows if r["fold"] == "Romano_2018_transfer"]
    keys = [(r["arm"], r["seed"]) for r in selected]
    expected = [("C0", ""), ("C1", "")]
    expected += [(arm, str(seed)) for seed in SEEDS for arm in ("S0", "S1")]
    if len(selected) != 12 or set(keys) != set(expected) or len(set(keys)) != 12:
        raise ValueError("Wrong archived fit membership")
    for r in selected:
        if (r["n_real"] != "192" or r["optimizer_success"] != "True"
                or r["beta_at_constraint"] != "0" or r["shape_at_constraint"] != "0"
                or any(not math.isfinite(float(r[k])) for k in
                       ("alpha", "beta", "log_shape"))):
            raise ValueError("Invalid archived fit")
    return selected


def forecast(root):
    checked(root, with_outcome=False)  # Deliberately never read the outcome file here.
    features, params = inputs(root), fits(root)
    rows = []
    for p in params:
        v = np.array([float(p[k]) for k in ("alpha", "beta", "log_shape")])
        tau = 0.0 if p["arm"] == "C0" else TAU
        for x in features:
            stress = float(x["stress_amplitude_MPa_derived"])
            median = median_e0(v, stress) if tau == 0 else median_m1(v, tau, stress)
            if not math.isfinite(median):
                raise ValueError("Nonfinite median")
            rows.append(dict(
                specimen_key=x["specimen_key"], surface_condition=x["surface_condition"],
                batch=x["batch"], stress_range_MPa=x["stress_range_MPa"],
                stress_amplitude_MPa=stress, R=x["R"],
                arm=p["arm"], seed=p["seed"], alpha=v[0], beta=v[1],
                log_shape=v[2], tau=tau, median_log10_cycles=median,
                density_measure="log10_cycles",
                source_offset_rule="none" if tau == 0 else "fresh_normal_prior",
            ))
    if len(rows) != 384:
        raise AssertionError("Forecast must be 32 x 12")
    out = root / OUT
    write_csv(out / FORECAST, rows)
    manifest = dict(
        status="forecast_saved_without_outcomes",
        locked_blobs={k: v for k, v in BLOBS.items() if k != str(SOURCE)},
        expected_outcome_blob=BLOBS[str(SOURCE)],
        script_blob=blob(Path(__file__).resolve()),
        forecast_blob=blob(out / FORECAST),
        specimen_count=32, forecast_count=384, seeds=list(SEEDS),
        tau=TAU, numerical_density_measure="log10_cycles",
        software=dict(python=platform.python_version(), numpy=np.__version__,
                      scipy=scipy.__version__),
    )
    (out / "forecast_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n",
                                                 encoding="utf-8")
    print(json.dumps({"phase": "forecast", "rows": len(rows),
                      "forecast_blob": manifest["forecast_blob"]}))


def outcomes(root, features):
    ledger = json.loads((root / SOURCE).read_text(encoding="utf-8"))
    exposures = ledger["fatigue_exposures"]
    if len(exposures) != 40:
        raise ValueError("Original exposure count changed")
    first = [r for r in exposures if r["exposure_index"] == 1 and
             r["exposure_role"] == "first_exposure"]
    by_id = {r["specimen_key"]: r for r in first}
    if (len(first) != 32 or len(by_id) != 32 or
            set(by_id) != {r["specimen_key"] for r in features}):
        raise ValueError("First-exposure ID join failed")
    for x in features:
        r = by_id[x["specimen_key"]]
        if (r["surface_condition"] != x["surface_condition"] or
                str(r["batch"]) != x["batch"] or str(r["stress_range_MPa"]) !=
                x["stress_range_MPa"] or float(r["stress_amplitude_MPa_derived"]) !=
                float(x["stress_amplitude_MPa_derived"]) or
                float(r["R"]) != float(x["R"])):
            raise ValueError(f"Keyed source-field mismatch: {x['specimen_key']}")
        event, n, op = (r["failure_event_1"], r["cycles_observed_or_bound"],
                        r["observation_operator"])
        if (event == 0 and (n != 5_000_000 or op != ">=")) or (
                event == 1 and (n <= 0 or op != "=")) or event not in (0, 1):
            raise ValueError("Invalid failure/censor operator")
    if (sum(r["failure_event_1"] for r in first) != 25 or
            sum(1-r["failure_event_1"] for r in first) != 7 or
            by_id[ANOMALY]["cycles_observed_or_bound"] != 5_600_000 or
            by_id[ANOMALY]["failure_event_1"] != 1):
        raise ValueError("Event count or printed anomaly changed")
    return by_id


def summarize(scores):
    groups = defaultdict(list)
    for r in scores:
        for name, flag in (
            ("overall_32", True),
            ("failure_25", r["event_failure"] == 1),
            ("runout_7", r["event_failure"] == 0),
            ("as_built_19", r["surface_condition"] == "as_built"),
            ("machined_13", r["surface_condition"] == "machined"),
            ("exclude_anomaly_31", r["specimen_key"] != ANOMALY),
        ):
            if flag:
                groups[(name, r["arm"], r["seed"])].append(r)
    detail = []
    counts = {"overall_32": 32, "failure_25": 25, "runout_7": 7,
              "as_built_19": 19, "machined_13": 13, "exclude_anomaly_31": 31}
    for (name, arm, seed), rs in sorted(groups.items()):
        if len(rs) != counts[name]:
            raise ValueError(f"Group membership: {name} {arm} {seed}")
        detail.append(dict(stratum=name, arm=arm, seed=seed, n=len(rs),
                           failures=sum(x["event_failure"] for x in rs),
                           runouts=sum(1-x["event_failure"] for x in rs),
                           mean_nll=sum(x["nll"] for x in rs) / len(rs),
                           mean_nll_minus_C1=sum(x["nll_minus_C1"] for x in rs) / len(rs)))
    aggregate = []
    for name in counts:
        c1 = next(r for r in detail if r["stratum"] == name and r["arm"] == "C1")
        for arm in ("C0", "C1", "S0", "S1"):
            rs = [r for r in detail if r["stratum"] == name and r["arm"] == arm]
            if len(rs) != (1 if arm in ("C0", "C1") else 5):
                raise ValueError("Missing arm/seed stratum")
            values = [r["mean_nll"] for r in rs]
            mean = sum(values) / len(values)
            aggregate.append(dict(
                stratum=name, arm=arm, n=counts[name],
                failures=rs[0]["failures"], runouts=rs[0]["runouts"],
                seed_count=len(rs), mean_nll=mean, min_seed_nll=min(values),
                max_seed_nll=max(values), mean_nll_minus_C1=mean-c1["mean_nll"],
            ))
    return detail, aggregate


def score(root):
    out = root / OUT
    manifest = json.loads((out / "forecast_manifest.json").read_text(encoding="utf-8"))
    if (manifest.get("status") != "forecast_saved_without_outcomes"
            or manifest.get("script_blob") != blob(Path(__file__).resolve())
            or manifest.get("forecast_blob") != blob(out / FORECAST)
            or manifest.get("expected_outcome_blob") != BLOBS[str(SOURCE)]
            or manifest.get("locked_blobs") !=
            {k: v for k, v in BLOBS.items() if k != str(SOURCE)}):
        raise ValueError("Forecast-phase identity gate failed")
    checked(root, with_outcome=True)
    features, parameter_rows = inputs(root), fits(root)
    by_id = outcomes(root, features)
    forecasts = read_csv(out / FORECAST)
    if len(forecasts) != 384 or len({(f["specimen_key"], f["arm"], f["seed"])
                                     for f in forecasts}) != 384:
        raise ValueError("Forecast shape/unique keys changed")
    by_fit = defaultdict(list)
    for f in forecasts:
        by_fit[(f["arm"], f["seed"])].append(f)
    baseline = {}
    scores = []
    for p in parameter_rows:
        arm, seed = p["arm"], p["seed"]
        rows = by_fit[(arm, seed)]
        if len(rows) != 32 or {r["specimen_key"] for r in rows} != set(by_id):
            raise ValueError("Missing forecast ID")
        for f in rows:
            x = next(x for x in features if x["specimen_key"] == f["specimen_key"])
            if (f["surface_condition"] != x["surface_condition"] or
                    f["batch"] != x["batch"] or
                    f["stress_range_MPa"] != x["stress_range_MPa"] or
                    float(f["stress_amplitude_MPa"]) !=
                    float(x["stress_amplitude_MPa_derived"]) or
                    float(f["R"]) != float(x["R"]) or
                    f["density_measure"] != "log10_cycles" or
                    f["source_offset_rule"] !=
                    ("none" if arm == "C0" else "fresh_normal_prior") or
                    any(float(f[k]) != float(p[k]) for k in
                        ("alpha", "beta", "log_shape")) or
                    float(f["tau"]) != (0. if arm == "C0" else TAU)):
                raise ValueError("Forecast/input/fit identity changed")
        v = np.array([float(p[k]) for k in ("alpha", "beta", "log_shape")])
        stress = np.array([float(f["stress_amplitude_MPa"]) for f in rows])
        cycles = np.array([by_id[f["specimen_key"]]["cycles_observed_or_bound"]
                           for f in rows])
        event = np.array([by_id[f["specimen_key"]]["failure_event_1"]
                          for f in rows])
        if arm == "C0":
            logterms, delta = e0_logterms(v, stress, cycles, event), 0.
        else:
            logterms, delta = prediction_checks(v, TAU, stress, cycles, event)
        if delta > 1e-5 or np.any(~np.isfinite(logterms)):
            raise ValueError("Numerical prediction instability")
        for f, n, e, logterm in zip(rows, cycles, event, logterms):
            key = f["specimen_key"]
            q = dict(specimen_key=key, surface_condition=f["surface_condition"],
                     batch=f["batch"], stress_range_MPa=f["stress_range_MPa"],
                     stress_amplitude_MPa=f["stress_amplitude_MPa"],
                     arm=arm, seed=seed, observed_cycles_or_bound=int(n),
                     event_failure=int(e), observation_operator=
                     by_id[key]["observation_operator"], log_likelihood=float(logterm),
                     nll=-float(logterm), quadrature_max_delta=delta)
            if arm == "C1":
                baseline[key] = q["nll"]
            scores.append(q)
    if len(baseline) != 32 or len(scores) != 384:
        raise ValueError("Missing comparator or score")
    for r in scores:
        r["nll_minus_C1"] = r["nll"] - baseline[r["specimen_key"]]
    write_csv(out / "scores_per_record.csv", scores)
    detail, aggregate = summarize(scores)
    write_csv(out / "scores_by_arm_seed_stratum.csv", detail)
    write_csv(out / "summary.csv", aggregate)
    meta = dict(
        status="scored_fixed_model_external_one_campaign",
        forecast_blob=manifest["forecast_blob"],
        forecast_manifest_blob=blob(out / "forecast_manifest.json"),
        candidate_blob=BLOBS[str(SOURCE)],
        scores_blob=blob(out / "scores_per_record.csv"),
        detail_blob=blob(out / "scores_by_arm_seed_stratum.csv"),
        summary_blob=blob(out / "summary.csv"),
        unique_first_exposures=32, failures=25, right_censored=7,
        excluded_later_exposures=8, anomaly_sensitivity_n=31,
        max_quadrature_delta=max(r["quadrature_max_delta"] for r in scores),
        no_refit=True, no_external_source_offset_update=True,
        outcomes_inspected_at_intake=True, independent_publications=1,
    )
    (out / "score_manifest.json").write_text(json.dumps(meta, indent=2) + "\n",
                                             encoding="utf-8")
    print(json.dumps({"phase": "score", "overall": [r for r in aggregate
                                                   if r["stratum"] == "overall_32"],
                      "quadrature_max_delta": meta["max_quadrature_delta"]}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("phase", choices=("forecast", "score"))
    parser.add_argument("--root", type=Path, default=Path("."))
    args = parser.parse_args()
    if args.phase == "forecast":
        forecast(args.root.resolve())
    else:
        score(args.root.resolve())
