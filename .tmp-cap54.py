# -*- coding: utf-8 -*-
import sys,json,io,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
f=r"D:\字谱智能体\卷卌一 殳.docx"; ps=[p.text.strip() for p in Document(f).paragraphs]
num,name=None,None
for i in range(60,-1,-1):
    m=re.match(r"^(\d{1,3})[.．]\s*(\S{1,2})部$", ps[i])
    if m: num,name=int(m.group(1)),m.group(2); break
d={"char":"豛","trad":"豛","simp":"","pinyin":"yì","level":3,"parent":"殳","bus":[{"num":num or 0,"name":name or "殳"}],
"sections":[
 {"key":"benyi","label":"本义","text":"豛，yì：《說文》「上谷名豬豭。从豕，役省聲。營只切。」上谷（地名）把公豬叫作「豛」；从「豕」表類，从「役」省聲。","cites":[]},
 {"key":"bianzheng","label":"辩证","text":"《玉篇》：「齧豕。」——疑指野豬：有獠牙似「殳」，受驚時撞向對方（原稿按語）。","cites":[]},
 {"key":"yinyuan","label":"音源","text":"从「役」省聲（營只切），借役之音記豛之讀。","cites":[]},
 {"key":"shengmu","label":"声母拟态","text":"y 零聲母，不系（照實）。","cites":[]}]}
json.dump(d,io.open(r"D:\系统汉字\web\public\cards\豛.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("部",num,name,"已按原文重写 豛")