import glob,os
from docx import Document
for path in sorted(glob.glob(r"D:\字谱智能体\*.docx")):
    try: d=Document(path)
    except Exception: continue
    ps=[(p.text or "").strip() for p in d.paragraphs]
    for i,t in enumerate(ps):
        if t.startswith("407."):
            print("HIT",os.path.basename(path),"p",i,"total",len(ps))
            for j in range(i,min(len(ps),i+40)):
                if ps[j]: print(j,ps[j][:110])
            raise SystemExit
print("not found")