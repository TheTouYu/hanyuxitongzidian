# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\措.json"; d=json.load(io.open(p,encoding="utf-8"))
d["head"]="措"; d["aliases"]=[]
for s in d["sections"]:
    if s.get("key")=="shiyi" and not s.get("text","").startswith("措"):
        s["text"]="措cuò《說文》：“置也。从手昔聲。倉故切。”安放、安置；《廣韻》：“置也。}}\"".replace("}}","")
    if s.get("key")=="shengmu":
        s["text"]="c「刺持」取「持」：手執而安置之（推）。"
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("ok",d["head"])