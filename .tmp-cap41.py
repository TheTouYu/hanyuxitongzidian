# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
d={"char":"貍","trad":"貍","simp":"狸","pinyin":"lí","level":2,"parent":"士","bus":[{"num":9,"name":"士"}],
"head":"貍（狸）","aliases":["狸"],
"sections":[
 {"key":"benyi","label":"本义","text":"貍，lí：即山貓。西周金文所从為貍的象形；因其晝伏夜出，棲息于社林中，喜歡將吃剩的食物、拉的糞便埋藏起來，故从「里」聲。《說文》：「伏獸，似貙。从豸里聲。里之切。」《段注》：「即俗所謂野貓。」《正字通》：「狸，野貓也。有數種：大小似狐，毛雜黃黑，有斑如貓。」","cites":[]},
 {"key":"zhuanyi","label":"转义","text":"由「伏藏」引申为潜藏、伏匿；又指貍的毛皮（《詩》「取彼狐貍，為公子裘」）。","cites":[]},
 {"key":"bianzheng","label":"辩证","text":"《說文》析為「从豸里聲」不全面：所从之「里」在西周金文中本作貍的象形（伏獸），後象形訛變為「里」，非單純表音；「豸」為後加形旁。","cites":[]},
 {"key":"yinyuan","label":"音源","text":"音源：其本音應為 mái，源于山貓的叫聲。因其象形字後來演化作形旁「豸」或「犬」，迷失了本音。","cites":[]},
 {"key":"shengmu","label":"声母拟态","text":"m「蒙末」取「蒙」：山貓晝伏夜出、蒙蔽而伏（推）。","cites":[]},
 {"key":"zizu","label":"字族衍义","text":"字族衍义：","groups":[
  {"title":"①埋藏、填塞、遮蔽","note":"","rows":[
   ["薶","mái","艸","《說文》「瘞也」埋葬，《爾雅》「塞也」填塞；取貍之「伏藏食物糞便」義，故从艸（掩於草土之下）"],
   ["霾","mái","雨","《說文》「風雨土也」，《釋名》「晦也，言如物塵晦之色也」；取貍之「伏藏、隱晦」義，故从雨（土蔽天如埋）"],
   ["㦟","mái","心","《集韻》與「埋」同，藏也；貍聲，取伏藏義"]]}]}]}
json.dump(d,io.open(rf"{C}\貍.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
for f in ("狸",):
    import os
    p=rf"{C}\{f}.json"
    if os.path.exists(p):
        x=json.load(io.open(p,encoding="utf-8")); x["hidden"]=True; x["trad"]="貍"
        json.dump(x,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("貍 rewritten")