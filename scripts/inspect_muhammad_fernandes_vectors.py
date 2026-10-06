#!/usr/bin/env python3
"""Produce source glyph candidate JSON and annotated crops; no model data used."""
import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path
import fitz
from PIL import Image, ImageDraw, ImageFont

SOURCES = {
 "Muhammad_2023": {
  "sha": "67bfaaec15604e8cebd55a16d5e3b2ba23d72a1951af0e64b644fd815e5de797",
  "page": 9, "clip": (145,85,462,289),
 },
 "Fernandes_2024": {
  "sha": "f4cd15a5fd6ca9613b30dfda6bfe5dbebf78c47b9d201bc157c46e1f286570c3",
  "page": 4, "clip": (72,520,282,692),
 },
}

def detect_m(d):
 r=d["rect"]
 if not (3.73<r.width<3.79 and 3.73<r.height<3.79):return None
 if d["type"]=="f":
  color=d.get("fill")
  if color==(0.,0.,0.) and len(d["items"])==1:return "AB_R01"
  if color==(1.,0.,0.) and len(d["items"])==4:return "AB_Rm1"
  if color==(0.,0.,1.) and len(d["items"])==3:return "CMP_R01"
 if d["type"]=="s":
  color=d.get("color")
  if color and color[0]<.01 and .65<color[1]<.75 and .27<color[2]<.35 and len(d["items"])==3:return "CMP_Rm1"
 return None

def detect_f(d):
 r=d["rect"]
 if not (4.8<r.width<5.0 and 5.1<r.height<5.3 and d["type"]=="s"):return None
 color=d.get("color")
 if color and .25<color[0]<.30 and .43<color[1]<.47:return "AB"
 if color and .72<color[1]<.79 and color[2]<.01:return "SR"
 if color==(1.,0.,0.):return "HIP"
 return None

def main():
 p=argparse.ArgumentParser()
 p.add_argument("--muhammad",type=Path,required=True)
 p.add_argument("--fernandes",type=Path,required=True)
 p.add_argument("--output",type=Path,required=True)
 a=p.parse_args();a.output.mkdir(parents=True,exist_ok=True)
 for source,path,detector in (("Muhammad_2023",a.muhammad,detect_m),("Fernandes_2024",a.fernandes,detect_f)):
  cfg=SOURCES[source]
  if hashlib.sha256(path.read_bytes()).hexdigest()!=cfg["sha"]:raise ValueError(source+" PDF hash mismatch")
  page=fitz.open(path)[cfg["page"]]
  clip=fitz.Rect(*cfg["clip"])
  candidates=[]
  for d in page.get_drawings():
   tag=detector(d)
   if not tag:continue
   r=d["rect"];x=(r.x0+r.x1)/2;y=(r.y0+r.y1)/2
   if not clip.contains(fitz.Point(x,y)):continue
   if source=="Fernandes_2024" and x>245 and y<570:continue # plot legend, not specimens
   candidates.append(dict(source=source,series=tag,pdf_x=round(x,4),pdf_y=round(y,4),
                          glyph_halfwidth_pdf_pt=round(r.width/2,4),
                          glyph_halfheight_pdf_pt=round(r.height/2,4),
                          drawing_sequence=d["seqno"],geometry_items=len(d["items"])))
  candidates.sort(key=lambda r:(r["series"],r["pdf_x"],r["pdf_y"]))
  for i,r in enumerate(candidates,1):r["candidate_id"]=("MU" if source=="Muhammad_2023" else "FE")+f"{i:02d}"
  (a.output/(source+"_vector_candidates.json")).write_text(json.dumps(candidates,indent=2)+"\n")
  pix=page.get_pixmap(matrix=fitz.Matrix(5,5),clip=clip,alpha=False)
  png=a.output/(source+"_annotated.png");pix.save(png)
  im=Image.open(png).convert("RGB")
  draw=ImageDraw.Draw(im)
  colors={"AB_R01":"#222222","AB_Rm1":"#CC0000","CMP_R01":"#0000CC","CMP_Rm1":"#009933",
          "AB":"#2966BB","SR":"#D89800","HIP":"#CC0000"}
  for r in candidates:
   x=5*(r["pdf_x"]-clip.x0);y=5*(r["pdf_y"]-clip.y0)
   c=colors[r["series"]]
   draw.ellipse((x-14,y-14,x+14,y+14),outline=c,width=2)
   draw.text((x+12,y-24),r["candidate_id"],fill=c,stroke_width=2,stroke_fill="white")
  im.save(png)
  print(source,dict(Counter(r["series"] for r in candidates)),len(candidates),png)

if __name__=="__main__":main()
