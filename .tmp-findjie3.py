import re,glob,os
from docx import Document
t=open(r"knowledge\hanzi-origin\mulu.md",encoding="utf-8").read()
for line in t.splitlines():
    if "介" in line: print("MULU:",line)
for f in glob.glob(r"D:\字谱智能体\*.docx"):
    d=Document(f)
    ps=[p.text.strip() for p in d.paragraphs]
    for k,s in enumerate(ps):
        if s.startswith("介") and len(s)<60: print("P:",os.path.basename(f),k,s[:60])