import glob,os
from docx import Document
for path in sorted(glob.glob(r"D:\字谱智能体\卷六十一*.docx"))+sorted(glob.glob(r"D:\字谱智能体\卷六十二*.docx")):
    d=Document(path); ps=[(p.text or "").strip() for p in d.paragraphs]
    for i,t in enumerate(ps):
        if t.startswith("355."):
            print("HIT",os.path.basename(path),"p",i,t[:40])
            for j in range(i+1,min(len(ps),i+14)):
                if ps[j]: print(" p%d %s"%(j,ps[j][:110]))
            raise SystemExit
print("not found")