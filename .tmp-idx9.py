import sys,glob,os,json
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
ROOT=r"D:\系统汉字"
out=[]
for fp in glob.glob(ROOT+r"\web\public\cards\*.json"):
    if os.path.basename(fp)=="index.json": continue
    try: d=json.load(open(fp,encoding="utf-8"))
    except: continue
    if not isinstance(d,dict): continue
    ch=d.get("char") or os.path.basename(fp)[:-5]; b=d.get("bus") or []; b0=b[0] if b and isinstance(b[0],dict) else {}
    out.append({"c":ch,"p":d.get("pinyin",""),"b":b0.get("num",""),"n":b0.get("name",""),"lv":d.get("level",0),
                "t":[s.get("text","")[:24] for s in d.get("sections",[]) if isinstance(s,dict)]})
out.sort(key=lambda x:(x["b"] if isinstance(x["b"],int) else 999,x["c"]))
json.dump(out,open(ROOT+r"\web\public\cards\index.json","w",encoding="utf-8"),ensure_ascii=False,separators=(",",":"))
print("cards",len(out))