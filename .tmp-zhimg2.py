import os,json,sys,shutil
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
out=r"D:\系统汉字\web\public\glyphs\photos\旨"
names=[]
for f in sorted(os.listdir(out)):
    if not f.endswith(".jpg"): continue
    b=open(os.path.join(out,f),"rb").read(8)
    ext=".png" if b.startswith(b"\x89PNG") else ".jpg"
    nf=f[:-4]+ext
    os.replace(os.path.join(out,f),os.path.join(out,nf)); names.append(nf)
p=r"D:\系统汉字\web\public\glyphs\photos\index.json"
d=json.load(open(p,encoding="utf-8")); ph=d.get("photos") or d
ph["旨"]=names; json.dump({"photos":ph},open(p,"w",encoding="utf-8"),ensure_ascii=False)
print(names)