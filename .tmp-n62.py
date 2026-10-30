import glob
from docx import Document
for p in glob.glob(r"D:\字谱智能体\卷六十二*.docx")+glob.glob(r"D:\字谱智能体\卷六十三*.docx"):
    d=Document(p); ps=[(x.text or "").strip() for x in d.paragraphs]
    print(p.split("\\")[-1], len(ps), "first:", ps[0][:60] if ps else "")
    for i,t in enumerate(ps[:12]):
        if t: print("  p%d %s"%(i,t[:100]))