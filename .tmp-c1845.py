import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
doc=Document(r"D:\字谱智能体\第八章  子.docx"); parts=doc.part.related_parts; ps=doc.paragraphs
n=0
for el in ps[315]._p.iter():
    for a,v in el.attrib.items():
        if a.endswith("}embed") or a.endswith("}id"):
            try: b=parts[v].blob
            except KeyError: continue
            if len(b)>30000:
                ext=".png" if b[:4]==b"\x89PNG" else ".jpg"
                open(rf"D:\系统汉字\.tmp-img{n}{ext}","wb").write(b); print(n,ext,len(b)); n+=1