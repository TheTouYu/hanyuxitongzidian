# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
M={
"愾":"x「续消」取「消」：太息連連，氣漸消盡。",
"慨":"k「口控」取「口」：慨歎出聲，口張而氣放。",
"歖":"x「续消」取「续」：笑聲相連不絕。",
"杴":"x「续消」取「续」：鍬入土，一下接一下。",
"渇":"k「口控」取「缺」：口張求飲，水缺而不得。",
"赩":"x「续消」取「续」：赤色濃而相續。",
"鎎":"x「续消」取「消」：金氣漸散而消。",
"𤸎":"k「口控」取「缺」：熱病口渴，水缺而思飲。",
"刺":"c「刺持」取「刺」：刀刺入而傷。",
"㔠":"x「续消」取「续」：力相接而不斷。",
}
n=0
for ch,txt in M.items():
    p=os.path.join(C,ch+".json")
    if not os.path.exists(p): print("缺",ch); continue
    d=json.load(io.open(p,encoding="utf-8"))
    for s in d["sections"]:
        if s.get("key")=="shengmu": s["text"]=txt
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("改",n)