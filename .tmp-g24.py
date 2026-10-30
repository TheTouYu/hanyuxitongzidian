import docx
d=docx.Document(r"D:\字谱智能体\卷八十九  象.docx")
P=[p.text.strip() for p in d.paragraphs]
for t in "壯 莊 奘 裝 匨 銺 焋 梉 糚 㮜 狀 妝".split():
    for p in P[59:217]:
        if p.startswith(t+"（") or p.startswith(t):
            if "《" in p: print(t,"|",p[:150]); break