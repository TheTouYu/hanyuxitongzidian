import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
d=Document(r"D:\字谱智能体\卷一  雞.docx"); parts=d.part.related_parts
def imgs(el):
    out=[]
    for bl in el.iter():
        for a,v in bl.attrib.items():
            if a.endswith('}embed') or a.endswith('}id'):
                try:
                    p=parts[v]
                    if hasattr(p,'blob') and p.content_type.startswith('image'): out.append((v,len(p.blob)))
                except KeyError: pass
    return out
ps=d.paragraphs
for i in range(115,142):
    t=ps[i].text.strip()
    ii=imgs(ps[i]._p)
    if ii or t.startswith("本義") or t.startswith("3."): print(i, (t[:34] or "-"), ii[:3])