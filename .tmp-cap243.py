import os,json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
I=set(os.listdir(r"D:\系统汉字\web\public\glyphs\inline"))
C=r"D:\系统汉字\web\public\cards"
for ch in list(I)[:6]:
    p=os.path.join(C,ch+".json")
    if not os.path.exists(p): continue
    d=json.load(io.open(p,encoding="utf-8"))
    print(ch,[s["key"] for s in d["sections"]], os.listdir(os.path.join(r"D:\系统汉字\web\public\glyphs\inline",ch)))