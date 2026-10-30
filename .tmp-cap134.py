# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\枳.json"
d=json.load(io.open(p,encoding="utf-8"))
print("before:", [(s["key"],s.get("text")) for s in d["sections"]])
for s in d["sections"]:
    if s.get("key")=="shengmu":
        s["text"]="zh「凿总」取「凿」：枳枝有刺，扎刺人。"
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("after:", [s.get("text") for s in d["sections"] if s["key"]=="shengmu"])