import json,glob,re
from docx import Document
want=set(range(353,364))
head={}
for path in sorted(glob.glob(r"D:\字谱智能体\*.docx")):
    try: d=Document(path)
    except Exception: continue
    ps=[(p.text or "").strip() for p in d.paragraphs]
    for i,t in enumerate(ps):
        m=re.match(r"^(\d{3})[.．](\S{1,8}?)部$",t)
        if not m: continue
        num=int(m.group(1))
        if num not in want or num in head: continue
        txt=""
        for j in range(i+1,min(len(ps),i+40)):
            s=ps[j]
            if re.match(r"^\d{3}[.．]",s): break
            if s.startswith("本義："): txt=s[3:]; break
        if txt: head[num]=(m.group(2),txt,path)
print("取到部头",sorted(head))
fixed=0; miss=0
for p in glob.glob(r"web\public\cards\*.json"):
    c=json.load(open(p,encoding="utf-8"))
    if any(s.get("key")=="bengen" for s in c.get("sections",[])): continue
    m=re.match(r"(\d{3})",(c.get("bus") or [""])[0])
    if not m: miss+=1; continue
    h=head.get(int(m.group(1)))
    if not h: miss+=1; continue
    tx=h[1].strip()
    if len(tx)>240: tx=tx[:236]+"……"
    c["sections"].insert(0,{"key":"bengen","label":"字根本義","text":tx,"cites":[]})
    json.dump(c,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); fixed+=1
print("已补",fixed,"仍缺",miss)