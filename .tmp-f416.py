import glob,os
from docx import Document
for path in sorted(glob.glob(r"D:\字谱智能体\*.docx")):
    try: d=Document(path)
    except Exception: continue
    ps=[(p.text or "").strip() for p in d.paragraphs]
    for i,t in enumerate(ps):
        if t.startswith("416.") :
            print("HIT",os.path.basename(path),"p",i,t[:50],"total",len(ps))
            for j in range(i+1,min(len(ps),i+22)):
                if ps[j]: print(" p%d %s"%(j,ps[j][:110]))
            raise SystemExit
print("none")