# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
spec={"𢼗":("赦","《龍龕》：「𢼗，俗；赦，正。」赦免。「赦」的訛字。"),
      "𤵫":("𤶣","《龍龕》：「𤵫，俗；𤶣，正。宅加、陟加二反。痂𤶣，瘡瘢痕也。」"),
      "𦊎":("罘","《正字通》：「張網。或曰罘譌作𦊎，誤。與四畫䍒同。」")}
for ch,(zheng,txt) in spec.items():
    p=rf"{C}\{ch}.json"; d=json.load(io.open(p,encoding="utf-8"))
    d["sections"]=[{"key":"shiyi","label":"释义","text":txt,"cites":[]},
                   {"key":"ezhi","label":"讹字说明","text":"形近「"+zheng+"」之訛；字見示部字族③組（原稿 p446–448）。","cites":[]}]
    d["sections"][1]["text"]=""
    if zheng=="𤶣": d["noRoot"]=True; d.pop("parent",None)
    else: d["parent"]=zheng
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("3 讹字卡改为两栏：释义＋讹字说明")