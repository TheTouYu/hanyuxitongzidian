# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
p=os.path.join(C,"揭.json"); d=json.load(io.open(p,encoding="utf-8"))
a=d.get("aliases") or []
if "担" not in a: a.append("担")
d["aliases"]=a; json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("揭",a)