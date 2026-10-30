import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
doc=Document(r"D:\字谱智能体\卷三  矢.docx"); ps=doc.paragraphs; parts=doc.part.related_parts
for k in list(range(104,112))+[226,227,228]:
    imgs=[]
    for el in ps[k]._p.iter():
        for a,v in el.attrib.items():
            if a.endswith("}embed") or a.endswith("}id"):
                try: imgs.append(len(parts[v].blob))
                except KeyError: pass
    print(k, ps[k].text.strip()[:24] or "-", imgs[:10])