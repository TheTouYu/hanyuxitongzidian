import sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷一  雞.docx").paragraphs]
fams={"㤅":"僾瞹皧薆噯曖嬡璦燰鱫䁆鑀靉","疑":"㘈嶷癡懝譺擬儗礙薿凝㽈𥣖䰯𦡸","贛":"𧗜𧆐䤗䀍𥸡㔶𠏤戇竷"}
for k in range(330,500):
    t=ps[k]
    if not t: continue
    c=t[0]
    for r,chars in fams.items():
        if c in chars: print(k,t[:120])