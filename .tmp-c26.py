# -*- coding: utf-8 -*-
import json,io,glob,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
n=0
for f in glob.glob(r"D:\系统汉字\web\public\cards\*.json"):
    try: d=json.load(io.open(f,encoding="utf-8"))
    except: continue
    if not isinstance(d,dict) or "sections" not in d: continue
    hit=False
    for s in d.get("sections") or []:
        if not isinstance(s,dict): continue
        t=s.get("text") or ""
        if t.startswith("原稿："):
            s["text"]=t[len("原稿："):].lstrip(); hit=True
    if hit:
        json.dump(d,io.open(f,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("stripped",n)