import glob,os
from docx import Document
for path in sorted(glob.glob(r"D:\字谱智能体\卷六十三*.docx")):
    d=Document(path); ps=[(p.text or "").strip() for p in d.paragraphs]
    print("FILE",os.path.basename(path),len(ps))
    for i,t in enumerate(ps):
        if t.startswith("371."):
            for j in range(i,min(len(ps),i+26)):
                if ps[j]: print(" p%d %s"%(j,ps[j][:100]))
            break