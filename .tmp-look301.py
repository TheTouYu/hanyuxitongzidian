import sys,re,glob
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
for f in glob.glob(r"D:\字谱智能体\*.docx"):
    ps=[p.text.strip() for p in Document(f).paragraphs]
    for k,t in enumerate(ps):
        if re.match(r"^2[6-7][.．]\s*\S+部$",t):
            print(f.split("\\")[-1],k,t)