import glob,os
from docx import Document
for path in sorted(glob.glob(r"D:\字谱智能体\*.docx")):
    try: d=Document(path)
    except Exception: continue
    ps=d.paragraphs
    for i,p in enumerate(ps):
        t=(p.text or "").strip()
        if ("𣎆" in t[:12] or t.startswith("羸") or t.startswith("贏（")) and len(t)>8:
            print("HIT",os.path.basename(path),i,"|",t[:150]); print("   NEXT:",(ps[i+1].text or "")[:160] if i+1<len(ps) else "")
            raise SystemExit