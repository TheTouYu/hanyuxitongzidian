import sys,glob,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
d=Document(r"D:\字谱智能体\卷五十八  兒.docx"); ps=[p.text.strip() for p in d.paragraphs]
for k in range(108,158):
    t=ps[k]
    if t and (re.match(r"^[①②③④⑤⑥]",t) or "《" in t): print(k,t[:78])