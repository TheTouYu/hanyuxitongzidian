from docx import Document
import re
d=Document(r"D:\字谱智能体\卷七十三  釆.docx"); P=d.paragraphs
for i,q in enumerate(P):
    if q.text.strip().startswith("439.扁"):
        n=0
        for r in P[i:i+45]:
            s=r.text.strip()
            if not s: continue
            print(s[:170]); n+=1
            if n>=38: break
        break