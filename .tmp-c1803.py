import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
for ch in ["悒","裛","㛕","𥒵","𨹝","挹","浥","䱒","䓃","䭂","𦀕","𦛞","𪁗"]:
    p=os.path.join(C,ch+".json"); d=json.load(io.open(p,encoding="utf-8"))
    for s in d["sections"]:
        if s["key"]=="shengmu":
            s["text"]="y「零声母」不系：零聲母，緒論七組未列（照實）。"
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("ok")