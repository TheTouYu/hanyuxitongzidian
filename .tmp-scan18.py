# -*- coding: utf-8 -*-
import sys,glob,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
for f in glob.glob(r"D:\字谱智能体\卷二*.docx"):
    ps=[p.text.strip() for p in Document(f).paragraphs]
    for i in range(330,346):
        s=ps[i]
        if s and re.search(r"(lí|mái|mò|yù|貍|狸)", s): print(i, s[:200])