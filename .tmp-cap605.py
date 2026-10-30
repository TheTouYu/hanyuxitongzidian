# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
M={"倁":"zh「凿总」取「总」：行走往來，總集於一途（推）。",
"痴":"ch「刺持」取「持」：癡人執持一念而不放（推）。",
"聟":"x「续消」取「续」：女夫續嗣，血脈相續（推）。",
"踟":"ch「刺持」取「持」：持足而卻行不進（推）。",
"𢔊":"ch「刺持」取「持」：行而持重，不輕發（推）。",
"𢛍":"zh「凿总」取「凿」：心意快利如鑿（推）。",
"𩳦":"ch「刺持」取「刺」：鬼魅刺人而迷（推）。",
"𪑜":"zh「凿总」取「总」：草書筆勢總連（推）。",
"䝷":"zh「凿总」取「凿」：以財質當，鑿定其信（推）。",
"𦝔":"zh「凿总」取「总」：皮肉總聚而起繭（推）。",
"𨢮":"zh「凿总」取「总」：酒味總厚（推）。",
"𥇭":"zh「凿总」取「凿」：目察如鑿，洞見隱微（推）。",
"𥏯":"zh「凿总」取「凿」：水鑿土而得水（推）。",
"䵹":"zh「凿总」取「凿」：蛛絲鑿空而織（推）。",
"㲛":"zh「凿总」取「总」：獸毛總聚而多（推）。",
"𥏴":"j「聚决」取「聚」：箭創聚痛（推）。",
"䓡":"zh「凿总」取「总」：知母根鬚總聚如毛（推）。",
"𠕧":"j「聚决」取「聚」：矯詐聚言（推）。"}
n=0
for ch,t in M.items():
    p=os.path.join(C,ch+".json")
    if not os.path.exists(p): print("miss",ch); continue
    d=json.load(io.open(p,encoding="utf-8"))
    for s in d["sections"]:
        if s["key"]=="shengmu": s["text"]=t
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
ph=0
for f in os.listdir(C):
    if not f.endswith(".json") or f=="index.json": continue
    try: d=json.load(io.open(os.path.join(C,f),encoding="utf-8"))
    except Exception: continue
    if not isinstance(d,dict): continue
    for s in d.get("sections",[]):
        if isinstance(s,dict) and s.get("key")=="shengmu" and ("「—」" in s.get("text","")):
            ph+=1
print("写入",n,"全库余占位",ph)