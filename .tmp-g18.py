import docx
d=docx.Document(r"D:\字谱智能体\卷八十八  昜.docx")
P=[p.text.strip() for p in d.paragraphs]
for t in "𣞙 鎟 𡠏 𩺞 𢧱 𣉕 縔 褬 𤸯 䮣 𨢆 𦟄".split():
    for p in P[378:440]:
        if p.startswith(t):
            print(t,"|",p[:150]); break