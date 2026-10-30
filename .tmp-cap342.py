# -*- coding: utf-8 -*-
import json,io,glob,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
z=json.load(io.open(r"D:\系统汉字\web\public\zigen.json",encoding="utf-8")); bn=z["byName"]
n=0; miss=0
for f in glob.glob(C+r"\*.json"):
    if os.path.basename(f) in ("index.json","variants.json"): continue
    d=json.load(io.open(f,encoding="utf-8"))
    if d.get("bus"): continue
    p=d.get("parent") or ""
    it=bn.get(p)
    if it: d["bus"]=[{"num":it["no"],"name":p}]; json.dump(d,io.open(f,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
    else: miss+=1
print("补 bus",n,"仍缺",miss)