import glob,os
from docx import Document
for path in sorted(glob.glob(r"D:\字谱智能体\卷七十*")):
    d=Document(path); ps=[(p.text or "").strip() for p in d.paragraphs]
    for i,t in enumerate(ps):
        if t.startswith("425."):
            print("HIT",os.path.basename(path),i,t[:36],"total",len(ps))
            for j in range(i+1,i+16):
                if ps[j] and len(ps[j])>6: print(j, ps[j][:70])
            raise SystemExit
print("none in 卷七十*")