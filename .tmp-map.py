from docx import Document
import re,glob
want=set("犮戾翊肆必半皆癶")
for p in glob.glob(r"D:\字谱智能体\*.docx"):
    try: d=Document(p)
    except Exception: continue
    for q in d.paragraphs:
        t=q.text.strip()
        m=re.match(r"(\d{3})\.(\S+?)部$",t)
        if m and m.group(2) in want:
            print(p.split("\\")[-1],"|",t)