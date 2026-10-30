# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\家.json"; d=json.load(io.open(p,encoding="utf-8"))
for s in d["sections"]:
    if s["key"]=="zizu":
        g=s["groups"]
        g[0]["title"]="①"
        print("groups:",[x["title"] for x in g], "rows:",[len(x["rows"]) for x in g])
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)