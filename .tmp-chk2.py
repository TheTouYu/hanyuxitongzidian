# -*- coding: utf-8 -*-
import json,io,glob,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; out=[]
for f in glob.glob(C+r"\*.json"):
    if f.endswith("index.json"): continue
    d=json.load(io.open(f,encoding="utf-8")); ch=d.get("char")
    for s in d.get("sections",[]):
        for g in (s.get("groups") or []):
            hdr=g.get("header") or []
            if hdr and len(hdr)!=4 and g.get("rows"): out.append((ch,s.get("key"),len(hdr),len(g["rows"][0])))
            for r in (g.get("rows") or []):
                if len(r)!=4 and len(hdr)!=len(r): out.append((ch,s.get("key"),"r",len(r)))
print(len(out)); print(out[:12])
print([ (json.load(io.open(f,encoding="utf-8")).get("char")) for f in glob.glob(C+r"\*.json") if json.load(io.open(f,encoding="utf-8")).get("level")==2 and "zizu" not in [s["key"] for s in json.load(io.open(f,encoding="utf-8"))["sections"]]])