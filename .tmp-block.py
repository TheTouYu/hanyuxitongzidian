import re
md=open(r"knowledge\hanzi-yinyuan\02y-zika.md",encoding="utf-8").read()
m=re.search(r"<!-- CLAIM:START (clm_[0-9A-F]+) -->\s*\n### 刑(.+?)\n([\s\S]*?)<!-- CLAIM:END",md)
print(m.group(0)[:700] if m else "no")