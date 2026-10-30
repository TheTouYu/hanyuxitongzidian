import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
d=json.load(io.open(C+r"\尗.json",encoding="utf-8"))
d["head"]="尗"; d["aliases"]=[]
json.dump(d,io.open(C+r"\尗.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("head fixed")