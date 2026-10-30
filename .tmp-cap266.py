# -*- coding: utf-8 -*-
import json,io,sys,os
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
d=json.load(io.open(os.path.join(C,"市.json"),encoding="utf-8"))
for s in d["sections"]:
    if s.get("key")=="shengmu":
        s["text"]="s「失收」取「收」：市為廟會所聚，人貨收聚而交易（推）。"
json.dump(d,io.open(os.path.join(C,"市.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("ok",[s["key"] for s in d["sections"]], len(d["sections"][-1].get("groups",[])))