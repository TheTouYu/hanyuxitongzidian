import re,json,subprocess,os
mp=json.load(open(r".tmp-bu.json",encoding="utf-8"))
name2num={v:k for k,v in mp.items()}
t=open(r"knowledge\hanzi-yinyuan\02y-zika.md",encoding="utf-8").read()
blocks=re.findall(r"<!-- CLAIM:START (clm_[0-9A-F]+) -->\s*### (.*?)\n+(.*?)\n+#### 适用边界\n+(.*?)\n+<!-- CLAIM:END",t,re.S)
fix=[]
for cid,title,body,bd in blocks:
    m=re.search(r"第(\d+)部「(.+?)部」",bd)
    if not m: continue
    n,nam=m.group(1),m.group(2)
    if mp.get(n)==nam: continue
    if nam not in name2num: continue
    nb=bd.replace(f"第{n}部「{nam}部」",f"第{name2num[nam]}部「{nam}部」",1)
    fix.append((cid,body.strip().replace("\n",""),nb.strip(),title))
print("fixable",len(fix))
json.dump([{"id":c,"statement":b,"boundary":nb,"title":ti} for c,b,nb,ti in fix],open(r".tmp-fixbd.json","w",encoding="utf-8"),ensure_ascii=False)
print(fix[0][3][:30] if fix else "")