# -*- coding: utf-8 -*-
import json,io,glob,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; n=0
for p in glob.glob(os.path.join(C,"*.json")):
    if p.endswith("index.json"): continue
    try: d=json.load(io.open(p,encoding="utf-8"))
    except Exception: continue
    if not isinstance(d,dict) or "sections" not in d: continue
    secs=[s for s in d["sections"] if "gscroll" not in (s.get("text") or "")]
    if len(secs)!=len(d["sections"]):
        d["sections"]=secs
        json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("移除重复字形栏",n)