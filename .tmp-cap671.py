import sys,glob
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
for f in glob.glob(r"D:\字谱智能体\*.docx"):
    for k,p in enumerate(Document(f).paragraphs):
        t=p.text.strip()
        if t.startswith("芪"):
            print(f.split("\\")[-1],k,t[:120]); break