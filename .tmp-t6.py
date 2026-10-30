from docx import Document
import sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
d=Document(r"D:\字谱智能体\卷二  㠯.docx")
ps=[p.text.strip() for p in d.paragraphs]
for k,t in enumerate(ps):
    if re.match(r"^（.*）：",t):
        nxt=next((ps[j] for j in range(k+1,min(k+4,len(ps))) if ps[j]),"")
        print(k,t[:28],"|",nxt[:34])