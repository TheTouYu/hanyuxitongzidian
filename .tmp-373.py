import glob,os
from docx import Document
for path in glob.glob(r"D:\字谱智能体\卷六十三*.docx"):
    d=Document(path); ps=[(p.text or "").strip() for p in d.paragraphs]
    for i,t in enumerate(ps):
        if t.startswith("373."):
            print("FILE",os.path.basename(path),"p",i,t)
            for j in range(i+1,i+16):
                if ps[j]: print(" p%d %s"%(j,ps[j][:110]))
            raise SystemExit
print("not found")