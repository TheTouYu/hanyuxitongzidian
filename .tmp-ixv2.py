# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
D=r"D:\系统汉字\web\public\cards"
var=json.load(io.open(os.path.join(D,"variants.json"),encoding="utf-8"))
inv={}
for s,ts in var.items():
    for t in ts: inv.setdefault(t,[]).append(s)
p=os.path.join(D,"index.json"); rows=json.load(io.open(p,encoding="utf-8"))
n=0
for r in rows:
    c=r.get("ch") or r.get("c")
    v=inv.get(c) or []
    if v: r["v"]=v; n+=1
    else: r.pop("v",None)
json.dump(rows,io.open(p,"w",encoding="utf-8"),ensure_ascii=False)
print("rows",len(rows),"v",n)