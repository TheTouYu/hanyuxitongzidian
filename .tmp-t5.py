from docx import Document
import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
d=Document(r"D:\字谱智能体\卷二  㠯.docx")
ps=[p.text.strip() for p in d.paragraphs]
for k in range(120,245):
    t=ps[k]
    if not t: continue
    if t.startswith("字族衍義") or t[:1] in "①②③④⑤" or t.startswith("（") and "：" in t[:6]:
        print(k,t[:60])
    elif len(t)>2 and t[1] in "（(" or (len(t)>3 and t[2] in "（("):
        print(k,t[:64])