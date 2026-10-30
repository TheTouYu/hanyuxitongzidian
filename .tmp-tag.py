import io,sys,json,glob,os
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
h=r"D:\系统汉字\web\public\test.html"
s=io.open(h,encoding="utf-8").read()
a=s.replace("d.level===1?'一級字根':d.level===2?'二級字根':'字根衍生字'",
            "d.level===1?'一級字根':d.level===2?'二級字根':'谐声字'",1)
b=a.replace('字理分析·字根「${esc(d.parent)}」','字根「${esc(d.parent)}」',1)
io.open(h,"w",encoding="utf-8",newline="\n").write(b)
n=0
for f in glob.glob(r"D:\系统汉字\web\public\cards\*.json"):
    if os.path.basename(f) in ("index.json","variants.json"): continue
    d=json.load(open(f,encoding="utf-8"))
    secs=[x for x in d.get("sections",[]) if not (isinstance(x,dict) and x.get("key")=="lili")]
    if len(secs)!=len(d.get("sections",[])):
        d["sections"]=secs; json.dump(d,open(f,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("cards fixed",n,"| tag ok:", "谐声字" in b, "| heading:", "字理分析·字根" in b)