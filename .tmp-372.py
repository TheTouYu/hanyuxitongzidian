import glob,os
from docx import Document
n=len(glob.glob(r"web\public\cards\*.json"))
print("cards:",n)
for path in glob.glob(r"D:\字谱智能体\卷六十三*.docx"):
    d=Document(path); ps=[(p.text or "").strip() for p in d.paragraphs]
    for i,t in enumerate(ps):
        if t.startswith("372."):
            print("HIT p",i,t[:30])
            for j in range(i+1,i+22):
                if ps[j]: print(" p%d %s"%(j,ps[j][:90]))
            raise SystemExit