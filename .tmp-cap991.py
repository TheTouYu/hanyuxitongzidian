import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\尸.json"; d=json.load(io.open(p,encoding="utf-8"))
secs=[]
for s in d["sections"]:
    if s["key"]=="zizu":
        s["groups"]=[g for g in s["groups"] if not g["title"].startswith("本部二级字根")]
        secs.append(s)
        secs.append({"key":"erji","label":"本部二级字根","text":"尺：量尺，从尸足部标记，详见「尺」卡。","cites":[]})
    elif s["key"]!="erji":
        secs.append(s)
d["sections"]=secs
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
for s in d["sections"]: print(s["key"],s.get("label"))