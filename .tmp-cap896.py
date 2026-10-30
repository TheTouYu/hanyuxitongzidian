# -*- coding: utf-8 -*-
import json,io,os,subprocess,sys,time
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
ENV["PYTHONUTF8"]="1"; ENV["PYTHONIOENCODING"]="utf-8"
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,env=ENV)
    return (r.stdout or b"").decode("utf-8","replace")+(r.stderr or b"").decode("utf-8","replace")
p=r"D:\系统汉字\intake\20261028-繁简对照-01.json"
d=json.load(io.open(p,encoding="utf-8"))
small={"schema_version":1,"intent":f"繁简预检小批{time.strftime('%H%M%S')}","risk":"low","claims":d["claims"][:20]}
p2=r"D:\系统汉字\intake\20261028-繁简对照-t20.json"
json.dump(small,io.open(p2,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
t=time.time(); out=run("knowledge-plan","capture","--file",p2,"--preview-only","--format","json")
print(round(time.time()-t),"s"); print(out[:1200])