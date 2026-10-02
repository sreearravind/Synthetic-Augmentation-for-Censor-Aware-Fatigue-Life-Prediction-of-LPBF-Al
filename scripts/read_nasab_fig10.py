"""Two method readings of Hamidi Nasab et al. (2019), Fig. 10.

Vector reading A uses PDF path geometry with rendered visibility checks.
Raster reading B uses only the rendered image and independently seeded
template matches. Neither path consults model predictions.
"""
import argparse
import hashlib
import json
from collections import defaultdict
from pathlib import Path

import fitz
import numpy as np
from PIL import Image
from scipy import ndimage as ndi, signal

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--pdf', type=Path, required=True, help='User-supplied Hamidi Nasab 2019 PDF')
parser.add_argument('--output', type=Path, required=True, help='Directory for rendered figure and readings')
args = parser.parse_args()
BASE = args.output.resolve()
BASE.mkdir(parents=True, exist_ok=True)
PDF = args.pdf.resolve()
EXPECTED_SHA256 = 'caf08c6ba88e9edebce30b4b9dcc8d49ae8f39a15cabcdb1b73fb98559c6cd8f'
actual_sha256 = hashlib.sha256(PDF.read_bytes()).hexdigest()
if actual_sha256 != EXPECTED_SHA256:
    raise ValueError(f'PDF hash mismatch: expected {EXPECTED_SHA256}, got {actual_sha256}')
PNG = BASE / "nasab_fig10_5x.png"
source_page = fitz.open(PDF)[9]
source_page.get_pixmap(matrix=fitz.Matrix(5, 5), clip=fitz.Rect(130, 540, 480, 750), alpha=False).save(PNG)

im = np.asarray(Image.open(PNG).convert("RGB"))
r, g, b = im[:, :, 0], im[:, :, 1], im[:, :, 2]
masks = {
    "MP": (r > 150) & (g < 110) & (b < 110),
    "VF": (b > 100) & (g > 50) & (r < 80),
    "SB": (r < 70) & (g < 70) & (b < 70),
}


def color_group(c):
    if c is None:
        return None
    if c[0] > 0.9 and c[1] < 0.1 and c[2] < 0.1:
        return "MP"
    if c[2] > 0.6 and c[1] > 0.3:
        return "VF"
    if max(c) < 0.1:
        return "SB"
    return None


# A: PDF geometry. White-filled symbols have one colored outline path each.
# The paper embeds an earlier, clipped plot layer; verify visibility in the
# *rendered* image, without selecting paths merely by object sequence number.
pdf = fitz.open(PDF)
grouped = defaultdict(list)
for d in pdf[9].get_drawings():
    rect = d["rect"]
    group = color_group(d.get("color"))
    if not group or not (220 < rect.x0 < 425 and 565 < rect.y0 < 675):
        continue
    if not (3.6 < rect.width < 4.05 and 3.6 < rect.height < 4.05):
        continue
    cx = (rect.x0 + rect.x1) / 2
    cy = (rect.y0 + rect.y1) / 2
    px, py = round(5 * (cx - 130)), round(5 * (cy - 540))
    region = masks[group][py - 12 : py + 13, px - 12 : px + 13]
    if region.sum() < 100:
        continue
    key = (group, round(cx, 4), round(cy, 4))
    grouped[key].append(d["seqno"])
A = [
    dict(group=k[0], pdf_x=k[1], pdf_y=k[2], pixel_x=round((k[1] - 130) * 5, 2),
         pixel_y=round((k[2] - 540) * 5, 2), object_count=len(v), sequences=v)
    for k, v in grouped.items()
]
A.sort(key=lambda q: (q["group"], q["pdf_x"], q["pdf_y"]))

# B: image-only template matching. Seed centers are visually chosen isolated
# symbols in the rendered figure and no vector coordinates enter this reading.
# Templates include the colored outline and ignore gray grid lines.
seeds = {"MP": (921, 269), "VF": (1024, 598), "SB": (1023, 379)}
B = []
for group, mask in masks.items():
    x, y = seeds[group]
    template = mask[y - 12 : y + 13, x - 12 : x + 13].astype(float)
    crop = mask[150:635, 535:1420].astype(float)
    scores = signal.fftconvolve(crop, template[::-1, ::-1], mode="same") / template.sum()
    peaks = (scores == ndi.maximum_filter(scores, size=(15, 15))) & (scores > 0.65)
    yy, xx = np.where(peaks)
    for py, px in zip(yy, xx):
        B.append(dict(group=group, pixel_x=int(px + 535), pixel_y=int(py + 150),
                      match_score=round(float(scores[py, px]), 4)))
B.sort(key=lambda q: (q["group"], q["pixel_x"], q["pixel_y"]))

(BASE / "reader_A_vector.json").write_text(json.dumps(A, indent=2) + "\n")
(BASE / "reader_B_raster.json").write_text(json.dumps(B, indent=2) + "\n")
print("PDF SHA256 is recorded in source lock; rendered figure is page 10, clip (130,540,480,750), scale=5")
print("A visible positions:", {k: sum(q["group"] == k for q in A) for k in masks})
print("A excess coincident paths:", {k: sum(q["object_count"]-1 for q in A if q["group"]==k) for k in masks})
print("B detected positions:", {k: sum(q["group"] == k for q in B) for k in masks})
