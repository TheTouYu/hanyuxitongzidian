# -*- coding: utf-8 -*-
import json,io,glob,sys,os
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; n=0
for f in glob.glob(C+r"\*.json"):
    if f.endswith("index.json"): continue
    try: d=json.load(io.open(f,encoding="utf-8"))
    except Exception: continue
    ch=d.get("char")
    for s in d.get("sections",[]):
        if s.get("key")=="zizu" and s.get("groups"):
            if s.get("text","").strip():
                s["text"]=""; n+=1
    json.dump(d,io.open(f,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("cleared dup text in",n,"cards")
h=io.open(r"D:\系统汉字\web\public\test.html",encoding="utf-8").read()
i=h.find("function secHTML"); print(h[i:i+260].replace("\n"," "))