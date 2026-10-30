# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
for fn in ("厂.json","反.json"):
    p=os.path.join(C,fn); d=json.load(io.open(p,encoding="utf-8"))
    secs=[s for s in d["sections"] if s.get("key") not in ("suoshu","suoshujuan")]
    secs.append({"key":"suoshujuan","label":"所属卷","text":"","links":[{"ch":"卷五雁","label":"卷五 雁"}]})
    d["sections"]=secs
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("ok")