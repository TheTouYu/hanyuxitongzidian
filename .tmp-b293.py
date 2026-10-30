from docx import Document
P=Document(r"D:\字谱智能体\卷七十三  釆.docx").paragraphs
start=None
for i,q in enumerate(P):
    if q.text.strip().startswith("441.豩"): start=i; break
n=0
for r in P[start:start+70]:
    s=r.text.strip()
    if not s: continue
    print(s[:200]); n+=1
    if n>=58: break