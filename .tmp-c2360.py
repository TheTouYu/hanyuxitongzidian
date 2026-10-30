import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
for ch,ph,caps in (("尗",[],[]),):
    d=json.load(io.open(C+"\\"+ch+".json",encoding="utf-8"))
    d.pop("photos",None); d.pop("captions",None)
    json.dump(d,io.open(C+"\\"+ch+".json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("尗 卡去掉误挂照片（花椒归茮）")