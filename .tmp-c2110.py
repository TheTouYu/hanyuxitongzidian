# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
v=json.load(io.open(os.path.join(C,"variants.json"),encoding="utf-8"))
rev={}
for k,x in v.items():
    if isinstance(x,list):
        for t in x: rev.setdefault(t,[]).append(k)
    else: rev.setdefault(x,[]).append(k)
n=0
for fn in os.listdir(C):
    if not fn.endswith(".json") or fn in ("index.json","variants.json"): continue
    p=os.path.join(C,fn); d=json.load(io.open(p,encoding="utf-8"))
    ch=d.get("char") or fn[:-5]; dirty=False
    cand=[]
    if ch in v and isinstance(v[ch],str): cand.append(v[ch])
    if ch in v and isinstance(v[ch],list): cand+=v[ch]
    if ch in rev: cand+=rev[ch]
    cand=[c for c in cand if c and c!=ch]
    if cand and not d.get("simp"):
        d["simp"]=cand[0]; dirty=True
    al=set(d.get("aliases") or [])
    for c in cand[:3]: al.add(c)
    if al!=set(d.get("aliases") or []):
        d["aliases"]=sorted(al); dirty=True
    if dirty:
        json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("补繁简",n)