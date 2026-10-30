# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
G=r"D:\系统汉字\web\public\glyphs"
d=os.path.join(G,"欣")
for f in os.listdir(d):
    if f.startswith("x_"): os.remove(os.path.join(d,f))
p=os.path.join(G,"index.json"); g=json.load(io.open(p,encoding="utf-8"))
g["chars"]["欣"]["files"]=[f for f in g["chars"]["欣"]["files"] if "/x_" not in f]
json.dump({"chars":g["chars"]},io.open(p,"w",encoding="utf-8"),ensure_ascii=False)
print(g["chars"]["欣"]["files"])