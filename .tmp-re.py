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
    ch=False
    for s in d.get("sections",[]):
        if s.get("key")=="zigen" and str(s.get("label","")).startswith("字根「"):
            s["key"]="rootembed"; ch=True
    if ch:
        json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("renamed",n)