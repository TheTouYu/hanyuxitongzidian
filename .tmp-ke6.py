# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
d=json.load(io.open(os.path.join(C,"可.json"),encoding="utf-8")); n=0
chars=[]
for s in d["sections"]:
    if s.get("key")=="zizu":
        for g in s["groups"]:
            for r in g["rows"]:
                if not r[3].startswith("《"): r[3]="《"+r[3]; n+=1
                chars.append(r[0])
json.dump(d,io.open(os.path.join(C,"可.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
fixed=0
for ch in chars:
    p=os.path.join(C,ch+".json")
    if not os.path.exists(p): continue
    e=json.load(io.open(p,encoding="utf-8"))
    for s in e.get("sections",[]):
        if s.get("key")=="shiyi" and s.get("text") and not s["text"].startswith("《"):
            s["text"]="《"+s["text"]; fixed+=1
    json.dump(e,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("rows fixed",n,"cards fixed",fixed)