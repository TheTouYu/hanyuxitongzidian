# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\弔.json"
d=json.load(io.open(p,encoding="utf-8"))
for s in d["sections"]:
    s["text"]=(s.get("text") or "").replace(".emf",".png")
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
for s in d["sections"]:
    if "inline" in (s.get("text") or ""): print(s["key"], s["text"][:160])
print("photo",d.get("photos"),d.get("captions"))