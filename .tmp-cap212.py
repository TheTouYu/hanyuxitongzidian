# -*- coding: utf-8 -*-
import json,io,glob,os,sys,re,collections
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
# 亙 改回二级 + 字族
p=os.path.join(C,"亙.json")
if os.path.exists(p):
    d=json.load(io.open(p,encoding="utf-8")); d["level"]=2; d["parent"]="乞"
    keys={s["key"] for s in d["sections"]}
    if "zizu" not in keys:
        d["sections"].append({"key":"zizu","label":"字族衍义","cites":[],"text":"亙系：",
          "groups":[{"title":"①回環往復","note":"","rows":[
            ["恆","héng","心","《說文》「常也」；亘取迴環往復之常，故从心"],
            ["絙","gēng","糸","《說文》「大索也」；繩索迴環而亘"],
            ["亙","gèn","二","《說文》「求回也」；本象迴環之形"]]}]})
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); print("亙 fixed")
# 缺声母的部1-10三级卡：按父字根声母组给「照实」或择面
cnt=collections.Counter(); n=0
for f in glob.glob(C+r"\*.json"):
    if os.path.basename(f) in ("index.json","variants.json"): continue
    d=json.load(io.open(f,encoding="utf-8"))
    bus=d.get("bus") or []
    num=bus[0].get("num") if bus and isinstance(bus[0],dict) else None
    if not isinstance(num,int) or not(1<=num<=10): continue
    if d.get("level")!=3: continue
    keys={s["key"] for s in d["sections"]}
    if "shengmu" in keys: continue
    par=d.get("parent") or ""
    if par in ("矣","㠯"): txt="聲符"+par+"為零聲母，緒論七組未列，不系（照實）。"
    elif par=="台": txt="台多讀（yí／tái／sì），聲母不系（照實）。"
    elif par=="氐": txt="d「囤动」取「囤」：氐為根柢之形，諸字多聚於下（推）。"
    else: txt="聲母擬態待按字義定面（聲符"+par+"，原稿未單列）。"
    d["sections"].append({"key":"shengmu","label":"声母拟态","text":txt,"cites":[]})
    json.dump(d,io.open(f,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1; cnt[par]+=1
print("补声母",n,dict(cnt))