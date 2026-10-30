# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
V=json.load(io.open(os.path.join(C,"variants.json"),encoding="utf-8"))
pairs={}
for simp,trads in V.items():
    for t in (trads if isinstance(trads,list) else [trads]):
        if not t: continue
        pairs.setdefault(simp,set()).add(t); pairs.setdefault(t,set()).add(simp)
def expand(ch,out,depth=0):
    if ch in out or depth>3: return
    out.add(ch)
    for x in pairs.get(ch,()): expand(x,out,depth+1)
n=0
for f in os.listdir(C):
    if not f.endswith(".json") or f in ("index.json","variants.json"): continue
    p=os.path.join(C,f); d=json.load(io.open(p,encoding="utf-8"))
    base=set()
    for c in [d.get("char")]+list(d.get("aliases") or [])+[d.get("simp"),d.get("trad")]:
        if c: expand(c,base)
    m=re.search(r"（(.+?)）",d.get("head") or "")
    if m:
        for c in m.group(1):
            if c.strip(): expand(c,base)
    base.discard(d["char"])
    if base!=set(d.get("aliases") or []):
        d["aliases"]=sorted(base); json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("按繁简表补别名",n)