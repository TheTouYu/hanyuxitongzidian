import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
for ch in ("𩦽","𤐽","駘","炱"):
    p=os.path.join(C,ch+".json")
    if os.path.exists(p):
        d=json.load(io.open(p,encoding="utf-8"))
        print(ch,"head",d.get("head"),"al",d.get("aliases"),"parent",d.get("parent"))
    else: print(ch,"无卡")