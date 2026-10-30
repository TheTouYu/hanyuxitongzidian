import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
import glob
for f in glob.glob(r"D:\字谱智能体\卷三*.docx"):
    ps=Document(f).paragraphs
    for k,p in enumerate(ps):
        t=p.text
        if "伯任" in t or "陳羌鐘" in t:
            print(f.split("\\")[-1],k,t[:50])