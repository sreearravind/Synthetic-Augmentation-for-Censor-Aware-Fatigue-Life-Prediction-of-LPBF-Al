"""Reconcile independent vector and raster symbol readings, without model access."""
import argparse
import json
from collections import Counter
from pathlib import Path

import numpy as np
from scipy.optimize import linear_sum_assignment

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--readings-dir', type=Path, required=True, help='Directory produced by read_nasab_fig10.py')
args = parser.parse_args()
BASE = args.readings_dir.resolve()
A = json.loads((BASE / "reader_A_vector.json").read_text())
B = json.loads((BASE / "reader_B_raster.json").read_text())

# Figure axes taken independently from visible tick intersections, then
# expressed in PDF points (the rendered clip starts at 130,540 and is 5x).
X_1E4, X_1E7 = 187.0, 434.2
Y_300, Y_0 = 547.6, 711.4
DECADE_PT = (X_1E7 - X_1E4) / 3
MPA_PT = 300 / (Y_0 - Y_300)
R = 0.1
GLYPH_HALF_PT = 1.92
LOG_SPAN = GLYPH_HALF_PT / DECADE_PT
STRESS_SPAN = GLYPH_HALF_PT * MPA_PT

match = {}
for group in ("VF", "SB", "MP"):
    ai = [i for i, q in enumerate(A) if q["group"] == group]
    bi = [i for i, q in enumerate(B) if q["group"] == group]
    cost = np.array([
        [np.hypot(A[i]["pixel_x"] - B[j]["pixel_x"], A[i]["pixel_y"] - B[j]["pixel_y"])
         for j in bi]
        for i in ai
    ])
    row, col = linear_sum_assignment(cost)
    for u, v in zip(row, col):
        if cost[u, v] <= 3.2:
            match[ai[u]] = (bi[v], round(float(cost[u, v]), 3))

records = []
for group in ("VF", "SB", "MP"):
    indexed = [(i, q) for i, q in enumerate(A) if q["group"] == group]
    for ordinal, (i, q) in enumerate(sorted(indexed, key=lambda z: (z[1]["pdf_x"], z[1]["pdf_y"])), 1):
        logn = 4 + (q["pdf_x"] - X_1E4) / DECADE_PT
        stress = (Y_0 - q["pdf_y"]) * MPA_PT
        is_runout = abs(q["pdf_x"] - 409.435) < 0.02
        bidx, delta = match.get(i, (None, None))
        independent = bidx is not None
        if is_runout:
            # The source method fixes the stopping cycle. Horizontal marker
            # width is not a range of failure times for a right-censored test.
            life = 5_000_000
            lower_life = upper_life = 5_000_000
        else:
            life = round(10 ** logn)
            lower_life = round(10 ** (logn - LOG_SPAN))
            upper_life = round(10 ** (logn + LOG_SPAN))
        records.append({
            "record_id": f"HN2019_{group}_{ordinal:02d}",
            "source_doi": "10.3390/met9101063",
            "figure": "Figure 10, PDF page 10",
            "finish": {"VF": "vibrofinished", "SB": "sandblasted", "MP": "machined and polished"}[group],
            "marker": {"VF": "blue open triangle", "SB": "black open diamond", "MP": "red open circle"}[group],
            "event": "runout" if is_runout else "failure",
            "censor_operator": ">=" if is_runout else "=",
            "sigma_max_mpa_center": round(stress, 2),
            "sigma_max_mpa_low": round(stress - STRESS_SPAN, 2),
            "sigma_max_mpa_high": round(stress + STRESS_SPAN, 2),
            "stress_ratio_R": R,
            "sigma_amplitude_mpa_center": round(0.45 * stress, 2),
            "sigma_amplitude_mpa_low": round(0.45 * (stress - STRESS_SPAN), 2),
            "sigma_amplitude_mpa_high": round(0.45 * (stress + STRESS_SPAN), 2),
            "cycles_center_or_stop": life,
            "cycles_glyph_low": lower_life,
            "cycles_glyph_high": upper_life,
            "log10_cycles_glyph_halfwidth": None if is_runout else round(LOG_SPAN, 5),
            "reader_A_pdf_x": q["pdf_x"],
            "reader_A_pdf_y": q["pdf_y"],
            "reader_A_vector_objects": q["object_count"],
            "reader_A_sequences": ",".join(map(str, q["sequences"])),
            "reader_B_pixel_x": B[bidx]["pixel_x"] if independent else None,
            "reader_B_pixel_y": B[bidx]["pixel_y"] if independent else None,
            "reader_B_match_score": B[bidx]["match_score"] if independent else None,
            "reader_A_B_center_distance_px": delta,
            "reconciliation": "agreed_visible_position" if independent else "vector_resolved_raster_blended",
            "primary_holdout": bool(independent),
            "adjudication_note": (
                ("Additional exactly coincident outline paths (" + str(q["object_count"] - 1) + ") cannot prove distinct specimens; count one visible position. "
                 if q["object_count"] > 1 else "")
                + ("Raster template cannot isolate this heavily overlapping outline; hold out of primary count. "
                   if not independent else "")
                + ("Right-censored at paper's 5e6-cycle limit; do not score as a failure."
                   if is_runout else "Failure life read from plotted symbol center.")
            ),
        })

summary = {
    "source": "Hamidi Nasab et al. 2019, DOI 10.3390/met9101063, Fig. 10",
    "vector_distinct_positions": len(A),
    "raster_distinct_positions": len(B),
    "agreed_primary_positions": sum(q["primary_holdout"] for q in records),
    "primary_events": dict(Counter(q["event"] for q in records if q["primary_holdout"])),
    "primary_finish_counts": dict(Counter(q["finish"] for q in records if q["primary_holdout"])),
    "raster_blended_vector_positions": [q["record_id"] for q in records if not q["primary_holdout"]],
    "extra_exactly_coincident_outline_paths": sum(q["reader_A_vector_objects"]-1 for q in records),
    "axis_calibration": {"pdf_x_1e4": X_1E4, "pdf_x_1e7": X_1E7,
                         "pdf_y_300_mpa": Y_300, "pdf_y_0_mpa": Y_0},
    "glyph_extent": {"half_width_pdf_pt": GLYPH_HALF_PT,
                     "log10_cycles_half_width": LOG_SPAN,
                     "sigma_max_half_width_mpa": STRESS_SPAN},
}
(BASE / "reconciled_records.json").write_text(json.dumps(records, indent=2) + "\n")
(BASE / "reconciliation_summary.json").write_text(json.dumps(summary, indent=2) + "\n")
print(json.dumps(summary, indent=2))
