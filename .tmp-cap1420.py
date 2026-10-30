import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
d=json.load(io.open(os.path.join(C,"朿.json"),encoding="utf-8"))
for s in d["sections"]:
    if s.get("key")=="erji": print("erji links",[x.get("ch") for x in s.get("links",[])])
z=json.load(io.open(os.path.join(C,"責.json"),encoding="utf-8"))
print("責 level",z.get("level"),"parent",z.get("parent"),"groups",[ (g["title"],len(g["rows"])) for s in z["sections"] if s.get("key")=="zizu" for g in s["groups"]])