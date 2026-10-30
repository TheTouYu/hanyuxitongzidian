# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
fixed=[]
for fn in os.listdir(C):
    if not fn.endswith(".json") or fn in ("index.json","variants.json"): continue
    p=os.path.join(C,fn); d=json.load(io.open(p,encoding="utf-8"))
    ch=d.get("char") or fn[:-5]
    head=d.get("head") or ""
    m=re.search(r"（([^）]*)）",head)
    if not m: continue
    need=set(m.group(1)); have=set(d.get("aliases") or []); have.discard(ch)
    miss=need-have
    if miss:
        have|=need; d["aliases"]=sorted(have)
        json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
        fixed.append((ch,sorted(miss)))
print("补",len(fixed),fixed[:12])