import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
doc=Document(r"D:\字谱智能体\卷五  雁.docx"); parts=doc.part.related_parts
for k in (249,250,251,252,253,254,255,256,257,258):
    ids=[]
    for el in doc.paragraphs[k]._p.iter():
        if el.tag.split("}")[-1]=="blip":
            rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
            if rid: ids.append((rid[0],len(parts[rid[0]].blob)))
    if ids: print(k,len(ids),ids[:30])