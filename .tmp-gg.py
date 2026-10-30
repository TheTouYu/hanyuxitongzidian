import glob,os,re
from docx import Document
for path in sorted(glob.glob(r"D:\字谱智能体\*.docx")):
    try: d=Document(path)
    except Exception: continue
    ps=d.paragraphs
    for i,p in enumerate(ps):
        t=(p.text or "").strip()
        if re.match(r"^\d{1,3}[.．]\s*(冎|咼)",t):
            print("HEAD",os.path.basename(path),i,t)
            for j in range(i,min(len(ps),i+10)):
                tt=(ps[j].text or "").strip()
                if tt: print(" ",j,"|",tt[:150])
            raise SystemExit
print("none")