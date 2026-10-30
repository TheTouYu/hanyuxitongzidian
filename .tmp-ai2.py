# -*- coding: utf-8 -*-
import json,copy,sys,os
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
ai=json.load(open(rf"{C}\愛.json",encoding="utf-8"))
rows=[]
for g in ai["sections"][-1].get("groups",[]):
    for r in g["rows"]: rows.append(list(r))
extra={"曖":"暧","嬡":"嫒","璦":"瑷","靉":"叆","鑀":"锿","噯":"嗳"}
simp_rows=[]
for r in rows:
    ch=r[0]; sp=extra.get(ch)
    simp_rows.append([f"{ch}（{sp}）" if sp else ch]+r[1:])
d=copy.deepcopy(ai); d["char"]="爱"; d["trad"]="愛"; d["simp"]=""
for s in d["sections"]:
    if s["key"]=="benyi":
        s["text"]="字源依本字「愛」："+s["text"].split("：",1)[-1]
    if s["key"]=="zizu":
        s["text"]=""
        s["groups"]=[{"title":"①均以「愛」為聲旁","note":"","rows":simp_rows}]
json.dump(d,open(rf"{C}\爱.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("爱 卡已改为与愛同构，字族行",len(simp_rows))