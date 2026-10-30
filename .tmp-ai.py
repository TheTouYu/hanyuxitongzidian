# -*- coding: utf-8 -*-
import json,copy,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
ai=json.load(open(rf"{C}\㤅.json",encoding="utf-8"))
ai["simp"]="愛"
json.dump(ai,open(rf"{C}\㤅.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
def mirror(src,new,trad,simp,lv=2,par="欠"):
    d=copy.deepcopy(src); d["char"]=new; d["trad"]=trad; d["simp"]=simp; d["level"]=lv; d["parent"]=par
    for s in d["sections"]:
        if s["key"]=="benyi":
            s["text"]=f"字源依本字「{trad}」："+s["text"].split("：",1)[-1]
    json.dump(d,open(rf"{C}\{new}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
mirror(ai,"愛","愛","爱"); mirror(ai,"爱","愛","")
pairs=[("嗳","噯"),("暧","曖"),("嫒","嬡"),("瑷","璦"),("叆","靉"),("锿","鑀")]
for t,tr in pairs:
    src=json.load(open(rf"{C}\{tr}.json",encoding="utf-8"))
    d=copy.deepcopy(src); d["char"]=t; d["trad"]=tr; d["simp"]=""; d["level"]=3; d["parent"]="㤅"
    for s in d["sections"]:
        if s["key"] in ("shiyi","benyi"):
            s["text"]=f"字源依本字「{tr}」："+s["text"].split("：",1)[-1]
    json.dump(d,open(rf"{C}\{t}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("愛/爱 + 6 简体谐声卡已建")