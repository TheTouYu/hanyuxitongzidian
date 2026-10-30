import json,subprocess,os,glob
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
files=sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)
b=os.path.basename(files[-1])[:-5]
print("bundle",b)
st=json.loads(run("bundle-status",b,"--format","json"))
h=st["bundles"][0]["content_hash"]; print("hash",h[:16])
print(run("bundle-approve",b,"--apply","--content-hash",h)[:120])
print(run("bundle-apply",b,"--apply","--content-hash",h)[:120])
print(run("rebuild")[:100])
v=json.loads(run("validate","--format","json")); print("errors",v.get("errors"))