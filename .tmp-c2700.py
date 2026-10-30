import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\惄.json"
d=json.load(io.open(p,encoding="utf-8"))
als=["愵","𢙤","𢞤","𢞔","𧖷","𧗂","𩚮","𢜷"]
d["head"]="惄（"+"".join(als)+"）"; d["aliases"]=als
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("惄 head/aliases ok")