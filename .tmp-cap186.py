# -*- coding: utf-8 -*-
import json,io,os,glob,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\滊.json"
d=json.load(io.open(p,encoding="utf-8"))
for s in d["sections"]:
    if s["key"]=="shengmu":
        s["text"]="x「续消」取「消」：鹹水經日曬，水汽散失而鹽析出。"
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
n=0
for f in glob.glob(r"D:\系统汉字\web\public\cards\*.json"):
    t=io.open(f,encoding="utf-8").read()
    if "取一面" in t: n+=1
print("改滊；全库仍含「取一面」的卡",n)