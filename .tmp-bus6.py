# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
cm=json.load(io.open(r"D:\系统汉字\.tmp-charmap.json",encoding="utf-8"))
items=cm.items() if isinstance(cm,dict) else []
fixed=0; left=0
for f in os.listdir(C):
    if not f.endswith(".json") or f in ("index.json","variants.json"): continue
    p=os.path.join(C,f); d=json.load(io.open(p,encoding="utf-8")); ch=f[:-5]
    b=d.get("bus")
    ok=isinstance(b,list) and b and isinstance(b[0],dict) and b[0].get("num")
    if ok: continue
    v=cm.get(ch)
    if not v: left+=1; continue
    no=v.get("bu") or v.get("buNo") or v.get("no"); nm=v.get("buName") or v.get("name") or ""
    if not no: left+=1; continue
    d["bus"]=[{"num":int(no),"name":nm}]
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); fixed+=1
print("fixed",fixed,"left",left)