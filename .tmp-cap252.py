import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
d=Document(r"D:\字谱智能体\卷二  㠯.docx"); ps=d.paragraphs; parts=d.part.related_parts
def imgs(el):
    o=[]
    for bl in el.iter():
        for a,v in bl.attrib.items():
            if a.endswith('}embed') or a.endswith('}id'):
                try:
                    q=parts[v]
                    if hasattr(q,'blob') and q.content_type.startswith('image'): o.append((v,len(q.blob)))
                except KeyError: pass
    return o
i=[k for k,p in enumerate(ps) if p.text.strip().startswith("11.帝部")][0]
print("部头段",i)
for k in range(i,i+14):
    t=ps[k].text.strip()
    print(k, (t[:40] or "-"), imgs(ps[k]._p)[:3])