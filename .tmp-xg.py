# -*- coding: utf-8 -*-
import json,io,os,shutil,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
G=r"D:\系统汉字\web\public\glyphs"; C=r"D:\系统汉字\web\public\cards"
src=os.path.join(G,"訢"); dst=os.path.join(G,"欣")
if os.path.isdir(src):
    for f in sorted(os.listdir(src)):
        shutil.copy2(os.path.join(src,f), os.path.join(dst,"x_"+f))
    print("copied",os.listdir(dst))
p=os.path.join(G,"index.json"); g=json.load(io.open(p,encoding="utf-8"))
g["chars"]["欣"]["files"]=sorted(g["chars"]["欣"].get("files",[])+["欣/x_01.png","欣/x_02.png"])
json.dump({"chars":g["chars"]},io.open(p,"w",encoding="utf-8"),ensure_ascii=False)
print(g["chars"]["欣"]["files"])