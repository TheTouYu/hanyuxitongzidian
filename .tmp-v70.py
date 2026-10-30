import io,json,glob,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
bad=0;tot=0
for f in glob.glob(r"D:\系统汉字\web\public\cards\卷*.json"):
    d=json.load(io.open(f,encoding="utf-8")); tot+=1
    for s in d["sections"]:
        for g in (s.get("groups") or []):
            h=g.get("header")
            if h and h[:1]==["字"]: bad+=1
print("卷卡",tot,"带旧表头组",bad)