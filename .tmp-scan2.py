# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
pat=re.compile("依聲符取義|取義一面|取一面|按義類取")
for f in sorted(os.listdir(C)):
    if not f.endswith(".json"): continue
    try: d=json.load(io.open(os.path.join(C,f),encoding="utf-8"))
    except Exception: continue
    if not isinstance(d,dict): continue
    sm=None; gl=""
    for s in d.get("sections") or []:
        if not isinstance(s,dict): continue
        if s.get("key")=="shengmu": sm=s.get("text") or ""
        if s.get("key") in ("shiyi","benyi") and not gl: gl=(s.get("text") or "")
    if sm and pat.search(sm):
        g=re.sub(r"《[^》]*》","",gl)[:34]
        print(d.get("char"),"|",sm.split("：")[0],"|",g)