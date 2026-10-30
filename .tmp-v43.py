import io,json,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; tot=hit=0
for f in os.listdir(C):
    if not f.startswith("卷"): continue
    d=json.load(io.open(os.path.join(C,f),encoding="utf-8"))
    for s in d.get("sections",[]):
        if s.get("key")=="zizu":
            for r in s["groups"][0]["rows"]:
                tot+=1; hit+= (r[2]!="—")
print("部目行",tot,"有中心义",hit)