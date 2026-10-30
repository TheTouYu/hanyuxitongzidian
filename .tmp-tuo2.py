from docx import Document
d=Document(r"D:\字谱智能体\卷六十  𦟀.docx")
ps=[(p.text or "").strip() for p in d.paragraphs]
for j in range(302,345):
    t=ps[j]
    if not t: continue
    if t[0] in "娞綏哸餒㞂荽鵎婑嗺鐁鮾餧㾼" or (len(t)>6 and "《" in t[:20]):
        print(j, t[:130])