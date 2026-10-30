import sys,glob,os
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
pat=("或囗","或口","一或")
for f in glob.glob(r"D:\字谱智能体\*.docx"):
    try: d=Document(f)
    except: continue
    for i,p in enumerate(d.paragraphs):
        t=p.text.strip()
        if any(k in t for k in pat) and len(t)<200:
            print(os.path.basename(f),i,t[:100])