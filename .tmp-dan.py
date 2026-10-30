# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
p=os.path.join(C,"担.json")
if os.path.exists(p): os.remove(p); print("removed 担.json")
q=os.path.join(C,"擔.json"); d=json.load(io.open(q,encoding="utf-8"))
a=d.get("aliases") or []
for x in ("担",):
    if x not in a: a.append(x)
d["aliases"]=a; json.dump(d,io.open(q,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("擔 aliases",a)