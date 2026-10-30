import sys,json,io
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷五  雁.docx").paragraphs]
out={k:ps[k] for k in range(228,244) if ps[k]}
io.open(r"D:\系统汉字\.tmp-changrows.json","w",encoding="utf-8").write(json.dumps(out,ensure_ascii=False))
print(len(out))