# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷七  斤.docx").paragraphs]
targets="㢉咤詫姹挓侘烢𪀥䤩䯔𧧉侂秺垞𨴥䖳𨀟𣳥㤞𤵾𥭌𨀸"
txt={}
for k in range(290,374):
    t=ps[k]
    if t and t[0] in targets and t[0] not in txt: txt[t[0]]=t
p=r"D:\系统汉字\web\public\cards\宅.json"
d=json.load(io.open(p,encoding="utf-8"))
sec=next(s for s in d["sections"] if s.get("key")=="zizu")
n=0
for g in sec["groups"]:
    for r in g["rows"]:
        h=r[0][0]
        if h in txt: r[3]=txt[h]; n+=1
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("filled",n)