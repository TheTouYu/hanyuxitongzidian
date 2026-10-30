# -*- coding: utf-8 -*-
import json,io,os,subprocess,sys,time,glob
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
ENV["PYTHONUTF8"]="1"; ENV["PYTHONIOENCODING"]="utf-8"
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,env=ENV)
    return (r.stdout or b"").decode("utf-8","replace")+(r.stderr or b"").decode("utf-8","replace")
p=r"D:\系统汉字\intake\20261028-fj-summary.json"
d=json.load(io.open(p,encoding="utf-8"))
c0=d["claims"][0]
for k in ("topic_path","topic_title","topic_summary","topic_keywords"): c0.pop(k,None)
d["intent"]=f"繁简汇总{time.strftime('%Y%m%d-%H%M%S')}"
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",p,"--format","json")
j=json.loads(out) if out.strip().startswith("{") else {}
print("ok",j.get("ok"),"ops",(j.get("semantic_diff") or {}).get("operations"),str(j.get("errors"))[:200])
if j.get("ok"):
    bd=j["bundle_id"]; h=j["content_hash"]
    print(run("bundle-approve",bd,"--apply","--content-hash",h)[:80])
    print(run("bundle-apply",bd,"--apply","--content-hash",h)[:80])
    print(run("rebuild")[-120:]); print(run("validate","--format","json")[:140])