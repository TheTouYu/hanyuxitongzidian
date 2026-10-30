# -*- coding: utf-8 -*-
import io,json,glob,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; n=0
for f in glob.glob(C+r"\卷*.json"):
    d=json.load(io.open(f,encoding="utf-8"))
    keep=[]
    for s in d["sections"]:
        if s.get("key")=="zizu" or (s.get("key")!="js_音系" and any("部目" in (g.get("title") or "") for g in (s.get("groups") or []))):
            continue
        keep.append(s)
    if len(keep)!=len(d["sections"]):
        d["sections"]=keep; json.dump(d,io.open(f,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("清重复部目栏",n)
d=json.load(io.open(C+r"\卷八虎.json",encoding="utf-8"))
print([s["label"] for s in d["sections"]], len(d["sections"][-1]["groups"][0]["rows"]))