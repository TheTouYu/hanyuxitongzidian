import json,io,os,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; bad=[]; n=0
for fn in os.listdir(C):
    if not fn.endswith(".json") or fn=="index.json": continue
    d=json.load(io.open(os.path.join(C,fn),encoding="utf-8"))
    if d.get("parent") not in ("尗","叔","曳"): continue
    n+=1
    s=[x for x in d["sections"] if x["key"]=="shengmu"]
    if not s or "零聲母" in s[0]["text"] and d.get("pinyin","").lstrip().startswith(("y","w"))==False: bad.append((d["char"],s[0]["text"][:20] if s else ""))
print("族卡",n,"不合",len(bad),bad[:5])