# -*- coding: utf-8 -*-
import json,io,glob,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
n=0
for f in glob.glob(r"D:\系统汉字\web\public\cards\第*章*.json"):
    d=json.load(io.open(f,encoding="utf-8"))
    if not d.get("chapter"): continue
    for s in d["sections"]:
        if s.get("key")=="yinxi":
            for g in (s.get("groups") or []):
                g["header"]=["卷","部目"]
                g["rows"]=[[r[0],r[2]] for r in g["rows"] if len(r)>=3]
    json.dump(d,io.open(f,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("patched",n)