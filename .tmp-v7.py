# -*- coding: utf-8 -*-
import io,json,glob,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
# 卷卡：部链接栏改名并按部号排序放最后
d=json.load(io.open(rf"{C}\卷一雞.json",encoding="utf-8"))
for s in d["sections"]:
    if s.get("key")=="juan":
        s["label"]="直接链接：第1–7部"
        s["links"]=sorted(s["links"],key=lambda l:int(l["label"].split()[0]))
d["sections"]=[s for s in d["sections"] if s.get("key")!="juan"]+[s for s in d["sections"] if s.get("key")=="juan"]
json.dump(d,io.open(rf"{C}\卷一雞.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
n=0; miss=0
for fp in glob.glob(C+r"\*.json"):
    if fp.endswith("index.json") or fp.endswith("variants.json"): continue
    c=json.load(io.open(fp,encoding="utf-8")); bus=c.get("bus") or []
    num=bus[0].get("num") if bus and isinstance(bus[0],dict) else None
    if isinstance(num,int) and 1<=num<=7:
        js=[s for s in c.get("sections",[]) if s.get("key")=="juan"]
        if js and any(l.get("ch")=="卷一雞" for l in js[0].get("links",[])): n+=1
        else: miss+=1
print("部1-7卡带卷一链接",n,"缺",miss)
h=io.open(r"D:\系统汉字\web\public\test.html",encoding="utf-8").read()
i=h.find("const LKR="); print(h[i:i+150])