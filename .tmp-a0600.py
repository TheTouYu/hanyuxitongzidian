# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
HAN=re.compile(r"[\u3400-\u9fff\U00020000-\U0002A6DF]")
n=0
for fn in sorted(os.listdir(C)):
    if not fn.endswith(".json") or fn in ("index.json","variants.json"): continue
    p=os.path.join(C,fn); d=json.load(io.open(p,encoding="utf-8")); ch=d.get("char") or fn[:-5]
    h=d.get("head") or ""
    m=re.search(r"（([^）]+)）",h)
    old=[a for a in (d.get("aliases") or []) if len(HAN.findall(a))<=1]
    vs=HAN.findall(m.group(1)) if m else []
    al=sorted({a for a in old+vs if a!=ch})
    if al!= (d.get("aliases") or []):
        d["aliases"]=al; json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("cards fixed",n)