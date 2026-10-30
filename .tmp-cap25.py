import sys,glob
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
for f in glob.glob(r"D:\字谱智能体\*.docx"):
    try: ps=[p.text.strip() for p in Document(f).paragraphs]
    except: continue
    for k,t in enumerate(ps):
        if t.startswith("巵") and ("《" in t or "本義" in t or "說文" in t or "zhī" in t):
            print(f.split("\\")[-1],k,t[:200])