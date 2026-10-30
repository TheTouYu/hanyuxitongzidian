import json,io,glob,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
bad=[]
for f in glob.glob(C+r"\*.json"):
    if os.path.basename(f) in ("index.json","variants.json"): continue
    d=json.load(io.open(f,encoding="utf-8"))
    if (d.get("parent") or "") in ("台","氐","矣"):
        sm=[s for s in d["sections"] if s.get("key")=="shengmu"]
        if sm and "㠯部聲母為零" in sm[0]["text"]: bad.append((d["char"],d["parent"]))
print(len(bad),bad[:12])