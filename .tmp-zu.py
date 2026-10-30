import glob,os
from docx import Document
for path in sorted(glob.glob(r"D:\字谱智能体\*.docx")):
    try: d=Document(path)
    except Exception: continue
    for i,p in enumerate(d.paragraphs):
        t=(p.text or "").strip()
        if t.startswith("宗") and "說文" in t and len(t)>20:
            print("ENTRY",os.path.basename(path),i,t[:70])