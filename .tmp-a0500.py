# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
n=0; added=0; samples=[]
for fn in sorted(os.listdir(C)):
    if not fn.endswith(".json") or fn in ("index.json","variants.json"): continue
    p=os.path.join(C,fn); d=json.load(io.open(p,encoding="utf-8")); ch=d.get("char") or fn[:-5]
    h=d.get("head") or ""
    m=re.search(r"（([^）]+)）",h)
    if not m: continue
    vs=[x for x in m.group(1).split() if x and x!=ch]
    al=list(dict.fromkeys((d.get("aliases") or [])+vs))
    if set(vs)-set(d.get("aliases") or []):
        d["aliases"]=al; json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
        n+=1; added+=len(vs); 
        if len(samples)<8: samples.append((ch,"".join(vs)))
print("补齐卡数",n,"新增别名",added,samples)