import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
idx=json.load(io.open(C+r"\index.json",encoding="utf-8"))
cov=set()
for x in idx:
    cov.add(x.get("c") or "")
    for a in (x.get("a") or []): cov.add(a)
from docx import Document
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷二  㠯.docx").paragraphs]
txt=" ".join(ps[685:730])
# 只取每条开头的正字与括注
pairs=re.findall(r"([^\s（(《a-zA-Z]{1,2})(（([^）]*)）)?\s*[a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü]+\s*《",txt)
miss=[]
for head,_,par,_,_2 in []: pass
for m in re.finditer(r"([^\s（(《a-zA-Z]{1,2})(?:（([^）]*)）)?\s*[a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü]+",txt):
    h=m.group(1); par=m.group(2) or ""
    for ch in list(h)+[c for c in re.sub(r"[^\u3400-\u9fff]","",par)]:
        if ch not in cov: miss.append(ch)
print("未覆盖",len(set(miss)), sorted(set(miss))[:40])