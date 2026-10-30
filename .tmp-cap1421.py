# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
V=json.load(io.open(r"D:\系统汉字\web\public\variants.json",encoding="utf-8"))
pairs=V.get("pairs") or V
# 建立 繁→简
f2s={}
if isinstance(pairs,list):
    for x in pairs:
        if isinstance(x,dict):
            s=x.get("s") or x.get("simp"); t=x.get("t") or x.get("trad")
            if t and s: f2s[t]=s
        elif isinstance(x,(list,tuple)) and len(x)==2: f2s[x[1]]=x[0]
else:
    for t,s in pairs.items(): f2s[t]=s
n=0
for fn in os.listdir(C):
    if not fn.endswith(".json") or fn=="index.json": continue
    p=os.path.join(C,fn); d=json.load(io.open(p,encoding="utf-8")); ch=d.get("char")
    s=f2s.get(ch)
    if s and s!=ch:
        d["simp"]=s
        al=set(d.get("aliases") or []); al.add(s); d["aliases"]=sorted(al); n+=1
        json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("补 simp",n,"責->",f2s.get("責"))