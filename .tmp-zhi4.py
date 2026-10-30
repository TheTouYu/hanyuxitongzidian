# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
M={
 "奪":"d「囤動」取「囤」：爪抓而囤取，聚而奪之（推）。",
 "𠔟":"d「囤動」取「囤」：同奪，聚而取之（推）。",
 "䨥":"h「豁活」取「豁」：大雨開豁而下（推）。",
 "愯":"s「失收」取「收」：懼而收攝（推）。",
 "𢊄":"h「豁活」取「活」：姿態流動（推）。",
 "㸕":"j「聚決」取「聚」：攫而聚取（推）。",
 "㨦":"s「失收」取「收」：執而收持（推）。",
 "䉟":"h「豁活」取「活」：竹器活絡可開闔（推）。",
 "篗":"y「零聲母」不系：零聲母，緒論七組未列（照實）。",
 "𩹹":"h「豁活」取「豁」：魚口開闊（推）。",
 "𥻬":"zh「凿总」取「凿」：營治如凿之入（推）。",
}
n=0
for c,t in M.items():
    p=os.path.join(C,c+".json"); d=json.load(io.open(p,encoding="utf-8"))
    for s in d["sections"]:
        if s.get("key")=="shengmu": s["text"]=t; n+=1
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("patched",n)