import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
doc=Document(r"D:\字谱智能体\卷三  矢.docx"); parts=doc.part.related_parts
for k in range(536,548):
    p=doc.paragraphs[k]; rids=[]
    for el in p._p.iter():
        for a,v in el.attrib.items():
            if a.endswith("}embed") or a.endswith("}id"):
                try: rids.append((v,len(parts[v].blob)))
                except KeyError: pass
    print(k,p.text.strip()[:30],rids[:8])