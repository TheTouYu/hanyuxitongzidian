from docx import Document
d=Document(r"D:\字谱智能体\卷六十三  索.docx"); ps=[(p.text or "").strip() for p in d.paragraphs]
want=["鏥","㴼","䈹","䑿","𤛝","𥀝","𨣡","𩘰","宿"]
for ch in want:
    for i in range(150,215):
        t=ps[i] if i<len(ps) else ""
        if t.startswith(ch) and len(t)>25:
            print("==",ch,"p",i); print(t[:120]); break
    else: print("==",ch,"none")