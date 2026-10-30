import glob,os,re
from docx import Document
for path in sorted(glob.glob(r"D:\字谱智能体\卷六十*.docx"))+sorted(glob.glob(r"D:\字谱智能体\卷七十*.docx")):
    try: d=Document(path)
    except Exception: continue
    ps=[(p.text or "").strip() for p in d.paragraphs]
    for i,t in enumerate(ps):
        if re.match(r"^366[.．、]",t):
            print("HIT",os.path.basename(path),"p",i,t[:26])
            for j in range(i+1,min(len(ps),i+12)):
                if ps[j]: print(" p%d %s"%(j,ps[j][:96]))
            raise SystemExit
print("not found in 60s/70s")