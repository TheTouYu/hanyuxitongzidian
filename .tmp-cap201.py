import re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
def head(f,idx):
    ps=[p.text.strip() for p in Document(f).paragraphs]
    for i in range(idx,-1,-1):
        m=re.match(r"^(\d{1,3})[.．]\s*(\S{1,2})部$",ps[i])
        if m: return m.group(1),m.group(2)
    return None
print("㞷",head(r"D:\字谱智能体\卷八十五  匚.docx",273))
print("㠱",head(r"D:\字谱智能体\第八章  子.docx",468))