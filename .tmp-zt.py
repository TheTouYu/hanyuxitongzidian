import glob,io,os,re
from docx import Document
from docx.oxml.ns import qn
from PIL import Image
for path in sorted(glob.glob(r"D:\字谱智能体\*.docx")):
    try: d=Document(path)
    except Exception: continue
    ps=d.paragraphs
    for i,p in enumerate(ps):
        t=(p.text or "").strip()
        if re.match(r"^宗[（(：: ]",t) and ("《" in t or "本義" in t) and len(t)>15:
            print("ENTRY",os.path.basename(path),i,t[:60])