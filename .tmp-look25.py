import sys,glob,json,re,os
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
targets=["谷","干","斗","台"]
found={}
for f in glob.glob(r"D:\字谱智能体\*.docx"):
    try: ps=[p.text.strip() for p in Document(f).paragraphs]
    except: continue
    for t in targets:
        if t in found: continue
        for i,x in enumerate(ps):
            if x.startswith(t) and len(x)<400 and ("《說文》" in x or "《说文》" in x):
                found[t]=x; break
for t in targets:
    print(t,"=>",found.get(t,"")[:150])
print("---")
C=r"D:\系统汉字\web\public\cards"
for ch in ["谷","干"]:
    if ch not in found: continue
    p=os.path.join(C,ch+".json"); d=json.load(open(p,encoding="utf-8"))
    for s in d["sections"]:
        if s.get("key")=="benyi":
            s["text"]="（依原稿原文）"+found[ch]
    json.dump(d,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("rewritten")