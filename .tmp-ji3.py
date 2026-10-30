# -*- coding: utf-8 -*-
import json,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
z=json.load(open(rf"{C}\亟.json",encoding="utf-8"))
for s in z["sections"]:
    for g in s.get("groups",[]):
        for r in g["rows"]:
            if r[0]=="極":
                r[3]="《說文》「棟也」屋之中棟，引申至極、窮盡；今簡化作「极」（「极」本義為驢上負物之木版，見极卡，非同字）"
json.dump(z,open(rf"{C}\亟.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
极={"char":"极","trad":"极","simp":"","pinyin":"jí","level":3,"parent":"亟","bus":[{"num":6,"name":"乞"}],"sections":[
 {"key":"shiyi","label":"释义","text":"从木及聲：《說文》「驢上負也」，《篇海》「為木版跨驢背以負物者」——驢背上架物用的木版。","cites":[]},
 {"key":"shengmu","label":"声母拟态","text":"j「聚决」取「聚」：木版聚物而决（推）。","cites":[]},
 {"key":"jiezi","label":"借字说明","text":"「极」本有其字（驢上負物之木版），与「極」（屋棟、至極）无关；今以「极」為「極」的簡化，屬同音借用，故二字分卡。《說文》另有「极」字，非简化所造。","cites":[]}]}
json.dump(极,open(rf"{C}\极.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("ok")