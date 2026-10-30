import io,json,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
a=json.load(io.open(r"D:\系统汉字\web\public\cards\卷一雞.json",encoding="utf-8"))
print([l for s in a["sections"] if s.get("key")=="juan" for l in s["links"]])
d=json.load(io.open(r"D:\系统汉字\web\public\cards\index.json",encoding="utf-8"))
e=[x for x in d if x.get("ch")]
print(json.dumps(e,ensure_ascii=True))