# -*- coding: utf-8 -*-
"""重建 web/public/cards/index.json（不移动文件）。"""
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
variants={}
vp=os.path.join(C,"variants.json")
if os.path.exists(vp): variants=json.load(io.open(vp,encoding="utf-8"))
rev={}
for simp,tr in variants.items():
    for t in (tr if isinstance(tr,list) else [tr]): rev.setdefault(t,[]).append(simp)
rows=[]
for fn in sorted(os.listdir(C)):
    if not fn.endswith(".json") or fn in ("index.json","variants.json"): continue
    try: d=json.load(io.open(os.path.join(C,fn),encoding="utf-8"))
    except Exception: continue
    if not isinstance(d,dict): continue
    c=d.get("char") or fn[:-5]; bus=d.get("bus") or {}
    b=bus.get("num") if isinstance(bus,dict) else (bus[0] if isinstance(bus,list) and bus else None)
    n=bus.get("name") if isinstance(bus,dict) else ""
    rows.append({"ch":d.get("char"),"cc":d.get("cc",""),"cn":d.get("cn",""),
        "h":d.get("head") or c,"c":c,"a":d.get("aliases") or [],"p":d.get("pinyin") or "",
        "t":[s.get("label","") for s in d.get("sections",[])],
        "b":b,"n":n or "","lv":d.get("level") or 3,"rl":d.get("rootLevel") or 0,
        "pr":d.get("parent") or "","rc":[],"rlb":"","rc2":[],"v":rev.get(c,[])})
json.dump(rows,io.open(os.path.join(C,"index.json"),"w",encoding="utf-8"),ensure_ascii=False,separators=(",",":"))
print("index",len(rows))