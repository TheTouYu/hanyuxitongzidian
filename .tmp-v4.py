import io,re,sys,subprocess,os
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
h=io.open(r"D:\系统汉字\web\public\test.html",encoding="utf-8").read()
blocks=re.findall(r"<script[^>]*>(.*?)</script>", h, re.S)
print("blocks",len(blocks))
node=r"C:\Users\萧磊\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\node\bin\node.exe"
for i,b in enumerate(blocks):
    p=rf"D:\系统汉字\.tmp-b{i}.js"; io.open(p,"w",encoding="utf-8").write(b)
    r=subprocess.run([node,"--check",p],capture_output=True,text=True)
    print(i,"rc",r.returncode, (r.stderr or "")[:80].replace("\n"," "))