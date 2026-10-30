# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
P=r"D:\系统汉字\web\public\glyphs\photos"
C=r"D:\系统汉字\web\public\cards"
files=sorted(os.listdir(os.path.join(P,"夷"))) if os.path.isdir(os.path.join(P,"夷")) else []
p=os.path.join(C,"夷.json"); d=json.load(io.open(p,encoding="utf-8"))
if files:
    d["photos"]=files; d["captions"]=["古中國的華夏與四夷分佈示意圖"]
    idx=json.load(io.open(os.path.join(P,"index.json"),encoding="utf-8")); ph=idx.get("photos") or idx
    ph["夷"]=files; json.dump({"photos":ph},io.open(os.path.join(P,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
    cap=json.load(io.open(os.path.join(P,"captions.json"),encoding="utf-8")); cm=cap.get("captions") or cap
    cm["夷"]=["古中國的華夏與四夷分佈示意圖"]
    json.dump({"captions":cm},io.open(os.path.join(P,"captions.json"),"w",encoding="utf-8"),ensure_ascii=False)
z=[s for s in d["sections"] if s["key"]=="zhuanyi"][0]
if "蹲踞" not in z["text"]:
    z["text"]=z["text"].rstrip()+"\n東夷民族喜歡蹲踞，這種姿勢被認為是傲慢無禮的。故引申指蹲踞；傲慢。《廣雅》：「踞也。」"
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("photos",files,"转义含蹲踞","蹲踞" in z["text"])