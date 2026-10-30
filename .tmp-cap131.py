# -*- coding: utf-8 -*-
import json,io,glob,sys,os
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
hit=[]
for f in glob.glob(C+r"\*.json"):
    if f.endswith("index.json"): continue
    d=json.load(io.open(f,encoding="utf-8"))
    for s in d.get("sections",[]):
        if s.get("key")=="shengmu" and "續而消" in (s.get("text") or ""):
            hit.append((d["char"],s["text"]))
print("命中旧句式:",len(hit),hit[:5])
for ch,txt in hit:
    p=os.path.join(C,ch+".json"); d=json.load(io.open(p,encoding="utf-8"))
    for s in d["sections"]:
        if s.get("key")=="shengmu":
            s["text"]=txt.replace("水續而消","溪水潺潺不斷，續而不絕").replace("續而消","續")
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("已改")