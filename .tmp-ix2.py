# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\glyphs\index.json"
d=json.load(io.open(p,encoding="utf-8")); ch=d["chars"]
ch["或"]["photos"]=["01.png"]; ch.setdefault("棫",{}); ch["棫"]["photos"]=["01.jpg"]
json.dump({"chars":ch},io.open(p,"w",encoding="utf-8"),ensure_ascii=False)
print(ch["或"]["photos"],ch["棫"]["photos"])