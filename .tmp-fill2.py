import json,glob,re,collections
md=open(r"knowledge\hanzi-yinyuan\02y-zika.md",encoding="utf-8").read()
head={}
for cid,title,body,bound in re.findall(r"<!-- CLAIM:START (clm_[0-9A-F]+) -->\s*\n### (.+?)\n(.*?)#### 适用边界\n(.*?)<!-- CLAIM:END",md,re.S):
    m=re.search(r"第\s*(\d+)\s*部「(.+?)部」",bound)
    if not m: continue
    bu=m.group(2)+"部"
    mb=re.search(r"【字根本義】(.*?)(?:\n\n【|\Z)",body,re.S)
    if mb and bu not in head: head[bu]=mb.group(1).strip()
def norm(b):
    if not b: return None
    m=re.match(r"\s*\d+[.．]\s*(.+)$",b)
    return (m.group(1).strip() if m else b.strip())
fixed=0; miss=collections.Counter(); ok=collections.Counter()
for p in glob.glob(r"web\public\cards\*.json"):
    d=json.load(open(p,encoding="utf-8"))
    if any(s.get("key")=="bengen" for s in d.get("sections",[])): continue
    bu=norm((d.get("bus") or [None])[0])
    txt=head.get(bu)
    if not txt: miss[bu]+=1; continue
    d["sections"].insert(0,{"key":"bengen","label":"字根本義","text":txt,"cites":[]})
    json.dump(d,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); fixed+=1; ok[bu]+=1
print("已补",fixed,"分布",dict(ok)); print("仍缺",sum(miss.values()),dict(miss))