# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\歇.json"
d=json.load(io.open(p,encoding="utf-8"))
for s in d["sections"]:
    if s.get("key")=="shengmu":
        s["text"]="x「续消」取「消」：勞作不已，氣力消盡乃休歇。"
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print([s["text"] for s in d["sections"] if s["key"]=="shengmu"])