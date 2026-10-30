import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
doc=Document(r"D:\字谱智能体\卷五  雁.docx"); parts=doc.part.related_parts
for idx in (28,53,73,102):
    seq=[]
    for el in doc.paragraphs[idx]._p.iter():
        tag=el.tag.split("}")[-1]
        if tag=="t": seq.append(el.text or "")
        elif tag=="blip":
            rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
            if rid:
                try: seq.append("[%d]"%len(parts[rid[0]].blob))
                except KeyError: pass
    print(idx,"".join(seq)[:400]); print("---")