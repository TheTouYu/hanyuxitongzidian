import json,io,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
d=json.load(io.open(r"D:\系统汉字\web\public\cards\支.json",encoding="utf-8"))
seen=set();names=[]
for s in d["sections"]:
    for g in s.get("groups") or []:
        for r in g.get("rows") or []:
            c=re.sub(r"（.*?）|\(.*?\)","",str(r[0])).strip()
            if c and c not in seen: seen.add(c); names.append(c)
print(len(names)); print(" ".join(names))