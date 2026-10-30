# -*- coding: utf-8 -*-
"""删选：把 44 部及以后尚未精修的卡移到 cards-archived/，并重建 cards/index.json。
用法: python tools/archive-cards.py [--from 44] [--dry]
"""
import json,io,os,shutil,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; A=r"D:\系统汉字\web\public\cards-archived"
args=sys.argv[1:]; dry="--dry" in args
frm=44
if "--from" in args: frm=int(args[args.index("--from")+1])
os.makedirs(A,exist_ok=True)
variants={}
vp=os.path.join(C,"variants.json")
if os.path.exists(vp): variants=json.load(io.open(vp,encoding="utf-8"))
rev={}
for simp,tr in variants.items():
    for t in (tr if isinstance(tr,list) else [tr]): rev.setdefault(t,[]).append(simp)
moved=[]; kept=[]
for fn in sorted(os.listdir(C)):
    if not fn.endswith(".json") or fn in ("index.json","variants.json"): continue
    p=os.path.join(C,fn)
    try: d=json.load(io.open(p,encoding="utf-8"))
    except Exception: kept.append(fn); continue
    if not isinstance(d,dict): kept.append(fn); continue
    bus=d.get("bus") or {}
    num=bus.get("num") if isinstance(bus,dict) else None
    if num is not None and num>=frm: moved.append(fn)
    else: kept.append(fn)
print("move",len(moved),"keep",len(kept),"from",frm, "(dry)" if dry else "")
if dry: raise SystemExit
for fn in moved: shutil.move(os.path.join(C,fn), os.path.join(A,fn))
rows=[]
for fn in kept:
    p=os.path.join(C,fn)
    try: d=json.load(io.open(p,encoding="utf-8"))
    except Exception: continue
    if not isinstance(d,dict): continue
    c=d.get("char") or fn[:-5]; bus=d.get("bus") or {}
    b=bus.get("num") if isinstance(bus,dict) else (bus[0] if isinstance(bus,list) and bus else None)
    n=bus.get("name") if isinstance(bus,dict) else None
    rows.append({"ch":d.get("char"),"cc":d.get("cc",""),"cn":d.get("cn",""),
        "h":d.get("head") or c,"c":c,"a":d.get("aliases") or [],"p":d.get("pinyin") or "",
        "t":[s.get("label","") for s in d.get("sections",[])],
        "b":b,"n":n or "","lv":d.get("level") or 3,"rl":d.get("rootLevel") or 0,
        "pr":d.get("parent") or "","rc":[],"rlb":"","rc2":[],"v":rev.get(c,[])})
json.dump(rows,io.open(os.path.join(C,"index.json"),"w",encoding="utf-8"),ensure_ascii=False,separators=(",",":"))
print("index",len(rows))