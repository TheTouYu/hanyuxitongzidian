# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
V=json.load(io.open(os.path.join(C,"variants.json"),encoding="utf-8"))
pairs={}
for t,s in (V.items() if isinstance(V,dict) else []):
    pairs.setdefault(t,set()).add(s); pairs.setdefault(s,set()).add(t)
def expand(ch,out):
    out.add(ch)
    for x in pairs.get(ch,()): out.add(x)
n=0
for f in os.listdir(C):
    if not f.endswith(".json") or f in ("index.json","variants.json"): continue
    p=os.path.join(C,f); d=json.load(io.open(p,encoding="utf-8"))
    al=set(d.get("aliases") or [])
    h=d.get("head") or ""
    m=re.search(r"（(.+?)）",h)
    if m:
        for c in m.group(1): 
            if c.strip(): al.add(c)
    for c in (d.get("simp"),d.get("trad")):
        if c: al.add(c)
    base=set(); expand(d["char"],base)
    for a in list(al): expand(a,base)
    base.discard(d["char"])
    if base!=al:
        d["aliases"]=sorted(base); json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("补别名",n)