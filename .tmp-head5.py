import sys,re,glob
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
for f in glob.glob(r"D:\字谱智能体\卷*.docx"):
    try: ps=[p.text.strip() for p in Document(f).paragraphs]
    except: continue
    for i,t in enumerate(ps[:80]):
        m=re.match(r"^(\d{1,2})[.．]\s*(\S{1,2})部?$",t)
        if m and int(m.group(1))<=7: print(f.split("\\")[-1],i,t[:40])