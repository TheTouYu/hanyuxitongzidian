import docx
d=docx.Document(r"D:\字谱智能体\卷八十八  昜.docx")
P=[p.text.strip() for p in d.paragraphs]
for t in "壋 螳 儅 簹 澢 艡 礑 闣 㼕 劏 㽆 嵣".split():
    for p in P[130:]:
        if p.startswith("・"+t) or p.startswith(t):
            print(t,"|",p[:190]); break