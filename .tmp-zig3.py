import json,glob
none=[];has=[]
for p in glob.glob(r"web\public\cards\*.json"):
    c=json.load(open(p,encoding="utf-8"))
    s=[x for x in c["sections"] if x["key"]=="zigen"]
    if not s: continue
    (none if "未收" in s[0]["text"] else has).append(c.get("char"))
print("none",len(none),none[:12])
print("has",len(has),sorted(has)[:12])