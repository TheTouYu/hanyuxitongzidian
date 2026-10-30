import sys,json,io
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
doc=Document(r"D:\字谱智能体\卷四  弋.docx"); ps=doc.paragraphs; parts=doc.part.related_parts
k0=[k for k,p in enumerate(ps) if p.text.strip().startswith("240.尗部")][0]
print("部头段",k0)
for k in range(k0,k0+40):
    imgs=[]
    for el in ps[k]._p.iter():
        for a,v in el.attrib.items():
            if a.endswith("}embed") or a.endswith("}id"):
                try: imgs.append((v,len(parts[v].blob)))
                except KeyError: pass
    if imgs: print(k,ps[k].text.strip()[:30],imgs[:3])