# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
src=json.load(io.open(rf"{C}\祟.json",encoding="utf-8"))
rows=[r for s in src["sections"] for g in (s.get("groups") or []) for r in g["rows"]]
made=[];skip=[]
for r in rows:
    raw=r[0]; m=re.match(r"^([^（(]+)[（(]([^）)]*)[）)]$",raw)
    ch=m.group(1) if m else raw; al=[c for c in (m.group(2) if m else "") if c.strip()]
    if os.path.exists(rf"{C}\{ch}.json"): skip.append(ch); continue
    d={"char":ch,"pinyin":r[1],"level":3,"parent":"祟","bus":[{"num":10,"name":"示"}],
       "sections":[{"key":"shiyi","label":"释义","text":r[3],"cites":[]}]}
    if al: d["head"]=raw; d["aliases"]=al
    json.dump(d,io.open(rf"{C}\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1); made.append(ch)
print("新建",len(made),made,"已有",len(skip),skip)