# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
C=r"D:\系统汉字\web\public\cards"
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷七  斤.docx").paragraphs]
benyi=ps[84].replace("本義：","",1)
rows=[["齭","chǔ","齒",ps[86]],["乺","suǒ",""," " + ps[87]],["㫹","shù","日",ps[88]]]
card={"char":"所","head":"所（𢨷）","pinyin":"suǒ / shǔ","bus":{"num":44,"name":"斤"},"parent":"斤","level":2,
 "aliases":["𢨷"],
 "sections":[
  {"key":"benyi","label":"本义","text":benyi,"cites":[]},
  {"key":"shengmu","label":"声母拟态","text":"sh「失收」取「收」：聚物之處曰所，物有所歸（推）。","cites":[]},
  {"key":"zizu","label":"字族衍义","groups":[{"no":"","title":"未形成字族（原文列齭、乺、㫹三字）","rows":rows}],"cites":[]},
  {"key":"suoshujuan","label":"所属卷","text":"","links":[{"ch":"卷七斤","label":"卷七 斤"}]}]}
json.dump(card,io.open(os.path.join(C,"所.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
for ch,py,lei,tx in rows:
    p=os.path.join(C,ch+".json")
    if os.path.exists(p): continue
    c={"char":ch,"head":ch,"pinyin":py,"bus":{"num":44,"name":"斤"},"parent":"所","level":3,"aliases":[],
       "sections":[{"key":"shiyi","label":"释义","text":tx,"cites":[]},
                   {"key":"shengmu","label":"声母拟态","text":"s「失收」：聲符取義隨文（推）。","cites":[]},
                   {"key":"suoshujuan","label":"所属卷","text":"","links":[{"ch":"卷七斤","label":"卷七 斤"}]}]}
    json.dump(c,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("ok")