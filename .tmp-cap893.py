# -*- coding: utf-8 -*-
import json,io,os,glob,subprocess,sys,time
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
ENV["PYTHONUTF8"]="1"; ENV["PYTHONIOENCODING"]="utf-8"
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,env=ENV)
    return (r.stdout or b"").decode("utf-8","replace")+(r.stderr or b"").decode("utf-8","replace")
p=r"D:\系统汉字\intake\20261028-繁简对照-01.json"
d=json.load(io.open(p,encoding="utf-8")); d["intent"]=f"繁简对照第一批{time.strftime('%H%M%S')}"
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",p,"--format","json")
print(out[:300])
if '"ok": true' in out or '"ok":true' in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    print(run("bundle-approve",bd,"--apply","--content-hash",h,"--format","json")[:200])
    print(run("bundle-apply",bd,"--apply","--content-hash",h,"--format","json")[:200])
    print(run("rebuild")[-200:])
    print(run("validate","--format","json")[:200])