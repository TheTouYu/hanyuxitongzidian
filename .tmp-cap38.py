# -*- coding: utf-8 -*-
import json,io,os,re,sys,subprocess,tempfile
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
# 主卡加 head 与 aliases
spec={"灔":("灔（灩滟𤅿淡淊）",["灩","滟","𤅿","淡","淊"]),
      "艷":("艷（豔豓𡤩艳）",["豔","豓","𡤩","艳"])}
for main,(head,al) in spec.items():
    p=rf"{C}\{main}.json"; d=json.load(io.open(p,encoding="utf-8"))
    d["head"]=head; d["aliases"]=al
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
for ch in ["灩","滟","𤅿","淡","淊","豔","豓","𡤩","艳"]:
    p=rf"{C}\{ch}.json"
    if os.path.exists(p): os.remove(p)
f=r"D:\系统汉字\web\public\test.html"; h=io.open(f,encoding="utf-8").read()
if "d.head||" not in h:
    h=h.replace("esc(d.cname||ch)","esc(d.head||d.cname||ch)")
    io.open(f,"w",encoding="utf-8",newline="\n").write(h); print("head render patched")
js="\n;\n".join(re.findall(r"<script>(.*?)</script>",h,re.S))
t=os.path.join(tempfile.gettempdir(),"chk16.js"); io.open(t,"w",encoding="utf-8").write(js)
r=subprocess.run([r"C:\Users\萧磊\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\node\bin\node.exe","--check",t],capture_output=True,text=True)
print("rc",r.returncode)