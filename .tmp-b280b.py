from docx import Document
import re
d=Document(r"D:\字谱智能体\卷七十三  釆.docx")
for q in d.paragraphs:
    t=q.text.strip()
    if re.match(r"\d{3}\.\S",t) and len(t)<40 and "部" in t:
        print(t[:40])