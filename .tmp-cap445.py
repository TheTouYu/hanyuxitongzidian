# -*- coding: utf-8 -*-
import json,io,os,re,sys,glob
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from PIL import Image
for p in glob.glob(r"D:\系统汉字\web\public\glyphs\photos\屐\*"):
    if p.lower().endswith((".jpg",".png")):
        im=Image.open(p); im.thumbnail((1400,1400))
        out=os.path.splitext(p)[0]+".jpg"; im.convert("RGB").save(out,quality=85)
        if out!=p: os.remove(p)
        print("resized",os.path.getsize(out))
P=r"D:\系统汉字\web\public\glyphs\photos"
ix=json.load(io.open(P+r"\index.json",encoding="utf-8")); k="photos" if "photos" in ix else None
(ix[k] if k else ix)["屐"]=["01.jpg"]
json.dump(ix,io.open(P+r"\index.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("index fixed")