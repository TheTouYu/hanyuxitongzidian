# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\glyphs\index.json"
ix=json.load(io.open(p,encoding="utf-8")); ch=ix["chars"]
h=ch.get("戈") or {"doc":"","variants":[],"files":[]}
h["photos"]=["戈/01.jpg"]; ch["戈"]=h
json.dump({"chars":ch},io.open(p,"w",encoding="utf-8"),ensure_ascii=False)
print("ok",h["photos"],len(h["files"]))