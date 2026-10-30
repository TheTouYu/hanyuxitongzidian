import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
d=json.load(io.open(r"D:\系统汉字\web\public\cards\措.json",encoding="utf-8"))
print(d.get("char"),d.get("head"),d.get("aliases"),d.get("pinyin"))
print(d["sections"][0]["text"][:80])