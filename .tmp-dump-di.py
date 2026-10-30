import sys,glob,os
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
for f in glob.glob(r"D:\字谱智能体\*.docx"):
    try: ps=[p.text.strip() for p in Document(f).paragraphs]
    except: continue
    for i,t in enumerate(ps):
        if t=="11.帝部" or t.startswith("11.帝部") or t=="11.帝":
            print("FILE",os.path.basename(f),"at",i)
            for k in range(i,i+26):
                if ps[k]: print(k,ps[k][:120])
            raise SystemExit