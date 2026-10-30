import json,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\index.json"
idx=json.load(open(p,encoding="utf-8"))
have={x["c"] for x in idx}
for ch in ["尔","你","弥"]:
    if ch in have: continue
    d=json.load(open(rf"D:\系统汉字\web\public\cards\{ch}.json",encoding="utf-8"))
    idx.insert(0,{"c":ch,"p":d["pinyin"],"b":d["bus"][0]["num"],"n":d["bus"][0]["name"],"lv":d["level"],
                  "t":[s["text"][:80] for s in d["sections"] if s.get("text")][:3]})
json.dump(idx,open(p,"w",encoding="utf-8"),ensure_ascii=False,separators=(",",":"))
print("idx",len(idx))