import glob,os
from docx import Document
for path in sorted(glob.glob(r"D:\字谱智能体\*.docx")):
    try: d=Document(path)
    except Exception: continue
    ps=[(p.text or "").strip() for p in d.paragraphs]
    for i,t in enumerate(ps):
        if t.startswith("418."):
            print("HIT",os.path.basename(path),i,t[:40],"total",len(ps))
            for j in range(i+1,min(len(ps),i+30)):
                if ps[j] and len(ps[j])>6: print(j, ps[j][:100])
            raise SystemExit
print("not found")