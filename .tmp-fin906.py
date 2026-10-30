import subprocess,os,glob,json,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,env=ENV)
    return (r.stdout+b"\n"+r.stderr).decode("utf-8","replace")
print(run("knowledge-plan","finalize","--intent","字卡594a0-2026-10-24")[-300:] if False else "")
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
print("newest",bd)
s=run("bundle-status",bd,"--format","json")
h=re.search(r'"content_hash":\s*"([0-9a-f]{64})"',s)
print("hash",bool(h))
if h:
    hh=h.group(1)
    print(run("bundle-approve",bd,"--apply","--content-hash",hh).strip()[-120:])
    print(run("bundle-apply",bd,"--apply","--content-hash",hh).strip()[-120:])
print(run("rebuild").strip()[-80:])
v=json.loads(run("validate","--format","json")); print("err",v.get("errors"))