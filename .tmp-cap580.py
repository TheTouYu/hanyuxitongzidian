# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
M={
"礩":"zh「凿总」取「总」：柱下石墩，荷重總承於下（推）。",
"躓":"zh「凿总」取「总」：物絆足下，行止而總（推）。",
"櫍":"zh「凿总」取「总」：鐘鼓架腳，力總於墊（推）。",
"劕":"zh「凿总」取「总」：契券兩書總合為憑（推）。",
"𧸲":"zh「凿总」取「总」：抵押之物總當於債（推）。",
"鑕":"zh「凿总」取「凿」：兩斤相合如鍘，合而斷之（推）。",
"懫":"zh「凿总」取「总」：忿戾之氣總塞於心（推）。",
"䑇":"zh「凿总」取「总」：刀箭瘡藥，藥力總敷於創（推）。",
"𨏑":"zh「凿总」取「总」：車前重載，重力總於前（推）。",
"𩧄":"zh「凿总」取「凿」：馬名借聲，聲母記音（推）。",
"𠘖":"zh「凿总」取「总」：身寒則筋脈總縮而抖（推）。",
"𡂒":"zh「凿总」取「凿」：野人言語質直，如鑿之透（推）。",
"儨":"zh「凿总」取「总」：正者總持不失（推）。",
"㜱":"zh「凿总」取「凿」：女字借聲（推）。",
"瓆":"zh「凿总」取「凿」：人名借聲（推）。",
"啠":"zh「凿总」取「凿」：智者照物如鑿之破（推）。",
"𧓳":"zh「凿总」取「凿」：螞蟥口器如利刃刺入皮肉吸血，取斧刃鋒利一面（推）。"}
n=0
for ch,t in M.items():
    p=os.path.join(C,ch+".json")
    if not os.path.exists(p): print("miss",ch); continue
    d=json.load(io.open(p,encoding="utf-8"))
    for s in d["sections"]:
        if s["key"]=="shengmu": s["text"]=t
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("改",n)