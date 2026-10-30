# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷五  雁.docx").paragraphs]
C=r"D:\系统汉字\web\public\cards"
p=os.path.join(C,"戹.json"); d=json.load(io.open(p,encoding="utf-8"))
g3={"no":"③","title":"音譯字","rows":[["苊","è","","碳氫化合物的一類，無色針狀結晶，溶于熱酒精，可做媒染劑。英文acenaphthene的音譯。"]]}
for s in d["sections"]:
    if s["key"]=="zizu":
        s["groups"]=[g for g in s["groups"] if g.get("no")!="③"]+[g3]
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
# 苊 族卡
card={"char":"苊","head":"苊","pinyin":"è","level":3,"parent":"戹","bus":[{"num":38,"name":"厄"}],
 "sections":[{"key":"shiyi","label":"释义","text":ps[540].split("：",1)[1] if "：" in ps[540] else ps[540]},
  {"key":"shengmu","label":"声母拟态","text":"e「零聲母」不系：影母字今讀零聲母，緒論七組未列（照實）。"},
  {"key":"suoshujuan","label":"所属卷","links":[{"ch":"卷五雁","label":"卷五 雁"}]}]}
json.dump(card,io.open(os.path.join(C,"苊.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("ok")