# -*- coding: utf-8 -*-
import io,re,json,glob,sys,subprocess,tempfile,os
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
old="<p>${esc(s.text)}</p>"
new="${s.text?('<p style=\"text-indent:2em\">'+esc(s.text).replace(/\\n+/g,'</p><p style=\"text-indent:2em\">')+'</p>'):''}"
for f in (r"D:\系统汉字\web\public\test.html", r"D:\系统汉字\web\public\index.html"):
    h=io.open(f,encoding="utf-8").read()
    if old in h:
        h=h.replace(old,new); io.open(f,"w",encoding="utf-8",newline="\n").write(h); print(f.split("\\")[-1],"indent patched")
    else: print(f.split("\\")[-1],"MISS indent")
n=0
for f in glob.glob(r"D:\系统汉字\web\public\cards\第*章*.json"):
    d=json.load(io.open(f,encoding="utf-8"))
    if not d.get("chapter"): continue
    for s in d["sections"]:
        if s.get("label")=="义类（声素与通假）": s["label"]="义类"
    json.dump(d,io.open(f,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("labels",n)
h=io.open(r"D:\系统汉字\web\public\test.html",encoding="utf-8").read()
js="\n;\n".join(re.findall(r"<script>(.*?)</script>",h,re.S))
p=os.path.join(tempfile.gettempdir(),"chk5.js"); io.open(p,"w",encoding="utf-8").write(js)
r=subprocess.run([r"C:\Users\萧磊\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\node\bin\node.exe","--check",p],capture_output=True,text=True)
print("rc",r.returncode,(r.stderr or "")[:150])