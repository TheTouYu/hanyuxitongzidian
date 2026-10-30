# -*- coding: utf-8 -*-
import json,io,os,sys,shutil
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; P=r"D:\系统汉字\web\public\glyphs\photos"
p=os.path.join(C,"到.json"); d=json.load(io.open(p,encoding="utf-8"))
d["head"]="到（dào、侄zhì）"; d["aliases"]=["侄"]
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
idx=json.load(io.open(os.path.join(P,"index.json"),encoding="utf-8")); ph=idx.get("photos") or idx
print("箌 photos:",ph.get("箌"))
if ph.get("箌"):
    src=os.path.join(P,"箌"); bak=os.path.join(r"D:\系统汉字\intake","misassigned-箌")
    if os.path.isdir(src): shutil.copytree(src,bak,dirs_exist_ok=True); shutil.rmtree(src)
    ph.pop("箌",None)
    cap=json.load(io.open(os.path.join(P,"captions.json"),encoding="utf-8")); cm=cap.get("captions") or cap; cm.pop("箌",None)
    json.dump({"captions":cm},io.open(os.path.join(P,"captions.json"),"w",encoding="utf-8"),ensure_ascii=False)
json.dump({"photos":ph},io.open(os.path.join(P,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
print("done")