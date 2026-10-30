import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
doc=Document(r"D:\字谱智能体\卷四  弋.docx"); ps=doc.paragraphs; parts=doc.part.related_parts
for k in range(96,126):
    imgs=[]
    for el in ps[k]._p.iter():
        for a,v in el.attrib.items():
            if a.endswith("}embed") or a.endswith("}id"):
                try: imgs.append(len(parts[v].blob))
                except KeyError: pass
    if imgs: print(k,len(imgs),imgs[:20])