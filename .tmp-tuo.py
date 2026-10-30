# -*- coding: utf-8 -*-
import json,io,os,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
HAN=re.compile("[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\U00020000-\U0002a6df]")
p=os.path.join(C,"橐.json"); d=json.load(io.open(p,encoding="utf-8"))
a=set(d.get("aliases") or [])
for v in ("槖","𢅍","𡇈"):
    if os.path.exists(os.path.join(C,v+".json")):
        os.remove(os.path.join(C,v+".json")); print("removed card",v)
    a.add(v)
d["aliases"]=sorted(a); d["head"]="橐（槖𢅍𡇈）"
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("aliases",d["aliases"])