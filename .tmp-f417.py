import glob,os
from docx import Document
for path in sorted(glob.glob(r"D:\字谱智能体\*.docx")):
    try: d=Document(path)
    except Exception: continue
    ps=[(p.text or "").strip() for p in d.paragraphs]
    for j,t in enumerate(ps):
        if t.startswith("399."):
            print("HIT",os.path.basename(path),j,t[:40],"total",len(ps))
            for k in range(j,min(len(ps),j+30)):
                if ps[k]: print(" ",k,ps[k][:120])
            raise SystemExit
print("none")