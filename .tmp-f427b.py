import glob,os
from docx import Document
for path in sorted(glob.glob(r"D:\字谱智能体\卷七十*.docx")):
    d=Document(path); ps=[(p.text or "").strip() for p in d.paragraphs]
    for i,t in enumerate(ps):
        if t.startswith("427."):
            print("HIT",os.path.basename(path),i,t[:36],"total",len(ps))
            for j in range(i+1,i+22):
                if ps[j] and len(ps[j])>6: print(j, ps[j][:95])
            raise SystemExit
print("not in 卷七十*")