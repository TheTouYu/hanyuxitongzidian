import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
doc=Document(r"D:\字谱智能体\卷四  弋.docx"); ps=doc.paragraphs; parts=doc.part.related_parts
idx=[(k,p.text.strip()) for k,p in enumerate(ps) if "尗" in p.text and "部" in p.text]
print(idx[:5])
k0=idx[0][0] if idx else None
if k0:
    for k in range(k0,k0+45):
        imgs=[]
        for el in ps[k]._p.iter():
            for a,v in el.attrib.items():
                if a.endswith("}embed") or a.endswith("}id"):
                    try: imgs.append((v,len(parts[v].blob)))
                    except KeyError: pass
        if imgs: print(k,ps[k].text.strip()[:26],imgs[:3])