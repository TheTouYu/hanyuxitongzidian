# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
M={
"鉙":"zh「凿总」取「总」：金屬聚而成塊（推）。",
"齞":"y 为零声母，绪论七组未列，不系（照实）。",
"𣲵":"zh「凿总」取「凿」：𣲵水多箴魚，其喙如箴（針），尖利刺物。",
"軹":"zh「凿总」取「凿」：車轂末端穿軸之小孔，如凿穿而成。",
"抧":"zh「凿总」取「凿」：張開指爪，指端如凿刺。",
"疻":"zh「凿总」取「凿」：毆打造成傷，如凿擊而入。",
"𧲻":"zh「凿总」取「凿」：豹犬齒爪尖利（推）。",
"䳅":"zh「凿总」取「凿」：原雞之距尖利（推）。",
"胑":"zh「凿总」取「总」：四胑總聚於身（推）。",
"咫":"zh「凿总」取「总」：以指總聚丈量，八寸為咫（推）。",
"䅩":"zh「凿总」取「总」：多小意而總聚止息（推）。",
"伿":"y 为零声母，绪论七组未列，不系（照实）。",
"𧧹":"x「续消」取「续」：等待綿延不斷（推）。",
"𨒅":"q「亲缺」取「缺」：曲折行走，路有缺折（推）。",
"㰨":"x「续消」取「续」：打鳴氣逆，氣息斷而復續（推）。",
"嘦":"j「聚决」取「聚」：只要，總聚而取其一（推）。",
"𠙂":"c「刺持」取「持」：音從，無義可說，記作借聲。",
"𫪩":"j「聚决」取「聚」：只有，聚而專一（推）。"}
for ch,txt in M.items():
    p=os.path.join(C,ch+".json")
    if not os.path.exists(p): print("缺卡",ch); continue
    d=json.load(io.open(p,encoding="utf-8")); secs=d["sections"]
    if not any(s.get("key")=="shengmu" for s in secs):
        secs.append({"key":"shengmu","label":"声母拟态","text":txt,"cites":[]})
    else:
        for s in secs:
            if s.get("key")=="shengmu": s["text"]=txt
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("已改",len(M),"张")