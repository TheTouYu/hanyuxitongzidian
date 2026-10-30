import sys,glob,re,json,os
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ROOT=r"D:\系统汉字"
cards={os.path.basename(p)[:-5] for p in glob.glob(ROOT+r"\web\public\cards\*.json")}
pat=re.compile(r"^([\u3400-\u9fff\U00020000-\U0002ffff]{1,3})\s*([（(][^）)]{0,30}[）)])?\s*([a-zA-Züāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜǹńňǚ]{1,12})\s*[，,]?\s*《")
heads={}
for f in glob.glob(r"D:\字谱智能体\*.docx"):
    try: ps=[p.text.strip() for p in Document(f).paragraphs]
    except: continue
    for t in ps:
        m=pat.match(t)
        if m: heads.setdefault(m.group(1)[0] if len(m.group(1))>1 else m.group(1),0)
miss=[h for h in heads if h not in cards]
print("字头总数",len(heads),"缺卡",len(miss))
print("样本",miss[:40])
json.dump({"total":len(heads),"missing":miss},open(ROOT+r"\.tmp-coverage.json","w",encoding="utf-8"),ensure_ascii=False)