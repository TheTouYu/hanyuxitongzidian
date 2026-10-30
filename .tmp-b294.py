from docx import Document
P=Document(r"D:\字谱智能体\卷七十四  雈.docx").paragraphs
start=None
for i,q in enumerate(P):
    if q.text.strip().startswith("443.卝"): start=i; break
n=0
for r in P[start:start+95]:
    s=r.text.strip()
    if not s: continue
    print(s[:190]); n+=1
    if n>=80: break