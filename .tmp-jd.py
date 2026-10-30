# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
p=C+"\\斤.json"; d=json.load(io.open(p,encoding="utf-8"))
n0=0
for s in d["sections"]:
    if s.get("key")=="zizu":
        for g in s["groups"]:
            b=[r for r in g["rows"] if r[0]!="听"]
            n0+=len(g["rows"])-len(b); g["rows"]=b
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
tp=os.path.join(C,"听.json")
if os.path.exists(tp): os.remove(tp); print("removed 听.json")
print("removed rows",n0)