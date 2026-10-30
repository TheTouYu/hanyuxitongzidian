# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
z=json.load(io.open(r"D:\系统汉字\web\public\zigen.json",encoding="utf-8"))
by=z.get("byName") or {}
n=0
for f in os.listdir(C):
    if not f.endswith(".json") or f=="index.json": continue
    p=os.path.join(C,f); d=json.load(io.open(p,encoding="utf-8")); ch=d.get("char")
    if ch in by and d.get("level")!=1:
        d["level"]=1; d.pop("parent",None)
        info=by[ch]
        if not d.get("bus"): d["bus"]=[{"num":info.get("no"),"name":ch}]
        json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("修正部头卡 level=1:",n)