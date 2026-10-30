# -*- coding: utf-8 -*-
import json,io,glob,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
out=[]
for f in sorted(glob.glob(C+r"\*.json")):
    if os.path.basename(f) in ("index.json","variants.json"): continue
    d=json.load(io.open(f,encoding="utf-8"))
    sm=[s for s in d.get("sections",[]) if s.get("key")=="shengmu"]
    if not sm or "取一面" not in (sm[0].get("text") or ""): continue
    g=""
    for k in ("benyi","shiyi"):
        s=[x for x in d["sections"] if x["key"]==k]
        if s: g=(s[0].get("text") or "")[:46]; break
    out.append((d["char"],d.get("pinyin",""),str(d.get("bus")),g))
print("余",len(out))
for r in out[:12]: print(r[0],"|",r[1],"|",r[2],"|",r[3])