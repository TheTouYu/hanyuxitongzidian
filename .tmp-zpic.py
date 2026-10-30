# -*- coding: utf-8 -*-
import json,io,os,shutil,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
P=r"D:\系统汉字\web\public\glyphs\photos"
files=sorted(os.listdir(os.path.join(P,"詹")))
print(files)
def move(src,dst_ch,cap,idx_cap):
    d=os.path.join(P,dst_ch); os.makedirs(d,exist_ok=True)
    for f in os.listdir(d): os.remove(os.path.join(d,f))
    shutil.move(os.path.join(P,"詹",src), os.path.join(d,"01.jpg"))
    return "01.jpg"
m1=move(files[1],"韂","馬障泥（原稿p371 有障泥的唐三彩馬）",None)
m2=move(files[2],"膽","膽囊位置示意圖（原稿p374）",None)
ip=os.path.join(P,"index.json"); ix=json.load(io.open(ip,encoding="utf-8")); mp=ix.get("photos") or ix
mp["詹"]=[files[0]]; mp["韂"]=[m1]; mp["膽"]=[m2]
json.dump({"photos":mp},io.open(ip,"w",encoding="utf-8"),ensure_ascii=False)
cp=os.path.join(P,"captions.json"); cx=json.load(io.open(cp,encoding="utf-8")); mc=cx.get("captions") or cx
old=mc.get("詹") or []
mc["詹"]=[old[0] if old else "燕子在屋簷下築巢"]; mc["韂"]=["有障泥的唐三彩馬"]; mc["膽"]=["膽囊位置示意圖"]
json.dump({"captions":mc},io.open(cp,"w",encoding="utf-8"),ensure_ascii=False)
print("詹",mp["詹"],"韂",mp["韂"],"膽",mp["膽"])