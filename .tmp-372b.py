import glob,os,re
from docx import Document
d=Document(r"D:\字谱智能体\卷六十三  索.docx"); ps=[(p.text or "").strip() for p in d.paragraphs]
have={os.path.splitext(f)[0] for f in os.listdir(r"web\public\cards")}
miss=[]
for i in range(58,140):
    t=ps[i] if i<len(ps) else ""
    m=re.match(r"^([\u3400-\u9fff\U00020000-\U0002A6DF])[（(]?.*?[a-zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü]{1,6}",t)
    if m and len(t)>25 and "\ufffd" not in t:
        ch=m.group(1)
        if ch not in have and ch not in ("束",):
            miss.append((i,ch,t[:150]))
print("missing",len(miss))
for i,ch,body in miss[:12]:
    print("==",ch,"p",i)
    print(body)