# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
n=0
for f in os.listdir(C):
    if not f.endswith(".json") or f in ("index.json","variants.json"): continue
    p=os.path.join(C,f)
    try: d=json.load(io.open(p,encoding="utf-8"))
    except Exception: continue
    if not isinstance(d,dict): continue
    secs=d.get("sections") or []
    keep=[s for s in secs if s.get("key") not in ("rootembed","zigen") or not str(s.get("label","")).startswith("字根「")]
    if len(keep)!=len(secs):
        d["sections"]=keep
        json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("cleaned",n)