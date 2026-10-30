# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
pat=re.compile("依聲符取義|取義一面|按今讀|暫記聲母|泛取|取一面|按義類取")
rows=[]
for f in sorted(os.listdir(C)):
    if not f.endswith(".json"): continue
    try: d=json.load(io.open(os.path.join(C,f),encoding="utf-8"))
    except Exception: continue
    if not isinstance(d,dict): continue
    for s in d.get("sections") or []:
        if not isinstance(s,dict): continue
        if s.get("key")=="shengmu" and pat.search(s.get("text") or ""):
            rows.append((d.get("char"), (s.get("text") or "")[:46])); break
print("vague:",len(rows))
for c,t in rows[:60]: print(c,"|",t)