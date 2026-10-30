import json,io,os,shutil,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
P=r"D:\系统汉字\web\public\glyphs\photos"
src=os.path.join(P,"號","01.jpg"); dst=os.path.join(P,"号")
os.makedirs(dst,exist_ok=True)
for f in os.listdir(dst): os.remove(os.path.join(dst,f))
shutil.copyfile(src,os.path.join(dst,"01.jpg"))
for name,key,val in (("index.json","photos",["01.jpg"]),("captions.json","captions",["老虎嚎叫"])):
    p=os.path.join(P,name); d=json.load(io.open(p,encoding="utf-8")); m=d.get(key) or d
    m["号"]=val; json.dump({key:m},io.open(p,"w",encoding="utf-8"),ensure_ascii=False)
print("ok")