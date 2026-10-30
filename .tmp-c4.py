from docx import Document
import json,io,glob,sys,os
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷一  雞.docx").paragraphs]
for k in range(0,6): print(k,repr(ps[k][:60]))
f=glob.glob(r"D:\系统汉字\web\public\cards\卷一雞.json")
print("volcard",f)
d=json.load(io.open(f[0],encoding="utf-8"))
for s in d["sections"]:
    if s.get("key")=="zizu":
        for g in s.get("groups") or []:
            print("G",g.get("title"),len(g.get("rows",[])),[r[0] for r in g["rows"]][:4])