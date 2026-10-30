# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
pat=re.compile(r"^卷「\d+\.?[^」]*」[：:]?\s*")
n=0
for f in os.listdir(C):
    if not f.endswith(".json") or f in ("index.json","variants.json"): continue
    p=os.path.join(C,f)
    try: d=json.load(io.open(p,encoding="utf-8"))
    except: continue
    ch=False
    for s in d.get("sections",[]):
        t=s.get("text") or ""
        t2=pat.sub("",t)
        if t2!=t: s["text"]=t2; ch=True
    if ch:
        json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("清理",n)