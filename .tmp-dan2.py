# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
print("淡 card:",os.path.exists(os.path.join(C,"淡.json")))
p=os.path.join(C,"澹.json"); d=json.load(io.open(p,encoding="utf-8")); a=d.get("aliases") or []
if "淡" not in a: a.append("淡")
d["aliases"]=a; json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
for vp in (os.path.join(C,"variants.json"), r"D:\系统汉字\web\public\variants.json"):
    v={}
    if os.path.exists(vp):
        try: v=json.load(io.open(vp,encoding="utf-8"))
        except Exception: v={}
    arr=v.get("淡") or []
    if "澹" not in arr: arr.append("澹")
    v["淡"]=arr
    json.dump(v,io.open(vp,"w",encoding="utf-8"),ensure_ascii=False)
print("澹 aliases",a)