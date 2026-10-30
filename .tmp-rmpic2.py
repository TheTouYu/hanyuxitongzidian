import json,io,os,shutil,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
P=r"D:\系统汉字\web\public\glyphs\photos"
ch="𤳯"
d=os.path.join(P,ch)
if os.path.isdir(d): shutil.rmtree(d); print("rm dir")
for name,key in (("index.json","photos"),("captions.json","captions")):
    p=os.path.join(P,name)
    x=json.load(io.open(p,encoding="utf-8")); m=x.get(key) or x
    if ch in m: m.pop(ch); print("clean",name)
    json.dump({key:m},io.open(p,"w",encoding="utf-8"),ensure_ascii=False)
# photos.js
pj=r"D:\系统汉字\web\public\photos.js"
s=io.open(pj,encoding="utf-8").read()
s2=re.sub(r'"%s":\s*\[[^\]]*\]\s*,?'%re.escape(ch),"",s)
open(pj,"w",encoding="utf-8",newline="\n").write(s2)
print("photos.js changed", s!=s2)