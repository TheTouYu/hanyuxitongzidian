from docx import Document
d=Document(r"D:\字谱智能体\卷六十三  索.docx"); ps=[(p.text or "").strip() for p in d.paragraphs]
want=["䄼","䇧","𦭮","𠈇","恬","宿","縮","摍","蹜","樎"]
for ch in want:
    for i in range(150,230):
        t=ps[i] if i<len(ps) else ""
        if t.startswith(ch) and len(t)>25:
            print("==",ch,"p",i); print(t[:130]); break
    else: print("==",ch,"none")