import glob,os
from docx import Document
for path in sorted(glob.glob(r"D:\字谱智能体\*.docx")):
    if "犀" not in path: continue
    d=Document(path); ps=[(p.text or "").strip() for p in d.paragraphs]
    for i,t in enumerate(ps):
        if t.startswith("359.") or t.startswith("360."):
            print("HIT",t,"p",i,"total",len(ps))
            for j in range(i+1,min(len(ps),i+22)):
                s=ps[j]
                if s: print(" p%d %s"%(j,s[:110]))
            print("---")