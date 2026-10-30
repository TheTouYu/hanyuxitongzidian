import json,io
p=r"D:\系统汉字\web\public\cards\朿.json"
d=json.load(io.open(p,encoding="utf-8"))
for s in d["sections"]:
    if s.get("key")=="erji":
        if not any(x.get("ch")=="責" for x in s.get("links",[])):
            s["links"].append({"ch":"責","label":"責"})
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print([x["ch"] for s in d["sections"] if s.get("key")=="erji" for x in s["links"]])