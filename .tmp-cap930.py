# -*- coding: utf-8 -*-
import json,io,os,re,subprocess,sys,time
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
ENV["PYTHONUTF8"]="1"; ENV["PYTHONIOENCODING"]="utf-8"
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,env=ENV)
    return (r.stdout or b"").decode("utf-8","replace")+(r.stderr or b"").decode("utf-8","replace")
d=json.load(io.open(r"D:\系统汉字\intake\20261028-fj-batch.json",encoding="utf-8"))
d["intent"]=f"繁简诊断{time.strftime('%H%M%S')}"
p=r"D:\系统汉字\intake\20261028-fj-batch.json"
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print(run("knowledge-plan","capture","--file",p,"--preview-only","--format","json")[:1600])