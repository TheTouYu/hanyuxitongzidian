import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
n=0
for f in os.listdir(C):
    if not f.endswith(".json") or f=="index.json" or f=="variants.json": continue
    d=json.load(io.open(os.path.join(C,f),encoding="utf-8"))
    if d.get("level")==2 and not any(s.get("key")=="zizu" for s in d.get("sections",[])):
        d["sections"].append({"key":"zizu","label":"字族衍义","text":"（原稿本部未列以本字为聲符之字，故字族表缺）","cites":[]})
        json.dump(d,io.open(os.path.join(C,f),"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("patched",n)