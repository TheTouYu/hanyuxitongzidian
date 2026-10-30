import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
chars=["締","諦","渧","𣽢","𧝐","蒂","揥","偙","楴","腣","崹","禘","鶙","䱱","碲"]
for ch in chars:
    p=os.path.join(C,ch+".json")
    if os.path.exists(p):
        d=json.load(io.open(p,encoding="utf-8"))
        print(ch,[s["label"] for s in d.get("sections",[])])
    else: print(ch,"無卡")