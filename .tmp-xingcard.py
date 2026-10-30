import json,re
d=json.load(open(r"web\public\cards\娙.json",encoding="utf-8"))
print("bus:",d["bus"]); print("bengen:",d["sections"][0]["text"][:60])
md=open(r"knowledge\hanzi-yinyuan\02y-zika.md",encoding="utf-8").read()
m=re.search(r"<!-- CLAIM:START (clm_[0-9A-F]+) -->\s*\n### 娙[^\n]*\n\n([\s\S]*?)\n\n#### 适用边界\n\n([\s\S]*?)\n",md)
print("claim:",m.group(1)); print("stmt:",m.group(2)[:80]); print("bound:",m.group(3))