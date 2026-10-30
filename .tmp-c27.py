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
        gs=s.get("groups") or []
        t=(s.get("text") or "").strip()
        if len(gs)==1 and t:
            ti=(gs[0].get("title") or "").strip("。 ")
            if ti and (t==ti or t.rstrip("。")==ti or t.startswith(ti)):
                s["text"]=""; hit=True
    if hit:
        json.dump(d,io.open(f,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("cards fixed",n)