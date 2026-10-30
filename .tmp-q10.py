import sys,glob,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
for f in glob.glob(r"D:\字谱智能体\卷二*.docx")+glob.glob(r"D:\字谱智能体\卷三*.docx"):
    try: ps=[p.text.strip() for p in Document(f).paragraphs]
    except Exception as e: print(f,"ERR",e); continue
    heads=[(i,t) for i,t in enumerate(ps) if re.match(r"^\d{1,3}[.．]\s*\S{1,2}部$",t)]
    print(f.split("\\")[-1], len(ps), heads[:12])