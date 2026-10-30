# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
p=os.path.join(C,"臺.json"); d=json.load(io.open(p,encoding="utf-8"))
d["parent"]="至"; d["level"]=3; d["rootLevel"]=3
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
t=os.path.join(C,"薹.json"); e=json.load(io.open(t,encoding="utf-8"))
e["parent"]="臺"; e["rootLevel"]=3
json.dump(e,io.open(t,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("臺 parent",d["parent"],"level",d["level"],"| 薹 parent",e["parent"])