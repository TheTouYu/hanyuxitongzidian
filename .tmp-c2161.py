import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\弋.json"; d=json.load(io.open(p,encoding="utf-8"))
for s in d["sections"]:
    if s["key"]=="zizu":
        for g in s["groups"]:
            if g["title"].startswith("④"):
                g["rows"]=[["鋱","tè","金","鋱tè：音譯字。一種金屬元素，符號Tb，屬稀土金屬，無色結晶的粉末，有毒。它的化合物可做殺蟲劑，亦用來治療皮膚病。"]]
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("④组补鋱")