import json,glob,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
items=[]
for f in glob.glob(C+r"\*.json"):
    if os.path.basename(f) in ("index.json","variants.json"): continue
    try: d=json.load(open(f,encoding="utf-8"))
    except: continue
    b=(d.get("bus") or [{}])[0]; num,name=(b.get("num",0),b.get("name","")) if isinstance(b,dict) else (0,b)
    tags=[x.get("label","") for x in d.get("sections",[]) if isinstance(x,dict)]
    if name: tags.append(name+"部")
    items.append({"c":d.get("trad") or d.get("char",""),"a":d.get("simp",""),"p":d.get("pinyin",""),"t":tags,"b":num,"n":name,"lv":d.get("level",0)})
items.sort(key=lambda x:x["c"])
json.dump(items,open(C+r"\index.json","w",encoding="utf-8"),ensure_ascii=False)
print(len(items))