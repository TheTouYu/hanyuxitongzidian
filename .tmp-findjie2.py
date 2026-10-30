import re,glob,os
from docx import Document
t=open(r"knowledge\hanzi-origin\mulu.md",encoding="utf-8").read()
for line in t.splitlines():
    if "介" in line: print("mulu:",line[:80])
for f in glob.glob(r"D:\字谱智能体\*.docx"):
    d=Document(f)
    for k,p in enumerate(d.paragraphs):
        s=p.text.strip()
        if re.match(r"^\d{3}[.．]",s) and ("介" in s): print(os.path.basename(f),k,s[:30])
        if "介（" in s and k<40: print("head?",os.path.basename(f),k,s[:40])