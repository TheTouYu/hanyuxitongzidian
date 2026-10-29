# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
bad=[]
for f in os.listdir(C):
    if not f.endswith(".json") or f in ("index.json","variants.json"): continue
    try: d=json.load(io.open(os.path.join(C,f),encoding="utf-8"))
    except Exception: continue
    for s in d.get("sections",[]):
        if s.get("key")=="zizu":
            for g in s.get("groups",[]):
                if not (g.get("title") or "").strip():
                    bad.append((f,g.get("no","?"),len(g.get("rows",[]))))
print("groups missing title:",len(bad))
for b in bad[:40]: print(b)
