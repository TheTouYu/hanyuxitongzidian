# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
fam=["栜","茦","洓","㾊","蓛","㭰","𧙞","㢀","𧊸","𧻕","刺","𧧒","敇","拺"]
n=0
for ch in fam:
    p=os.path.join(C,ch+".json"); d=json.load(io.open(p,encoding="utf-8"))
    if d.pop("rootLevel",None) is not None: n+=1
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("去 rootLevel",n)
idx=json.load(io.open(os.path.join(C,"index.json"),encoding="utf-8"))
print("刺条目",[ (x.get("c"),x.get("a")) for x in idx if x.get("c")=="刺" or "刺" in (x.get("a") or [])])