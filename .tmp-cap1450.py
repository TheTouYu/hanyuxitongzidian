import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
doc=Document(r"D:\字谱智能体\卷三  矢.docx"); ps=doc.paragraphs; parts=doc.part.related_parts
for k in range(355,405):
    t=ps[k].text.strip(); imgs=[]
    for el in ps[k]._p.iter():
        for a,v in el.attrib.items():
            if a.endswith("}embed") or a.endswith("}id"):
                try: imgs.append((v,len(parts[v].blob)))
                except KeyError: pass
    if imgs: print(k,t[:26],imgs)