import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\射.json"; d=json.load(io.open(p,encoding="utf-8"))
for s in d["sections"]:
    if s["key"]=="zizu":
        s["text"]="字族衍義：多指射箭，表示離、棄、速"
        s["groups"][0]["note"]="多指射箭，表示離、棄、速"
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("ok")