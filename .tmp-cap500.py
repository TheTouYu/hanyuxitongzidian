# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
fix={
 "技":"j「聚决」取「聚」：技藝須聚精會神、聚巧於手而後成（推）。",
 "妓":"j「聚决」取「聚」：女樂聚眾而歌、聚人而觀（推）。",
 "䰙":"零聲母（yǐ），緒論七組未列，不系（照實）。"}
for ch,t in fix.items():
    p=os.path.join(C,ch+".json"); d=json.load(io.open(p,encoding="utf-8"))
    for s in d["sections"]:
        if s["key"]=="shengmu": s["text"]=t
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
# 全库统计占位
bad=[]
for fn in os.listdir(C):
    if not fn.endswith(".json") or fn=="index.json": continue
    d=json.load(io.open(os.path.join(C,fn),encoding="utf-8"))
    for s in d.get("sections") or []:
        t=s.get("text") or ""
        if "取绪论拟态义一面" in t or "取一面：" in t or "拟态义一面" in t:
            bad.append(fn[:-5]); break
print("占位卡",len(bad),bad[:20])