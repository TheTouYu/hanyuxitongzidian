# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
n=0
for f in os.listdir(C):
    if not f.endswith(".json") or f=="index.json": continue
    p=os.path.join(C,f)
    try: d=json.load(io.open(p,encoding="utf-8"))
    except Exception: continue
    if not isinstance(d,dict): continue
    ss=d.get("sections",[])
    s2=[s for s in ss if s.get("key")!="shangji"]
    if len(s2)!=len(ss):
        d["sections"]=s2; json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("去上级字根栏",n)