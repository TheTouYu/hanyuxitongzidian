import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\夷.json"
d=json.load(io.open(p,encoding="utf-8"))
d["head"]="夷（𡗝𡰥𡖴𢎯）"
d["aliases"]=["𡗝","𡰥","𡖴","𢎯"]
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("head",d["head"])