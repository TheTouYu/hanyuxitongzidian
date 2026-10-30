import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
out=[]
for fn in os.listdir(C):
    if not fn.endswith(".json") or fn=="index.json": continue
    d=json.load(io.open(os.path.join(C,fn),encoding="utf-8"))
    if d.get("parent") not in ("尗","叔","曳"): continue
    s=[x for x in d["sections"] if x["key"]=="shengmu"]
    if s and s[0]["text"].startswith("y「零聲母"):
        out.append((d["char"],d.get("pinyin","")))
print(len(out)); print(out)