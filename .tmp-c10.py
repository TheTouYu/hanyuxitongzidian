# -*- coding: utf-8 -*-
import json,io,glob,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
n=0
for f in glob.glob(r"D:\系统汉字\web\public\cards\第*章*.json"):
    d=json.load(io.open(f,encoding="utf-8"))
    if not d.get("chapter"): continue
    for s in d["sections"]:
        if s.get("key")=="yinxi":
            s["text"]=""
            for g in (s.get("groups") or []): g["title"]=""
    json.dump(d,io.open(f,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("patched",n)