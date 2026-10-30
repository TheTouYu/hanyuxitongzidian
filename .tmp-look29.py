import sys,glob
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
for pat in ["卷五*","卷六*"]:
    for f in glob.glob(r"D:\字谱智能体\\"+pat):
        d=Document(f); ps=[p.text.strip() for p in d.paragraphs if p.text.strip()]
        print("FILE",f.split("\\")[-1],len(ps))
        for t in ps[:14]: print("  ",t[:90])