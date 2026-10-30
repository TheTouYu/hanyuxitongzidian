from docx import Document
d=Document(r"D:\字谱智能体\卷六十三  索.docx"); ps=[(p.text or "").strip() for p in d.paragraphs]
want=["遫","駷","竦","悚","疏","踈","梀","敕","搠","藗"]
for ch in want:
    for i in range(60,160):
        t=ps[i] if i<len(ps) else ""
        if t.startswith(ch) and len(t)>28:
            print("==",ch,"p",i); print(t[:150]); break
    else:
        print("==",ch,"no entry")