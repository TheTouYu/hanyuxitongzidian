# -*- coding: utf-8 -*-
import json,io,glob,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
rows=[]
for f in glob.glob(C+r"\*.json"):
    if os.path.basename(f) in ("index.json","variants.json"): continue
    d=json.load(io.open(f,encoding="utf-8"))
    bus=d.get("bus") or []
    num=bus[0].get("num") if bus and isinstance(bus[0],dict) else None
    if not isinstance(num,int) or not(1<=num<=10): continue
    sm=[s for s in d["sections"] if s.get("key")=="shengmu"]
    if not sm: continue
    t=sm[0]["text"]
    if "取一面" in t or "待按字義定面" in t or "待按字义定面" in t:
        g=""
        for k in ("benyi","shiyi"):
            s0=[x for x in d["sections"] if x["key"]==k]
            if s0: g=(s0[0].get("text") or "")[:26]; break
        rows.append((d["char"],d.get("parent",""),g))
print(len(rows))
for r in rows: print("|".join(r))