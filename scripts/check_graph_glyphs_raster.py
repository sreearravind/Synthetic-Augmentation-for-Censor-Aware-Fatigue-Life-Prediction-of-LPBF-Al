#!/usr/bin/env python3
"""Second modality check: count colored pixels in fresh 8x PDF rasters.

This flags occlusion and coordinate disagreement; it does not independently
establish physical specimen identity or failure status.
"""
import argparse
import csv
import hashlib
import json
from pathlib import Path

import fitz
import numpy as np

CFG = {
 "Muhammad_2023": dict(sha="67bfaaec15604e8cebd55a16d5e3b2ba23d72a1951af0e64b644fd815e5de797",
       page=9,clip=(145,85,462,289),radius=20),
 "Fernandes_2024": dict(sha="f4cd15a5fd6ca9613b30dfda6bfe5dbebf78c47b9d201bc157c46e1f286570c3",
       page=4,clip=(72,520,282,692),radius=24),
}

def colored(c, series):
    r,g,b=c[:,:,0],c[:,:,1],c[:,:,2]
    if series=="AB_R01":return (r<65)&(g<65)&(b<65)
    if series=="AB":return (b>130)&(r<110)&(g<170)
    if series=="CMP_R01":return (b>170)&(r<80)&(g<80)
    if series in ("AB_Rm1","HIP"):return (r>175)&(g<80)&(b<80)
    if series=="SR":return (r>190)&(g>100)&(g<230)&(b<80)
    return (g>80)&(r<80)&(b<160)

def main():
 p=argparse.ArgumentParser()
 p.add_argument("--muhammad",type=Path,required=True)
 p.add_argument("--fernandes",type=Path,required=True)
 p.add_argument("--candidates",type=Path,required=True)
 p.add_argument("--out",type=Path,required=True)
 a=p.parse_args();a.out.parent.mkdir(parents=True,exist_ok=True)
 results=[]
 for name,path in (("Muhammad_2023",a.muhammad),("Fernandes_2024",a.fernandes)):
  cfg=CFG[name]
  if hashlib.sha256(path.read_bytes()).hexdigest()!=cfg["sha"]:raise ValueError("PDF checksum mismatch: "+name)
  page=fitz.open(path)[cfg["page"]]
  pix=page.get_pixmap(matrix=fitz.Matrix(8,8),clip=fitz.Rect(*cfg["clip"]),alpha=False)
  img=np.frombuffer(pix.samples,dtype=np.uint8).reshape(pix.height,pix.width,3).astype(np.int16)
  for row in json.loads((a.candidates/(name+"_vector_candidates.json")).read_text()):
   x=8*(row["pdf_x"]-cfg["clip"][0]); y=8*(row["pdf_y"]-cfg["clip"][1]);R=cfg["radius"]
   x0=max(0,round(x)-R);x1=min(img.shape[1],round(x)+R+1)
   y0=max(0,round(y)-R);y1=min(img.shape[0],round(y)+R+1)
   mask=colored(img[y0:y1,x0:x1],row["series"])
   yy,xx=np.where(mask)
   if len(xx):
    dx=(float(xx.mean())+x0-x)/8;dy=(float(yy.mean())+y0-y)/8
   else:dx=dy=float("nan")
   q=[int(mask[:R,:R].sum()),int(mask[:R,R+1:].sum()),
      int(mask[R+1:,:R].sum()),int(mask[R+1:,R+1:].sum())]
   results.append(dict(candidate_id=row["candidate_id"],source=name,series=row["series"],
        pdf_x=row["pdf_x"],pdf_y=row["pdf_y"],raster_color_pixel_count=len(xx),
        raster_quadrants=";".join(map(str,q)),raster_centroid_offset_x_pdf_pt=round(dx,3),
        raster_centroid_offset_y_pdf_pt=round(dy,3),
        interpretation="pixel support is diagnostic, fitted lines/other symbols may add pixels"))
 with a.out.open("w",newline="") as f:
  w=csv.DictWriter(f,fieldnames=list(results[0]));w.writeheader();w.writerows(results)
 print("Raster checks:",len(results),"candidates")
 print("FE02/FE19:",*[r for r in results if r["candidate_id"] in ("FE02","FE19")],sep="\n")

if __name__=="__main__":main()
