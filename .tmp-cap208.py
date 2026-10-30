# -*- coding: utf-8 -*-
import json,io,glob,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
for f in sorted(glob.glob(C+r"\*.json")):
    if os.path.basename(f) in ("index.json","variants.json"): continue
    d=json.load(io.open(f,encoding="utf-8"))
    if (d.get("parent") or "")!="氐": continue
    sm=[s for s in d["sections"] if s.get("key")=="shengmu"]
    if not sm or "㠯部聲母為零" not in sm[0]["text"]: continue
    g=""
    for k in ("benyi","shiyi"):
        s=[x for x in d["sections"] if x["key"]==k]
        if s: g=(s[0].get("text") or "")[:30]; break
    print(d["char"],"|",g)