# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
M={"㑵":"j「聚决」取「决」：嫉恨決裂於心（推）。",
"蒺":"j「聚决」取「决」：蒺藜之刺決裂肌膚（推）。",
"槉":"j「聚决」取「决」：屋枅決起而承重（推）。",
"螏":"j「聚决」取「决」：蜈蚣決起疾行（推）。",
"𨪏":"j「聚决」取「决」：鐵撾五指決張為爪（推）。",
"𠹋":"j「聚决」取「决」：聲決而出（推）。",
"𧪠":"j「聚决」取「决」：語急而決（推）。",
"𧽑":"j「聚决」取「决」：走疾而決（推）。"}
n=0
for ch,t in M.items():
    p=os.path.join(C,ch+".json")
    if not os.path.exists(p): print("miss",ch); continue
    d=json.load(io.open(p,encoding="utf-8"))
    for s in d["sections"]:
        if s["key"]=="shengmu": s["text"]=t
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("改",n)