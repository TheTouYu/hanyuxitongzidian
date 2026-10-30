import sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷四  弋.docx").paragraphs]
i=[k for k,t in enumerate(ps) if re.match(r"^27[.．]\s*夷部",t)]
print("idx",i)
k=i[0] if i else 0
c=0
for j in range(k,min(k+80,len(ps))):
    if ps[j]:
        print(j,ps[j][:60]); c+=1
        if c>=8: break