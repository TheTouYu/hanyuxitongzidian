import sys,json,io
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷四  弋.docx").paragraphs]
for k in range(190,205):
    if ps[k]: print(k,ps[k][:80])
C=r"D:\系统汉字\web\public\cards"
d=json.load(io.open(C+r"\夷.json",encoding="utf-8"))
print("photos",d.get("photos"),"caps",d.get("captions"))