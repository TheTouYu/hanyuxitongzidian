# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
D=r"D:\系统汉字\web\public\cards"
hit=[]
for f in os.listdir(D):
    if not f.endswith(".json") or f in ("index.json","variants.json"): continue
    p=os.path.join(D,f)
    try: d=json.load(io.open(p,encoding="utf-8"))
    except Exception: continue
    for s in d.get("sections",[]):
        if s.get("key")=="shengmu" and "山名。本" in (s.get("text") or ""):
            s["text"]="j「聚决」取「聚」：山石之聚而高（推）。"
            json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
            hit.append(f); break
print(hit)