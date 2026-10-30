# -*- coding: utf-8 -*-
import json,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
j=json.load(open(rf"{C}\傑.json",encoding="utf-8"))
j["simp"]="杰"; j["aliases"]=["杰","偈"]
for s in j["sections"]:
    if s.get("key")=="shiyi":
        s["text"]="从人桀聲：《說文》「傲也」，《廣韻》「英傑，特立也。又俊也」——才德特立出眾者。原稿列「傑（杰偈）」，杰為其簡化俗體、偈為其異寫（偈偈，用力皃）。"
json.dump(j,open(rf"{C}\傑.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
jie={"char":"杰","trad":"傑","simp":"杰","pinyin":"jié","level":3,"parent":"桀","bus":[{"num":7,"name":"桀"}],"sections":[
 {"key":"shiyi","label":"释义","text":"傑的簡化俗體：从人桀聲，才德特立出眾者（《廣韻》「英傑，特立也」）。字源依本字「傑」，說見傑卡。","cites":[]},
 {"key":"shengmu","label":"声母拟态","text":"j「聚决」取「决」：特立而决（推）。","cites":[]},
 {"key":"jiezi","label":"借字说明","text":"「杰」與「傑」音義全同、僅寫法不同（人桀聲之省變），屬同字簡化，故二字各存卡、字源並從「傑」。","cites":[]}]}
json.dump(jie,open(rf"{C}\杰.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("ok")