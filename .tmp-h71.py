from docx import Document
import re,glob
for p in glob.glob(r"D:\字谱智能体\卷七十*.docx")+glob.glob(r"D:\字谱智能体\卷七十一*.docx"):
    try: d=Document(p)
    except Exception: continue
    print("=====",p.split("\\")[-1])
    for q in d.paragraphs:
        t=q.text.strip()
        if re.match(r"\d{3}\.\S",t) and len(t)<40 and "部" in t:
            print(t[:40])