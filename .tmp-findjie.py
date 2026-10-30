import re,glob,json,os
t=open(r"knowledge\hanzi-origin\mulu.md",encoding="utf-8").read()
for m in re.finditer(r"(第?\d{1,3})[部\.].{0,6}介",t):
    print("mulu:",m.group(0)[:40])
from docx import Document
for f in glob.glob(r"D:\字谱智能体\*.docx"):
    d=Document(f)
    for k,p in enumerate(d.paragraphs):
        s=p.text.strip()
        if re.match(r"^\d{3}[.．]\s*介部",s):
            print(os.path.basename(f),k,s[:40])