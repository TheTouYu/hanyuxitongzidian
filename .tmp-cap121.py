# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
z=json.load(io.open(r"D:\系统汉字\web\public\zigen.json",encoding="utf-8"))["byName"]
byno={v["no"]:k for k,v in z.items()}
for no in range(1,11):
    ch=byno.get(no)
    if not ch: print(no,"无部头"); continue
    p=os.path.join(C,ch+".json")
    if not os.path.exists(p): print(no,ch,"缺卡"); continue
    d=json.load(io.open(p,encoding="utf-8"))
    keys=[s["key"] for s in d["sections"]]
    rows=sum(len(g["rows"]) for s in d["sections"] for g in (s.get("groups") or []))
    print(f"{no} {ch} level={d.get('level')} 栏={len(keys)} 字族行={rows} keys={','.join(keys)}")