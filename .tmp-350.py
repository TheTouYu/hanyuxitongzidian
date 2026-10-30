import glob,os
from docx import Document
for path in sorted(glob.glob(r"D:\字谱智能体\*.docx")):
    try: d=Document(path)
    except Exception: continue
    ps=[(p.text or "").strip() for p in d.paragraphs]
    for i,t in enumerate(ps):
        if t.startswith("350.") or t.startswith("350．"):
            print("HIT",os.path.basename(path),"p",i,t[:40])
            n=0
            for j in range(i+1,min(len(ps),i+160)):
                s=ps[j]
                if s[:4] in ("351.","351．"): break
                if len(s)>10 and "《" in s[:18]:
                    print(" p%d %s"%(j,s[:120])); n+=1
                    if n>=10: break
            raise SystemExit
print("not found")