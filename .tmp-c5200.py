# -*- coding: utf-8 -*-
import json,io,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷四  弋.docx").paragraphs]
C=r"D:\系统汉字\web\public\cards"
p=C+r"\夷.json"; d=json.load(io.open(p,encoding="utf-8"))
fix={"蛦":"虫","鮧":"魚","恞":"心","䧅":"阜","侇":"人","銕":"金"}
for s in d["sections"]:
    if s["key"]!="zizu": continue
    for g in s["groups"]:
        for r in g["rows"]:
            base=re.sub(r"（.*?）","",r[0])
            if base=="眱": r[2]="目"
            if base in fix and not r[2]: r[2]=fix[base]
            # 落点：取原稿该字正条整段
            t=""
            for k in range(203,262):
                if ps[k].startswith(base): t=ps[k]; break
            if t: r[3]=t
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("类属补",fix,"眱→目")