import sys,json
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷五  雁.docx").paragraphs]
out={k:ps[k] for k in (423,426,427,445,447,448,449)}
json.dump(out,open(r"D:\系统汉字\.tmp-yixi.json","w",encoding="utf-8"),ensure_ascii=False)
print(sum(len(v) for v in out.values()))