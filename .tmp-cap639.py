import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
doc=Document(r"D:\字谱智能体\卷三  矢.docx"); ps=doc.paragraphs; parts=doc.part.related_parts
for k in range(150,170):
    imgs=[]
    for el in ps[k]._p.iter():
        for a,v in el.attrib.items():
            if a.endswith("}embed") or a.endswith("}id"):
                try: imgs.append(len(parts[v].blob))
                except KeyError: pass
    if imgs or ps[k].text.strip(): print(k,ps[k].text.strip()[:26] or "-",imgs[:6])