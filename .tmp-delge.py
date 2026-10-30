import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; G=r"D:\系统汉字\web\public\glyphs"
p=os.path.join(C,"蛤.json")
if os.path.exists(p):
    d=json.load(io.open(p,encoding="utf-8")); print("removing",d.get("head"),d.get("bus"),d.get("parent"))
    os.remove(p)
gd=os.path.join(G,"蛤")
if os.path.isdir(gd): print("glyph dir",os.listdir(gd))
p2=os.path.join(G,"index.json"); g=json.load(io.open(p2,encoding="utf-8"))
if "蛤" in g["chars"]: g["chars"].pop("蛤"); print("glyph entry removed")
json.dump({"chars":g["chars"]},io.open(p2,"w",encoding="utf-8"),ensure_ascii=False)