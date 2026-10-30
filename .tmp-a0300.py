# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; V=r"D:\系统汉字\web\public\variants.json"
p=os.path.join(C,"鈟.json"); d=json.load(io.open(p,encoding="utf-8"))
al=set(d.get("aliases") or []); al.update(["釣","魡","钓"]); d["aliases"]=sorted(al)
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
try: m=json.load(io.open(V,encoding="utf-8"))
except Exception: m={}
if isinstance(m,dict): m.setdefault("钓","釣"); m.setdefault("弔","弔"); m.setdefault("吊","弔")
json.dump({"variants":m},io.open(V,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("aliases",d["aliases"])