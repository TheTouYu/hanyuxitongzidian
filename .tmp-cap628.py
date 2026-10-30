import sys,hashlib
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
doc=Document(r"D:\字谱智能体\卷三  矢.docx"); ps=doc.paragraphs; parts=doc.part.related_parts
tgt={hashlib.sha1(open(rf"D:\系统汉字\web\public\glyphs\智\{i:02d}.png","rb").read()).hexdigest():i for i in range(1,8)}
for k in range(103,113):
    t=ps[k].text.strip()
    hits=[]
    for el in ps[k]._p.iter():
        for a,v in el.attrib.items():
            if a.endswith("}embed") or a.endswith("}id"):
                try: b=parts[v].blob
                except KeyError: continue
                h=hashlib.sha1(b).hexdigest()
                if h in tgt: hits.append(tgt[h])
    print(k,(t[:26] or "-"),hits[:5],len(t))