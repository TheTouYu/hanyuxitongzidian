import glob,os
from docx import Document
for path in sorted(glob.glob(r"D:\字谱智能体\卷六十三*.docx"))+sorted(glob.glob(r"D:\字谱智能体\卷六十四*.docx")):
    d=Document(path); ps=[(p.text or "").strip() for p in d.paragraphs]
    for i,t in enumerate(ps):
        if t.startswith("364."):
            print("HIT",os.path.basename(path),"p",i,t[:30])
            for j in range(i+1,min(len(ps),i+30)):
                if ps[j]: print(" p%d %s"%(j,ps[j][:100]))
            raise SystemExit
print("not in 63/64")