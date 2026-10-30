import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
G=r"D:\系统汉字\web\public\glyphs"
p=os.path.join(G,"index.json"); ix=json.load(io.open(p,encoding="utf-8")); ch=ix["chars"]
files=sorted(f for f in os.listdir(os.path.join(G,"彥")))
ch["彥"]={"doc":"卷五  雁.docx","variants":["𢒊"],"files":["彥/"+f for f in files]}
json.dump({"chars":ch},io.open(p,"w",encoding="utf-8"),ensure_ascii=False)
print(files)