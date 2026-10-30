# -*- coding: utf-8 -*-
import json,sys,io
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\旨.json"
d=json.load(open(p,encoding="utf-8")); n=0
for s in d["sections"]:
    for g in s.get("groups",[]) or []:
        for r in g["rows"]:
            t=r[3]
            if t.startswith("原稿未標書名："):
                r[3]=t.replace("原稿未標書名：","",1); n+=1
json.dump(d,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
e=r"D:\系统汉字\prompts\exegesis.md"; s=io.open(e,encoding="utf-8").read()
s=s.replace("（《說文》《廣韻》《字彙》《新附》等；原稿未标者注明「原稿未標書名」）；","（《說文》《廣韻》《字彙》《新附》等；原稿本来没有书名的，不标、也不要注明缺失）；")
io.open(e,"w",encoding="utf-8",newline="\n").write(s)
print("fixed rows",n)