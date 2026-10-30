# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
ROOT=r"D:\系统汉字"; C=os.path.join(ROOT,"web","public","cards")
z=json.load(io.open(os.path.join(ROOT,"web","public","zigen.json"),encoding="utf-8"))
by=z["byName"]
fixed=[]; miss=[]
for ch,info in by.items():
    p=os.path.join(C,ch+".json")
    if not os.path.exists(p): miss.append(ch); continue
    d=json.load(io.open(p,encoding="utf-8"))
    chg=False
    if d.get("level")!=1: d["level"]=1; chg=True
    if d.get("parent"): d["parent"]=""; chg=True
    if d.get("rootLevel"): d.pop("rootLevel",None); chg=True
    if chg:
        json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); fixed.append(ch)
print("修正部头",len(fixed),"缺卡",len(miss))
print(("例："+ "、".join(fixed[:12])) if fixed else "")