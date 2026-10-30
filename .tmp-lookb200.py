import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
doc=Document(r"D:\字谱智能体\卷四  弋.docx"); parts=doc.part.related_parts
seq=[]
for el in doc.paragraphs[347]._p.iter():
    tag=el.tag.split("}")[-1]
    if tag=="t": seq.append(el.text or "")
    elif tag=="blip":
        rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
        if rid:
            try: seq.append("[%d]"%len(parts[rid[0]].blob))
            except KeyError: seq.append("[?]")
print("".join(seq))