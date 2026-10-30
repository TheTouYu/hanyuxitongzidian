import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
d=Document(r"D:\字谱智能体\卷四  弋.docx"); ps=d.paragraphs; parts=d.part.related_parts
for k in range(70,105):
    for el in ps[k]._p.iter():
        for a,v in el.attrib.items():
            if a.endswith("}embed") or a.endswith("}id"):
                try: b=parts[v].blob
                except KeyError: continue
                if len(b)>8000: print(k,v,len(b),ps[k].text.strip()[:12])