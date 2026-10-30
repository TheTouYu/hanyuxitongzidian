import sys,glob
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
hits=0
for f in glob.glob(r"D:\字谱智能体\*.docx"):
    try: ps=[p.text.strip() for p in Document(f).paragraphs]
    except: continue
    for k,t in enumerate(ps):
        if ("巵" in t or "卮" in t) and len(t)<120:
            print(f.split("\\")[-1],k,t[:150]); hits+=1
            if hits>6: sys.exit()