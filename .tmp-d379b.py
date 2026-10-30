import glob,os
from docx import Document
for path in sorted(glob.glob(r"D:\字谱智能体\*.docx")):
    try: d=Document(path)
    except Exception: continue
    ps=[(p.text or "").strip() for p in d.paragraphs]
    for i,t in enumerate(ps):
        if t.startswith("379."):
            print("FILE",os.path.basename(path),"para",i,t[:40])
            n=0
            for j in range(i+1,len(ps)):
                if ps[j]:
                    print(j,ps[j][:120]); n+=1
                    if n>=20: break
            raise SystemExit
print("none")