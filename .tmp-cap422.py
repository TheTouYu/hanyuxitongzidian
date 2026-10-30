# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
V=json.load(io.open(C+r"\variants.json",encoding="utf-8"))
inv={}
for s,ts in V.items():
    for t in ts: inv.setdefault(t,[]).append(s)
n=0; miss=[]
for t,ss in inv.items():
    p=os.path.join(C,t+".json")
    if not os.path.exists(p):
        miss.append(t); continue
    d=json.load(io.open(p,encoding="utf-8"))
    al=set(d.get("aliases") or []); al.update(ss)
    if ss: d["simp"]=ss[0]
    d["aliases"]=sorted(al)
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("补simp/aliases",n,"无卡繁字",len(miss),miss[:12])