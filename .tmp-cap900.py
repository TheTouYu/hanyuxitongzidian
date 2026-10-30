import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
have={}
for fn in os.listdir(C):
    if not fn.endswith(".json") or fn in ("index.json",): continue
    try: d=json.load(io.open(os.path.join(C,fn),encoding="utf-8"))
    except: continue
    for k in [d.get("char"),d.get("trad"),d.get("simp")]+list(d.get("aliases") or []):
        if k: have[k]=1
raw=open(r"D:\字谱智能体\汉字简体繁体对照表大全资料.txt","rb").read().decode("gb18030")
pairs=[]; seen=set()
for s,f in re.findall(r"([\u3400-\u9fff])=([\u3400-\u9fff])",raw):
    if s in seen: continue
    seen.add(s); pairs.append((s,f))
todo=[(s,f) for s,f in pairs if s not in have and f not in have]
print("总",len(pairs),"已有",len(pairs)-len(todo),"待建",len(todo))
print(todo[:8])