import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
d=json.load(io.open(r"D:\系统汉字\web\public\cards\反.json",encoding="utf-8"))
for s in d["sections"]:
    print("--",s.get("key"),s.get("label"),"|",(s.get("text") or "")[:60].replace("\n"," "))
    for g in s.get("groups",[]): print("   group:",g.get("title"),len(g.get("rows",[])))
print("glyphs:",len((json.load(io.open(r"D:\系统汉字\web\public\glyphs\index.json",encoding="utf-8"))["chars"].get("反",{}) or {}).get("files",[])))
print("photos:",json.load(io.open(r"D:\系统汉字\web\public\glyphs\photos\index.json",encoding="utf-8")).get("photos",{}).get("反"))