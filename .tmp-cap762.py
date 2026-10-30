# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\薹.json"; d=json.load(io.open(p,encoding="utf-8"))
d["rootLevel"]=3; d["level"]=3
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("薹 rootLevel=3")