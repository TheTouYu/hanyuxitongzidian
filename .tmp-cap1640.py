import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
fix={"𠬨":"j「聚决」取「聚」：屈膝而治事有所制（推）。","𩱺":"j「聚决」取「聚」：器中聚食（推）。"}
for ch,t in fix.items():
    p=C+"\\"+ch+".json"; d=json.load(io.open(p,encoding="utf-8"))
    for s in d["sections"]:
        if s["key"]=="shengmu": s["text"]=t
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("fixed")