import docx,glob,os
d=docx.Document(r"D:\字谱智能体\卷八十八  昜.docx")
P=[p.text.strip() for p in d.paragraphs]
for t in "𥤗 𥸈 𩽳 𪇁 㿩 𣎲 𥳶 𩞦 𢿦 礃 𣾦 𦺡".split():
    for p in P[130:]:
        if p.startswith("・"+t) or p.startswith(t):
            print(t,"|",p[:150]); break
print("---files---")
for f in sorted(glob.glob(r"D:\字谱智能体\卷八十*.docx"))[-4:]: print(os.path.basename(f))