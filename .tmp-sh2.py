import sys,re,glob
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
for f in glob.glob(r"D:\系统汉字\knowledge\hanzi-yinyuan\*.md"):
    t=open(f,encoding="utf-8").read()
    if "申字族三" in t:
        i=t.find("申字族三"); print(f)
        seg=t[max(0,i-3000):i+1200]
        print(seg[:3300])
        break
for f in glob.glob(r"D:\字谱智能体\卷二十二*.docx"):
    ps=[p.text.strip() for p in Document(f).paragraphs]
    for k,x in enumerate(ps):
        if x.startswith("114.申部"):
            print("=== docx",f.split("\\")[-1],k)
            for y in ps[k:k+9]:
                if y: print(y[:220])