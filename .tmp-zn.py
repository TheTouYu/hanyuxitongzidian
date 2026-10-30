# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
p=os.path.join(C,"篧.json"); d=json.load(io.open(p,encoding="utf-8"))
d["char"]="籱"; d["head"]="籱（籗篧）"
al=[x for x in (d.get("aliases") or []) if x not in ("籱","籗","篧")]+["籗","篧"]
d["aliases"]=al
json.dump(d,io.open(os.path.join(C,"籱.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
os.remove(p)
print("renamed", al)