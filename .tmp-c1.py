from docx import Document
import glob,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for f in sorted(glob.glob(r"D:\字谱智能体\*.docx")):
    try: ps=[p.text.strip() for p in Document(f).paragraphs]
    except: continue
    for k,t in enumerate(ps[:40]):
        if re.match(r"^第[一二三四五六七八九十]+章",t):
            print(f.split("\\")[-1],k,t[:40],"|",(ps[k+1][:50] if k+1<len(ps) else ""))