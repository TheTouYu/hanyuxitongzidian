import glob,os
from docx import Document
for path in sorted(glob.glob(r"D:\字谱智能体\*.docx")):
    try: d=Document(path)
    except Exception: continue
    ps=[(p.text or "").strip() for p in d.paragraphs]
    for i,t in enumerate(ps):
        if t.startswith("351.") or t.startswith("351．"):
            print("HIT",os.path.basename(path),"p",i,t[:40],"total",len(ps))
            for j in range(i+1,min(len(ps),i+26)):
                s=ps[j]
                if s: print(" p%d %s"%(j,s[:120]))
            raise SystemExit
print("not found")