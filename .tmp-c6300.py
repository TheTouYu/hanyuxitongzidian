import json,io,re,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; n=0
for fn in os.listdir(C):
    if not fn.endswith(".json") or fn=="index.json": continue
    p=os.path.join(C,fn); d=json.load(io.open(p,encoding="utf-8"))
    if d.get("parent")!="弟": continue
    ch=re.sub(r"[a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü]+$","",d["char"])
    if ch!=d["char"]: d["char"]=ch; n+=1
    h=d.get("head") or ch
    h=re.sub(r"([^\s（(])[a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü]+$",r"\1",h)
    d["head"]=h
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("fixed",n)