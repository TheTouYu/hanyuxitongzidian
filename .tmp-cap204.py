# -*- coding: utf-8 -*-
import json,io,glob,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
n=0; other=[]
for f in glob.glob(C+r"\*.json"):
    if os.path.basename(f) in ("index.json","variants.json"): continue
    d=json.load(io.open(f,encoding="utf-8"))
    sm=[s for s in d.get("sections",[]) if s.get("key")=="shengmu"]
    if not sm or "取一面" not in (sm[0].get("text") or ""): continue
    bus=d.get("bus") or []
    num=bus[0].get("num") if bus and isinstance(bus[0],dict) else None
    if num==8:
        sm[0]["text"]="㠯部聲母為零（yǐ），緒論七組未列，不系（照實）。"
        json.dump(d,io.open(f,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
    else: other.append(d["char"])
print("㠯部定为零声母",n,"余非㠯部",len(other))
print(other[:15])