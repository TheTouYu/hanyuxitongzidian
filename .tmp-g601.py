import sys,glob,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
for f in glob.glob(r"D:\字谱智能体\*.docx"):
    try: d=Document(f)
    except: continue
    ps=[p.text.strip() for p in d.paragraphs]
    hit=[(i,t) for i,t in enumerate(ps) if re.match(r"^60[01]\s*[.．]",t)]
    if hit:
        print("FILE",f)
        for i,t in hit[:3]: print(" ",i,t[:60])