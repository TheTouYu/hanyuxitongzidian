# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
fix={
"姉":"z「凿总」取「总」：姊為女兄，總率諸妹（推）。",
"巵":"zh「凿总」取「总」：酒器總酒於中（推）。",
"蕾":"l「拢离」取「拢」：花蕾攏聚未開（推）。",
"鈰":"sh「失收」取「失」：元素音譯，聲母記音（推）。",
"𠶴":"z「凿总」取「凿」：砸擊之聲如鑿（推）。",
"𢘥":"sh「失收」取「收」：恃者心持而收（推）。",
"𨸲":"sh「失收」取「收」：師聚眾而收（推）。",
"䫜":"零聲母（áo），緒論七組未列，不系（照實）。",
"𢝷":"j「聚决」取「聚」：借聲之字，聲母亦摹其音（推）。"}
for ch,t in fix.items():
    p=os.path.join(C,ch+".json"); d=json.load(io.open(p,encoding="utf-8"))
    sm=[s for s in d["sections"] if s["key"]=="shengmu"]
    if sm: sm[0]["text"]=t
    else: d["sections"].append({"key":"shengmu","label":"声母拟态","text":t,"cites":[]})
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("修 9 张")