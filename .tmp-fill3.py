import json,glob,re
from docx import Document
d=Document(r"D:\字谱智能体\卷六十三  索.docx"); ps=[(p.text or "").strip() for p in d.paragraphs]
head={}
for i,t in enumerate(ps):
    m=re.match(r"^(\d{3})[.．](\S{1,6}?)部$",t)
    if not m: continue
    num,name=int(m.group(1)),m.group(2)
    txt=""
    for j in range(i+1,min(len(ps),i+40)):
        s=ps[j]
        if re.match(r"^\d{3}[.．]",s): break
        if s.startswith("本義："):
            txt=s[3:]
            break
    if txt: head[num]=(name,txt)
print("部头取到",sorted(head)[:20],"共",len(head))
fixed=0
for p in glob.glob(r"web\public\cards\*.json"):
    c=json.load(open(p,encoding="utf-8"))
    if any(s.get("key")=="bengen" for s in c.get("sections",[])): continue
    bus=(c.get("bus") or [""])[0]
    m=re.match(r"(\d{3})",bus)
    if not m: continue
    num=int(m.group(1)); h=head.get(num)
    if not h: continue
    name,txt=h
    text=txt.strip()
    if len(text)>240: text=text[:236]+"……"
    c["sections"].insert(0,{"key":"bengen","label":"字根本義","text":text,"cites":[]})
    json.dump(c,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); fixed+=1
print("已补",fixed)
