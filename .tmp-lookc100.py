import sys,re,glob
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
for f in glob.glob(r"D:\字谱智能体\卷五*.docx"):
    doc=Document(f); ps=[p.text.strip() for p in doc.paragraphs]
    print(f, len(ps))
    for k,t in enumerate(ps):
        m=re.match(r"^(\d{1,3})[.．]\s*(\S{1,3})部$",t)
        if m: print("  ",k,t)