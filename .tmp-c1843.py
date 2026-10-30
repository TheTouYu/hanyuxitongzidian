import sys,glob,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
for f in glob.glob(r"D:\字谱智能体\*.docx"):
    try: ps=[p.text.strip() for p in Document(f).paragraphs]
    except Exception: continue
    for k,t in enumerate(ps):
        m=re.match(r"^389[.．]\s*(\S{1,2})部",t)
        if m: print(f.split("\\")[-1],k,t[:20]); break