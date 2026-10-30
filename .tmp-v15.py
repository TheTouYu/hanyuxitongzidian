# -*- coding: utf-8 -*-
import io,json,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\卷一雞.json"
d=json.load(io.open(p,encoding="utf-8"))
for s in d["sections"]:
    if s.get("label","").startswith("卷首·"):
        s["label"]=s["label"].split("·",1)[1]
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print([s["label"] for s in d["sections"]])