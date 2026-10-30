import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
p=os.path.join(C,"𤳯.json")
d=json.load(io.open(p,encoding="utf-8"))
d["aliases"]=["𤳐"]
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("card aliases",d["aliases"])