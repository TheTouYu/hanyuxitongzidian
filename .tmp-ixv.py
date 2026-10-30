# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
D=r"D:\系统汉字\web\public\cards"
var=json.load(io.open(os.path.join(D,"variants.json"),encoding="utf-8"))
inv={}
for s,ts in var.items():
    for t in ts: inv.setdefault(t,[]).append(s)
p=os.path.join(D,"index.json"); ix=json.load(io.open(p,encoding="utf-8"))
rows=ix["cards"] if isinstance(ix,dict) and "cards" in ix else ix
n=0
for r in rows:
    c=r.get("c") or r.get("char")
    v=inv.get(c) or []
    if v: r["v"]=v; n+=1
    elif "v" in r: r.pop("v")
json.dump({"cards":rows},io.open(p,"w",encoding="utf-8"),ensure_ascii=False)
print("rows",len(rows),"with_v",n)