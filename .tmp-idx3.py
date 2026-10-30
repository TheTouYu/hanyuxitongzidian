import json,glob,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
items=[]
for f in glob.glob(C+r"\*.json"):
    if os.path.basename(f)=="index.json": continue
    try: d=json.load(open(f,encoding="utf-8"))
    except: continue
    b=(d.get("bus") or [{}])[0]
    if isinstance(b,str): num,name=0,b
    else: num,name=b.get("num",0),b.get("name","")
    items.append({"char":d.get("char",""),"pinyin":d.get("pinyin",""),"num":num,"name":name,"level":d.get("level",0)})
items.sort(key=lambda x:x["char"])
json.dump(items,open(C+r"\index.json","w",encoding="utf-8"),ensure_ascii=False)
print("index",len(items))