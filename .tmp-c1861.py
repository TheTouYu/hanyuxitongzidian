import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\ㄗ.json"
d=json.load(io.open(p,encoding="utf-8"))
for s in d["sections"]:
    if s.get("key")=="erji":
        s["links"]=[{"ch":x,"label":x} for x in ("卽","肥","配","邑","印","氾")]
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("ㄗ 二级六链接")