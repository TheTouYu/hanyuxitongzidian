import sys,re,glob
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
t=open(r"D:\系统汉字\knowledge\hanzi-yinyuan\22b-lei.md",encoding="utf-8").read()
i=t.find("申字族三")
print(t[max(0,i-2600):i+900].replace("\n\n","\n")[:3200])
for f in glob.glob(r"D:\字谱智能体\卷二十二*.docx"):
    ps=[p.text.strip() for p in Document(f).paragraphs]
    for k,x in enumerate(ps):
        if x.startswith("114.申部"):
            print("=== docx",k)
            for y in ps[k:k+8]:
                if y: print(y[:200])