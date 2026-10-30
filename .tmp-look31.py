import sys,os,re; sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
base=r"D:\字谱智能体"
for f in sorted(os.listdir(base)):
    if not f.endswith(".docx"): continue
    if not re.match(r"卷九[八九十]",f): continue
    try: d=Document(os.path.join(base,f))
    except Exception as e: print(f,"ERR"); continue
    ps=[p.text.strip() for p in d.paragraphs]
    heads=[t for t in ps if re.match(r"^\d{3}[.．]",t)][:6]
    print(f,"|",heads)