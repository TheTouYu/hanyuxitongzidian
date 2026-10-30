import json,io,glob,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
n=0; ex=[]
for p in glob.glob(r"D:\系统汉字\web\public\cards\*.json"):
    if p.endswith("index.json"): continue
    d=json.load(io.open(p,encoding="utf-8"))
    for s in d.get("sections",[]):
        if "gscroll" in (s.get("text") or ""):
            n+=1
            if len(ex)<3: ex.append(d["char"])
            break
print("含gscroll卡",n,ex)
gi=json.load(io.open(r"D:\系统汉字\web\public\glyphs\index.json",encoding="utf-8"))["chars"]
print("帝files",gi.get("帝",{}).get("files",[])[:2])