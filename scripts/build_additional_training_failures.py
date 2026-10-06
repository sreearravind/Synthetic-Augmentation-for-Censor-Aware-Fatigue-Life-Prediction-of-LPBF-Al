#!/usr/bin/env python3
"""Convert audited vector glyph candidates to conservative graph-derived failure rows.

Requires the two candidate JSON files produced by inspect_muhammad_fernandes_vectors.py.
This does not read or score any reserved external campaign or fit any model.
"""
import argparse
import csv
import json
import math
from collections import Counter, defaultdict
from pathlib import Path

MU_HOLD = {
    "MU03": "obscured_by_same_level_red_cluster",
    "MU07": "obscured_by_same_level_red_cluster",
    "MU11": "unresolved_same_series_overlap",
    "MU12": "unresolved_same_series_overlap",
    **{f"MU{i:02d}": "unresolved_same_series_overlap" for i in range(19, 29)},
    **{f"MU{i:02d}": "unresolved_same_series_overlap" for i in (37, 38, 39, 40, 41, 42)},
    "MU18": "right_axis_boundary_outcome_unverified",
    "MU31": "right_axis_boundary_outcome_unverified",
    "MU50": "right_axis_boundary_outcome_unverified",
}
FE_HOLD = {
    "FE06": "arrow_runout_stop_unverified",
    "FE07": "arrow_runout_stop_unverified",
    "FE17": "arrow_runout_stop_unverified",
    "FE27": "arrow_runout_stop_unverified",
    **{f"FE{i:02d}": "overprinted_cross_series_outcome_unresolved" for i in (12, 13, 14, 23, 24, 25)},
}
SOURCE = {
    "Muhammad_2023": {
        "doi": "10.1016/j.ijfatigue.2023.107965",
        "figure": "Figure 10", "pdf_page": 10,
        "pdf_sha256": "67bfaaec15604e8cebd55a16d5e3b2ba23d72a1951af0e64b644fd815e5de797",
        "calibration": "x 146.943=1e4, 457.148=1e7; y 289.144=0 MPa, 5.0552 pt per 10 MPa",
        "hold": MU_HOLD, "delta_pdf_pt": 0.5,
        "ratio": {"AB_R01": .1, "AB_Rm1": -1, "CMP_R01": .1, "CMP_Rm1": -1},
        "condition": {"AB_R01": "as-built", "AB_Rm1": "as-built", "CMP_R01": "as-built plus chemo-mechanical polishing", "CMP_Rm1": "as-built plus chemo-mechanical polishing"},
        "freq_hz": 40,
    },
    "Fernandes_2024": {
        "doi": "10.1016/j.tafmec.2024.104553",
        "figure": "Figure 5 smooth only", "pdf_page": 5,
        "pdf_sha256": "f4cd15a5fd6ca9613b30dfda6bfe5dbebf78c47b9d201bc157c46e1f286570c3",
        "calibration": "x 73.832=1e4, 278.284=1e7; log-y 525.6605=200 MPa, 606.4665=100 MPa",
        "hold": FE_HOLD, "delta_pdf_pt": 0.5,
        "ratio": {"AB": 0, "SR": 0, "HIP": 0},
        "condition": {"AB": "as-built", "SR": "stress relieved", "HIP": "hot isostatic pressed"},
        "freq_hz": 20,
    },
}

def values(src, x, y):
    if src == "Muhammad_2023":
        log_n = 4 + 3 * (x - 146.943) / (457.148 - 146.943)
        delta = (289.144 - y) * 10 / 5.0552
    else:
        log_n = 4 + 3 * (x - 73.832) / (278.284 - 73.832)
        delta = 100 * math.exp((606.4665 - y) * math.log(2) / (606.4665 - 525.6605))
    return log_n, delta / 2

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--candidates", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    a.out.mkdir(parents=True, exist_ok=True)
    audit, included = [], []
    for source, cfg in SOURCE.items():
        for row in json.loads((a.candidates / f"{source}_vector_candidates.json").read_text()):
            assert row["source"] == source
            ident = row["candidate_id"]
            x, y = row["pdf_x"], row["pdf_y"]
            half_x = row["glyph_halfwidth_pdf_pt"] + cfg["delta_pdf_pt"]
            half_y = row["glyph_halfheight_pdf_pt"] + cfg["delta_pdf_pt"]
            log_n, amplitude = values(source, x, y)
            lo_n, _ = values(source, x - half_x, y)
            hi_n, _ = values(source, x + half_x, y)
            _, lo_amp = values(source, x, y + half_y)
            _, hi_amp = values(source, x, y - half_y)
            reason = cfg["hold"].get(ident, "clear_first_exposure_failure_symbol")
            decision = "include_failure" if reason == "clear_first_exposure_failure_symbol" else "hold"
            common = dict(record_id=f"{source}_{ident}", source=source, doi=cfg["doi"],
                pdf_sha256=cfg["pdf_sha256"], figure=cfg["figure"], pdf_page=cfg["pdf_page"],
                candidate_id=ident, series=row["series"], condition=cfg["condition"][row["series"]],
                stress_ratio_R=cfg["ratio"][row["series"]], loading="axial", test_frequency_hz=cfg["freq_hz"],
                source_y_quantity="stress range Delta_sigma MPa", source_x_quantity="number of cycles",
                stress_amplitude_mpa=round(amplitude, 2), stress_amplitude_low_mpa=round(lo_amp, 2),
                stress_amplitude_high_mpa=round(hi_amp, 2), log10_cycles=round(log_n, 4),
                log10_cycles_low=round(lo_n, 4), log10_cycles_high=round(hi_n, 4),
                pdf_x=round(x, 4), pdf_y=round(y, 4), vector_sequence=row["drawing_sequence"],
                reading_method="PDF vector glyph center plus visual symbol/arrow audit",
                interval_method="glyph half-size plus 0.5 PDF pt calibration allowance on each axis; not a statistical CI",
                axis_calibration=cfg["calibration"], decision=decision, reason=reason)
            audit.append(common)
            if decision == "include_failure":
                included.append({k:v for k,v in common.items() if k not in ("decision", "reason")}
                    | {"event":1, "censoring":"failure", "source_precision_tier":"graph_derived",
                       "training_role":"candidate_training_only", "specimen_identity":"plotted_glyph_unlinked_to_specimen_id"})
    assert len(audit) == 88
    assert not any(r["source"] in ("Strauss_Lowisch_2024", "Kempf_2022") for r in audit)
    assert all(r["event"] == 1 for r in included)
    assert all(r["stress_amplitude_low_mpa"] <= r["stress_amplitude_mpa"] <= r["stress_amplitude_high_mpa"] for r in included)
    assert all(r["log10_cycles_low"] <= r["log10_cycles"] <= r["log10_cycles_high"] for r in included)
    for fname, rows in (("additional_training_symbol_audit_2026-10-06.csv",audit),
                        ("additional_training_failures_2026-10-06.csv",included)):
        with (a.out/fname).open("w",newline="") as f:
            writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
    print("audit", len(audit), dict(Counter((r["source"],r["decision"]) for r in audit)))
    print("included", len(included), dict(Counter((r["source"],r["series"]) for r in included)))
    print("holds", dict(Counter(r["reason"] for r in audit if r["decision"] == "hold")))

if __name__ == "__main__":main()
