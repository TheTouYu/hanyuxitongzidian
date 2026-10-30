# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
doc=Document(r"D:\字谱智能体\卷四  弋.docx"); parts=doc.part.related_parts
seq=[]
for el in doc.paragraphs[264]._p.iter():
    tag=el.tag.split("}")[-1]
    if tag=="t": seq.append(el.text or "")
    elif tag=="blip":
        rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
        if rid:
            try: b=parts[rid[0]].blob; seq.append("[IMG %d]"%len(b))
            except KeyError: seq.append("[?]")
print("".join(seq)[:1200])
print("----")
for k in (262,263,265,266,267,277,278):
    ps=doc.paragraphs[k].text.strip()
    n=sum(1 for el in doc.paragraphs[k]._p.iter() if el.tag.endswith('}blip'))
    print(k,n,ps[:60])