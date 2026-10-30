# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
G=r"D:\系统汉字\web\public\glyphs"
p=os.path.join(G,"index.json"); ix=json.load(io.open(p,encoding="utf-8"))
ph=ix.get("photos") or {}
pics={"羲":("羲/01.png","白鵝斂翅而鳴"),"㰕":("㰕/01.png","羊首勺（商）"),"義":("義/01.png","牛首形杆飾（商）")}
for k,(f,c) in pics.items(): ph[k]=[{"file":f,"caption":c}]
ix["photos"]=ph
json.dump(ix,io.open(p,"w",encoding="utf-8"),ensure_ascii=False)
print("photos keys",len(ph))