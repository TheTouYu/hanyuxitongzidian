import sys,os,json,io
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
P=r"D:\系统汉字\web\public\glyphs\photos"
print("dir:",os.listdir(os.path.join(P,"丂")) if os.path.isdir(os.path.join(P,"丂")) else "none")
ph=json.load(io.open(os.path.join(P,"index.json"),encoding="utf-8")); d=ph.get("photos") or ph
print("index:",d.get("丂"))
cp=json.load(io.open(os.path.join(P,"captions.json"),encoding="utf-8")); c=cp.get("captions") or cp
print("cap:",c.get("丂"))
from docx import Document
doc=Document(r"D:\字谱智能体\卷五  雁.docx")
for idx in (35,134):
    out=[]
    for el in doc.paragraphs[idx]._p.iter():
        if el.tag.split("}")[-1]=="blip":
            rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
            if rid:
                b=doc.part.related_parts[rid[0]].blob; out.append((len(b),b[:4]))
    print(idx,out)