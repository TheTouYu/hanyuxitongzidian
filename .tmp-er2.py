import sys,glob,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
for f in glob.glob(r"D:\字谱智能体\*.docx"):
    try: ps=[p.text.strip() for p in Document(f).paragraphs]
    except: continue
    for i,t in enumerate(ps):
        if re.match(r"^\d{1,3}[.．]\s*爾部$",t):
            print("HIT",f.split("\\")[-1],i)
            for k in range(i,i+14):
                if ps[k]: print(k,ps[k][:110])