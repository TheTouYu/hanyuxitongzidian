import glob,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
for f in glob.glob(r"D:\字谱智能体\*.docx"):
    try: ps=[p.text for p in Document(f).paragraphs]
    except: continue
    for i,t in enumerate(ps):
        if "㿣" in t:
            print(f.split("\\")[-1],i,t[:120]); break