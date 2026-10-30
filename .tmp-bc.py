import re,collections
t=open(r"knowledge\hanzi-yinyuan\02y-zika.md",encoding="utf-8").read()
pairs=re.findall(r"第(\d+)部「(.+?)」",t)
c=collections.Counter(pairs)
for (n,b),k in sorted(c.items(),key=lambda x:int(x[0][0])):
    if 415<=int(n)<=445: print(n,b,k)