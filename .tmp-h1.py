import re,glob,json
pat=re.compile(r"<!-- CLAIM:START (clm_[0-9A-F]+) -->\s*\n### (.+?)\n(.*?)#### 适用边界\n(.*?)<!-- CLAIM:END", re.S)
for f in glob.glob(r"D:\系统汉字\knowledge\**\*.md", recursive=True):
    t=open(f,encoding="utf-8").read()
    for cid,title,body,bound in pat.findall(t):
        if ("海" in title) or ("海" in body[:200] and ("每" in title or "水" in title)):
            print(cid,"|",title.strip()[:50],"|",bound.strip()[:40])
            print("   ",body.strip().replace("\n"," ")[:230]); print()