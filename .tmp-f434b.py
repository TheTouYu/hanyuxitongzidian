import glob,os,re
from docx import Document
for path in sorted(glob.glob(r"D:\字谱智能体\*.docx")):
    try: d=Document(path)
    except Exception: continue
    ps=[(p.text or "").strip() for p in d.paragraphs]
    for i,t in enumerate(ps):
        m=re.match(r"^(43[0-9])[.．、]\s*(\S{1,6})部",t)
        if m and int(m.group(1))>=434:
            print(os.path.basename(path),"p",i,t[:40])
            for j in range(i+1,min(len(ps),i+30)):
                if ps[j]: print("  ",j,ps[j][:80])
            raise SystemExit
print("none")