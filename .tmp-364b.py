import glob,os,re
from docx import Document
for path in sorted(glob.glob(r"D:\字谱智能体\*.docx")):
    try: d=Document(path)
    except Exception: continue
    for i,p in enumerate(d.paragraphs):
        t=(p.text or "").strip()
        if re.match(r"^36[45][.．、]",t):
            print(os.path.basename(path),"p",i,t[:26])