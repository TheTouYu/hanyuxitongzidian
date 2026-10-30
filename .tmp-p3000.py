# -*- coding: utf-8 -*-
import json,io,os,shutil,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; P=r"D:\系统汉字\web\public\glyphs\photos"
ch="䙘"
d=os.path.join(P,ch)
if os.path.isdir(d): shutil.rmtree(d)
ip=os.path.join(P,"index.json"); m=json.load(io.open(ip,encoding="utf-8")); ph=m.get("photos") or m
ph.pop(ch,None); json.dump({"photos":ph},io.open(ip,"w",encoding="utf-8"),ensure_ascii=False)
cp=os.path.join(P,"captions.json"); c=json.load(io.open(cp,encoding="utf-8")); cm=c.get("captions") or c
cm.pop(ch,None); json.dump({"captions":cm},io.open(cp,"w",encoding="utf-8"),ensure_ascii=False)
p=os.path.join(C,ch+".json")
if os.path.exists(p):
    d2=json.load(io.open(p,encoding="utf-8")); d2.pop("photos",None); d2.pop("captions",None)
    json.dump(d2,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("removed",ch)