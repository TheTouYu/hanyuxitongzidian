# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
p=os.path.join(C,"斤.json"); d=json.load(io.open(p,encoding="utf-8"))
keys=[s["key"] for s in d["sections"]]
if "erji" not in keys:
    d["sections"].insert(-1,{"key":"erji","label":"本部二级字根","text":"","links":[{"ch":"所","label":"所"},{"ch":"訢","label":"訢（欣）"}]})
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print([s["key"] for s in d["sections"]])