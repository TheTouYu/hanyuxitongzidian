import docx
d=docx.Document(r"D:\字谱智能体\卷八十八  昜.docx")
P=[p.text.strip() for p in d.paragraphs]
for i,p in enumerate(P):
    if p.startswith("黨（") and len(p)>50:
        for q in P[i:i+6]:
            if q.startswith("本義") or q.startswith("轉義") or q.startswith("音源"): print(i,"|",q[:220])
        break
for t in "钂 儻 讜 攩 欓 爣 曭 灙 矘 掌 撐 幥 罉".split():
    for p in P[130:]:
        if p.startswith("・"+t) or p.startswith(t):
            print(t,"|",p[:170]); break