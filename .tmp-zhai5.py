# -*- coding: utf-8 -*-
import json,io,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷七  斤.docx").paragraphs]
targets="㢉咤詫姹挓侘烢𪀥䤩䯔𧧉侂秺垞𨴥䖳𨀟𣳥㤞𤵾𥭌𨀸"
txt={}
for k in range(296,374):
    t=ps[k]
    if not t: continue
    c=t[0]
    if c in targets and c not in txt: txt[c]=t
missing=[c for c in targets if c not in txt]
print("got",len(txt),"missing",missing)
p=r"D:\系统汉字\web\public\cards\宅.json"
d=json.load(io.open(p,encoding="utf-8"))
for g in d["sections"][4]["groups"]:
    for r in g["rows"]:
        head=r[0][0]
        if head in txt: r[3]=txt[head]
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("ok")