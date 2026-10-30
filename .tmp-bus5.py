# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
z=json.load(io.open(r"D:\系统汉字\web\public\zigen.json",encoding="utf-8"))
num2name={}
for ch,v in (z.get("byName") or {}).items():
    if v.get("no") and v["no"] not in num2name: num2name[v["no"]]=ch
fixed=0
for f in os.listdir(C):
    if not f.endswith(".json") or f in ("index.json","variants.json"): continue
    p=os.path.join(C,f); d=json.load(io.open(p,encoding="utf-8"))
    b=d.get("bus"); ch=f[:-5]
    num=None
    if isinstance(b,list) and b and isinstance(b[0],str) and b[0].strip().isdigit(): num=int(b[0])
    elif isinstance(b,str) and b.strip().isdigit(): num=int(b)
    elif isinstance(b,dict) and b.get("num"): num=int(b["num"])
    elif isinstance(b,list) and b and isinstance(b[0],dict) and b[0].get("num"): num=int(b[0]["num"])
    if num is None: continue
    name=(b[0].get("name") if isinstance(b,list) and b and isinstance(b[0],dict) else None) or num2name.get(num) or (ch if d.get("level")==1 else "")
    new=[{"num":num,"name":name}]
    if b!=new:
        d["bus"]=new; json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); fixed+=1
print("normalized bus",fixed)