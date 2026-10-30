import glob,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
for f in glob.glob(r"D:\字谱智能体\卷一*.docx"):
    print("FILE",f)
    for p in Document(f).paragraphs[:400]:
        t=p.text.strip()
        m=re.match(r"^([1-9]\d?)[.．]\s*(\S{1,3})部$",t)
        if m: print(" ",m.group(1),m.group(2))