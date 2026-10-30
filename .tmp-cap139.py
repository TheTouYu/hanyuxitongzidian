# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
M={
"谿":"x「续消」取「续」：山中溝渠細長，水續而不斷。",
"嵠":"x「续消」取「续」：溪谷細長相連。",
"徯":"x「续消」取「续」：等待需時而續望。",
"榽":"x「续消」取「续」：木細葉似檀，枝葉細長相連（推）。",
"蒵":"x「续消」取「续」：款冬蔓生相連（推）。",
"傒":"x「续消」取「续」：等待而時續時望（推）。",
"縘":"x「续消」取「续」：繫而續不斷。",
"㨙":"x「续消」取「续」：挾扶而手相牽連。",
"膎":"x「续消」取「续」：乾肉以繩繫而懸（推）。",
"鞵":"x「续消」取「续」：鞋以繩繫於足（推）。",
"𡰄":"x「续消」取「续」：不能行，為人所引，續牽而行。",
"雞":"j「聚决」取「聚」：雞群聚而棲（推）。",
"𥰥":"x「续消」取「续」：安船之竹索，繫而續不斷。",
"𥉐":"q「亲缺」取「缺」：目動如有所繫而時缺（推）。",
"騱":"x「续消」取「续」：野馬群行相連續（推）。",
"鼷":"x「续消」取「续」：小鼠崽牽連母腹（推）。",
"豯":"x「续消」取「续」：三月豚腹豯豯，幼小牽連（推）。",
"貕":"x「续消」取「续」：豬子牽連成群（推）。",
"𤳤":"q「亲缺」取「缺」：小畚箕，器小而口有缺（推）。",
"謑":"x「续消」取「续」：恥辱連綿在心（推）。",
"慀":"x「续消」取「续」：心不平，情緒纏綿（推）。",
"螇":"x「续消」取「续」：知了鳴聲連續不斷。",
"㜎":"x「续消」取「续」：女奴以繩繫屬（推）。",
"𪓷":"x「续消」取「续」：水蟲牽連群游（推）。",
"𦫬":"x「续消」取「续」：黃疸病色連綿（推）。",
"鸂":"x「续消」取「续」：水鳥相隨成對（推）。"}
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
print("已改",len(M))