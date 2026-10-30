import glob
from docx import Document
for path in sorted(glob.glob(r"D:\字谱智能体\*.docx")):
    try: d=Document(path)
    except Exception: continue
    ps=[(p.text or "").strip() for p in d.paragraphs]
    for i,t in enumerate(ps):
        if t.startswith("348.") or t.startswith("348．") or "348." == t[:4]:
            print("HIT",path.split("\\")[-1],"p",i,t[:40])
            n=0
            for j in range(i+1,min(len(ps),i+300)):
                s=ps[j]
                if s and s[0] in "349" and s[1:2] in "..。": break
                if len(s)>8 and s[0].isalpha() is False and s[1:3] in ("（","《") or (len(s)>10 and "《" in s[:14]):
                    print(f"  p{j} {s[:90]}"); n+=1
                    if n>=8: break
            raise SystemExit