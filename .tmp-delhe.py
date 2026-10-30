# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
for n in ("鶴","鹤"):
    p=os.path.join(C,n+".json")
    if os.path.exists(p): os.remove(p); print("deleted",n)
for vp in (os.path.join(C,"variants.json"), r"D:\系统汉字\web\public\variants.json"):
    if not os.path.exists(vp): continue
    d=json.load(io.open(vp,encoding="utf-8")); m=d.get("variants") or d
    m["鹤"]=["隺"]; m["鶴"]=["隺"]
    json.dump({("variants" if "variants" in d else "variants"):m},io.open(vp,"w",encoding="utf-8"),ensure_ascii=False)
    print("variants updated",vp.split("\\")[-2:])