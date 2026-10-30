# -*- coding: utf-8 -*-
import json,io,os,shutil,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
P=r"D:\系统汉字\web\public\glyphs\photos"; C=r"D:\系统汉字\web\public\cards"
ip=os.path.join(P,"index.json"); cp=os.path.join(P,"captions.json")
ph=json.load(io.open(ip,encoding="utf-8"))["photos"]; ca=json.load(io.open(cp,encoding="utf-8"))["captions"]
removed=[]
for ch in list(ph.keys()):
    if ca.get(ch): continue
    removed.append(ch); ph.pop(ch,None)
    d=os.path.join(P,ch)
    if os.path.isdir(d): shutil.rmtree(d)
    fp=os.path.join(C,ch+".json")
    if os.path.exists(fp):
        j=json.load(io.open(fp,encoding="utf-8")); j.pop("photos",None); j.pop("captions",None)
        json.dump(j,io.open(fp,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
json.dump({"photos":ph},io.open(ip,"w",encoding="utf-8"),ensure_ascii=False)
print("删无原文图注的图",len(removed))
print(removed[:20])