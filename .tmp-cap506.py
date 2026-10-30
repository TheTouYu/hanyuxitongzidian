# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
hdr=0;bian=0;prose=0;lines=[]
for fn in os.listdir(C):
    if not fn.endswith(".json") or fn=="index.json": continue
    d=json.load(io.open(os.path.join(C,fn),encoding="utf-8"))
    sm=[s for s in d.get("sections") or [] if s.get("key")=="shengmu"]
    if not sm: continue
    t=(sm[0].get("text") or "").strip()
    if "聲母義（" in t: hdr+=1; lines.append(("H",fn[:-5],t[:40]))
    elif "辨證" in t or "辯證" in t: bian+=1; lines.append(("B",fn[:-5],t[:40]))
    elif "取「" not in t: prose+=1; lines.append(("P",fn[:-5],t[:40]))
print("旧表头",hdr,"辨証混入",bian,"散文",prose)
for x in (lines[:6]): print(x)