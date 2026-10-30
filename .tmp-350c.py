from docx import Document
d=Document(r"D:\字谱智能体\卷六十  𦟀.docx")
ps=[(p.text or "").strip() for p in d.paragraphs]
print("total",len(ps))
for j in range(352,len(ps)):
    t=ps[j]
    if len(t)>12 and (t.startswith(("後","退","各","路","咎","夅")) or "本義" in t[:6] or "轉義" in t[:6]):
        print(j, t[:110])