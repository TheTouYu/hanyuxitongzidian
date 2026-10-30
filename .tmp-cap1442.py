# -*- coding: utf-8 -*-
import json,io,os,shutil,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
P=r"D:\系统汉字\web\public\glyphs\photos"; C=r"D:\系统汉字\web\public\cards"
for ch in ("責",):
    d=os.path.join(P,ch)
    if os.path.isdir(d): shutil.rmtree(d)
    for name,key in (("index.json","photos"),("captions.json","captions")):
        p=os.path.join(P,name); j=json.load(io.open(p,encoding="utf-8")); j[key].pop(ch,None)
        json.dump(j,io.open(p,"w",encoding="utf-8"),ensure_ascii=False)
    cp=os.path.join(C,ch+".json"); cd=json.load(io.open(cp,encoding="utf-8"))
    cd.pop("photos",None); cd.pop("captions",None)
    json.dump(cd,io.open(cp,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    print("清",ch)