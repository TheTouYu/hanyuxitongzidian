import json,io,os,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
k=0; miss=[]
for f in os.listdir(C):
    if not f.endswith(".json") or f=="index.json": continue
    try: d=json.load(io.open(os.path.join(C,f),encoding="utf-8"))
    except Exception: continue
    if not isinstance(d,dict): continue
    for s in d.get("sections",[]):
        if isinstance(s,dict) and s.get("key")=="shiyi" and '<img class="gin"' in s.get("text",""):
            if k<2: print(d["char"],"|",s["text"][:90].replace("\n"," "))
            k+=1
print("含换入图卡",k)
for f in os.listdir(C):
    if not f.endswith(".json") or f=="index.json": continue
    try: d=json.load(io.open(os.path.join(C,f),encoding="utf-8"))
    except Exception: continue
    if not isinstance(d,dict): continue
    for s in d.get("sections",[]):
        if isinstance(s,dict) and s.get("key")=="shiyi" and re.search(r"。，",s.get("text","")) and len(miss)<15:
            miss.append(d["char"])
print("仍待处理",len(miss),miss)