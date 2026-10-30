# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
p=os.path.join(C,"臺.json"); d=json.load(io.open(p,encoding="utf-8"))
d["aliases"]=["坮","㙵"]
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("aliases",d["aliases"],"parent",d["parent"])