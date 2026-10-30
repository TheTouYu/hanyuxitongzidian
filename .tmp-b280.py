from docx import Document
import re,glob
S=r"D:\字谱智能体"
for p in glob.glob(rf"{S}\*.docx"):
    try: d=Document(p)
    except Exception: continue
    P=d.paragraphs
    for i,q in enumerate(P):
        if re.match(r"44[01]\.",q.text.strip()):
            print("=====",p.split("\\")[-1],q.text.strip()[:60]); n=0
            for r in P[i+1:i+50]:
                s=r.text.strip()
                if not s: continue
                if re.match(r"\d{3}\.",s): break
                print(s[:160]); n+=1
                if n>=30: break
            break