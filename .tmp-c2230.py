# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
v=json.load(io.open(r"D:\系统汉字\web\public\variants.json",encoding="utf-8"))
rev={}
for k,x in v.items():
    for t in ([x] if isinstance(x,str) else x):
        rev.setdefault(t,[]).append(k)
n=0
for fn in os.listdir(C):
    if not fn.endswith(".json") or fn=="index.json": continue
    p=os.path.join(C,fn); d=json.load(io.open(p,encoding="utf-8"))
    ch=d.get("char") or fn[:-5]; cand=[]
    x=v.get(ch); cand += [x] if isinstance(x,str) else (x or [])
    cand += rev.get(ch,[]); cand=[c for c in cand if c and c!=ch]
    dirty=False
    if cand and not d.get("simp"): d["simp"]=cand[0]; dirty=True
    al=set(d.get("aliases") or []); al.update(cand[:3])
    if al!=set(d.get("aliases") or []): d["aliases"]=sorted(al); dirty=True
    if dirty:
        json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("补繁简",n)