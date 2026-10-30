# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
P=r"D:\系统汉字\web\public\glyphs\photos"
idx=json.load(io.open(os.path.join(P,"index.json"),encoding="utf-8")); ph=idx["photos"]
cap=json.load(io.open(os.path.join(P,"captions.json"),encoding="utf-8")); cm=cap["captions"]
add={"汥":"01.jpg","鳷":"01.jpg","技":"01.jpg","䰙":"01.png"}
for ch,fn in add.items(): ph[ch]=[fn]
cm["技"]=["東漢畫像磚《斜索技》"]; cm["䰙"]=["唐三彩三足鍑"]
json.dump({"photos":ph},io.open(os.path.join(P,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
json.dump({"captions":cm},io.open(os.path.join(P,"captions.json"),"w",encoding="utf-8"),ensure_ascii=False)
print(len(ph),len(cm),ph.get("汥"),cm.get("技"))