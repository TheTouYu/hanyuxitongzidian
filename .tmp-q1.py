import json,os
p=r"D:\系统汉字\web\public\glyphs\index.json"
d=json.load(open(p,encoding="utf-8"))
chars=d.get("chars",{})
for c in ["银","銀","金","艮","限","根","跟","很","恨","痕","肯"]:
    v=chars.get(c)
    print(c, (len(v.get("files",[])) if v else 0), (v.get("doc","") if v else ""))