# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\虖.json"
d=json.load(io.open(p,encoding="utf-8"))
for s in d["sections"]:
    if s.get("key")=="zizu":
        for g in s["groups"]:
            g["title"]=re.sub(r"^[①②③④⑤]\s*","",g["title"])
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print([g["title"] for g in [x for x in d["sections"] if x["key"]=="zizu"][0]["groups"]])