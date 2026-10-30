import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\glyphs\photos\captions.json"
d=json.load(io.open(p,encoding="utf-8")); c=d.get("captions") or d
c["丂"]=["“丂”字形雁陣"]
c.setdefault("可",["斧柯"])
c.setdefault("號",["老虎嚎叫"])
json.dump({"captions":c},io.open(p,"w",encoding="utf-8"),ensure_ascii=False)
print("ok")