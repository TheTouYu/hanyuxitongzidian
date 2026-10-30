import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷二  㠯.docx").paragraphs]
for k in range(660,740):
    if "伎（𢺵）" in ps[k]: print(k, ps[k].count("伎（𢺵）"), ps[k][:60],"…",ps[k][-60:])