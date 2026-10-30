# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\朿.json"
d=json.load(io.open(p,encoding="utf-8"))
for s in d["sections"]:
    if s.get("key")=="shengmu":
        s["text"]="c「刺持」取「刺」：朿為箭頭之刺，木刺尖利，直刺傷人（推）。"
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print(d["char"], [s["text"] for s in d["sections"] if s["key"]=="shengmu"])