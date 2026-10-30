import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
P=r"D:\系统汉字\web\public\glyphs\photos"; C=r"D:\系统汉字\web\public\cards"
# 1) 删卽误挂的玉人图，重编号
d=os.path.join(P,"卽")
os.remove(os.path.join(d,"01.png"))
os.replace(os.path.join(d,"02.jpg"), os.path.join(d,"01.jpg"))
ip=os.path.join(P,"index.json"); j=json.load(io.open(ip,encoding="utf-8")); ph=j["photos"]
ph["卽"]=["01.jpg"]
cp=os.path.join(P,"captions.json"); ca=json.load(io.open(cp,encoding="utf-8"))["captions"]
ca["卽"]=["漢畫像磚《宴飲圖》"]
ca["ㄗ"]=["商代玉人"]
json.dump({"photos":ph},io.open(ip,"w",encoding="utf-8"),ensure_ascii=False)
json.dump({"captions":ca},io.open(cp,"w",encoding="utf-8"),ensure_ascii=False)
# 2) 同步卡内
p=os.path.join(C,"卽.json"); k=json.load(io.open(p,encoding="utf-8"))
k["photos"]=["01.jpg"]; k["captions"]=["漢畫像磚《宴飲圖》"]
json.dump(k,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
p=os.path.join(C,"ㄗ.json"); k=json.load(io.open(p,encoding="utf-8"))
k["photos"]=["01.png"]; k["captions"]=["商代玉人"]
json.dump(k,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("fixed 卽(宴飲圖)/ㄗ(商代玉人)")