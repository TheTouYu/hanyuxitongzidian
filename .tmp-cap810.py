# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
var={}
vj=os.path.join(C,"variants.json")
if os.path.exists(vj):
    v=json.load(io.open(vj,encoding="utf-8"))
    if isinstance(v,dict):
        for k,val in v.items():
            var[k]=set(val if isinstance(val,list) else [val])
n=0; tot=0
for fn in os.listdir(C):
    if not fn.endswith(".json") or fn in ("index.json","variants.json"): continue
    p=os.path.join(C,fn); d=json.load(io.open(p,encoding="utf-8"))
    ch=d.get("char") or fn[:-5]
    al=set(d.get("aliases") or [])
    head=d.get("head") or ""
    m=re.search(r"（([^）]*)）",head)
    if m: al.update(list(m.group(1)))
    for k in ("simp","trad"):
        x=d.get(k)
        if isinstance(x,str) and x: al.update(list(x) if len(x)>1 else [x])
    for k in (ch,d.get("trad"),d.get("simp")):
        if k and k in var: al.update(var[k])
    al.discard(ch); al={x for x in al if x and x!=ch}
    old=set(d.get("aliases") or [])
    if al!=old:
        d["aliases"]=sorted(al); json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
    tot+=len(d.get("aliases") or [])
print("改卡",n,"别名总数",tot)