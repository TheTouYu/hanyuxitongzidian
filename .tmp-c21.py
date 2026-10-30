# -*- coding: utf-8 -*-
import json,io,glob,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
n=0
for f in glob.glob(r"D:\系统汉字\web\public\cards\卷*.json"):
    d=json.load(io.open(f,encoding="utf-8"))
    ch=d.get("char") or ""
    if not ch.startswith("卷"): continue
    hit=False
    for s in d.get("sections") or []:
        if s.get("key")=="yinxi" and "音系即本卷所属诸部" in (s.get("text") or ""):
            s["text"]=""; hit=True
    if hit:
        json.dump(d,io.open(f,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("cleared",n)