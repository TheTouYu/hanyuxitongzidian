# -*- coding: utf-8 -*-
import json,io,os,sys,shutil
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
G=r"D:\系统汉字\web\public\glyphs"; P=os.path.join(G,"photos")
src=os.path.join(P,"虍","02.png"); dst=os.path.join(P,"琥"); os.makedirs(dst,exist_ok=True)
for f in os.listdir(dst): os.remove(os.path.join(dst,f))
shutil.move(src, os.path.join(dst,"01.png"))
for name,key,val in (("index.json","photos",{"虍":["01.png"],"琥":["01.png"]}),
                     ("captions.json","captions",{"虍":["伏鳥雙尾青銅虎（商）"],"琥":["虎符（戰國）"]})):
    p=os.path.join(P,name); d=json.load(io.open(p,encoding="utf-8")); m=d.get(key) or d
    m.update(val); json.dump({key:m},io.open(p,"w",encoding="utf-8"),ensure_ascii=False)
gi=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8"))
gi["photos"]["虍"]=[{"file":"photos/虍/01.png","caption":"伏鳥雙尾青銅虎（商）"}]
gi["photos"]["琥"]=[{"file":"photos/琥/01.png","caption":"虎符（戰國）"}]
json.dump(gi,io.open(os.path.join(G,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
print("moved")