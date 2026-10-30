# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
G=r"D:\系统汉字\web\public\glyphs"; d=os.path.join(G,"科")
os.remove(os.path.join(d,"01.png"))
os.rename(os.path.join(d,"02.png"), os.path.join(d,"01.png"))
p=os.path.join(G,"index.json"); g=json.load(io.open(p,encoding="utf-8")); ch=g["chars"]
ch["科"]["files"]=["科/01.png"]
json.dump({"chars":ch},io.open(p,"w",encoding="utf-8"),ensure_ascii=False)
print(ch["科"]["files"])