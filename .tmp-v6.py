import io,json,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\卷一雞.json"
d=json.load(io.open(p,encoding="utf-8"))
d["trad"]="卷一雞"; d["simp"]="卷一鸡"; d["aliases"]=["卷一","卷一鸡","卷"]
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("ok")