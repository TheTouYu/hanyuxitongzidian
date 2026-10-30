# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
gi=json.load(io.open(r"D:\系统汉字\web\public\glyphs\index.json",encoding="utf-8"))
files=(gi.get("炙") or {}).get("files",[])
p=os.path.join(C,"炙.json"); d=json.load(io.open(p,encoding="utf-8"))
for s in d["sections"]:
    if s.get("key")=="zizu":
        for i,g in enumerate(s["groups"],1): g["no"]="①②③④⑤⑥"[i-1]
keys=[s.get("key") for s in d["sections"]]
if "zixing" not in keys:
    i=next((k for k,s in enumerate(d["sections"]) if s.get("key")=="zizu"),len(d["sections"]))
    d["sections"].insert(i,{"key":"zixing","label":"字形","files":files})
if "suoshujuan" not in keys:
    d["sections"].append({"key":"suoshujuan","label":"所属卷","text":"卷七 斤（第47部 炙）","links":[{"ch":"卷七斤","label":"卷七 斤"}]})
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
# 族字卡补所属卷
for ch in ["䂹","𠶨","𣇧","𣶋","𨂂"]:
    q=os.path.join(C,ch+".json")
    if not os.path.exists(q): continue
    c=json.load(io.open(q,encoding="utf-8"))
    if not any(s.get("key")=="suoshujuan" for s in c["sections"]):
        c["sections"].append({"key":"suoshujuan","label":"所属卷","text":"卷七 斤（第47部 炙）","links":[{"ch":"卷七斤","label":"卷七 斤"}]})
    json.dump(c,io.open(q,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("ok",files)