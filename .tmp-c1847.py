# -*- coding: utf-8 -*-
import json,io,os,shutil,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
P=r"D:\系统汉字\web\public\glyphs\photos"
d=os.path.join(P,"己"); os.makedirs(d,exist_ok=True)
shutil.copy(r"D:\系统汉字\.tmp-img0.jpg", os.path.join(d,"01.jpg"))
ip=os.path.join(P,"index.json"); ph=json.load(io.open(ip,encoding="utf-8"))["photos"]
ph["己"]=["01.jpg"]
json.dump({"photos":ph},io.open(ip,"w",encoding="utf-8"),ensure_ascii=False)
c=r"D:\系统汉字\web\public\cards\己.json"
if os.path.exists(c):
    j=json.load(io.open(c,encoding="utf-8")); j["photos"]=["01.jpg"]
    json.dump(j,io.open(c,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("己 插图归位")