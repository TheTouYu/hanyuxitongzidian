# -*- coding: utf-8 -*-
import json,io,glob,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
cm=json.load(io.open(r"D:\系统汉字\.tmp-charmap.json",encoding="utf-8"))
n=0; miss=0
for f in glob.glob(C+r"\*.json"):
    b=os.path.basename(f)
    if b in ("index.json","variants.json"): continue
    d=json.load(io.open(f,encoding="utf-8"))
    if d.get("bus"): continue
    ch=d.get("char"); it=cm.get(ch)
    if not it: miss+=1; continue
    d["bus"]=[{"num":it["bu"],"name":it["nm"]}]
    if not d.get("level"): d["level"]=3
    if not d.get("parent"): d["parent"]=it["nm"]
    if not d.get("pinyin"): d["pinyin"]=it["py"]
    for s in d["sections"]:
        if s.get("key")=="bengen" and not (s.get("text") or "").strip() and not s.get("groups"):
            s["text"]=it["txt"][:400]
    json.dump(d,io.open(f,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("修复",n,"未命中",miss)