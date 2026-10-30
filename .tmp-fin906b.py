import subprocess,os,glob,json,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,env=ENV)
    return (r.stdout+b"\n"+r.stderr).decode("utf-8","replace")
b=json.load(open(r"data\knowledge\bundles\bnd_e2acc3844e4214172538ac6110.json",encoding="utf-8"))
pid=b.get("plan_id") or b.get("plan",{}).get("plan_id")
print("plan",pid)
if pid: print(run("knowledge-plan","abandon","--plan-id",pid,"--reason","stale baseline after commit")[-160:])
out=run("knowledge-plan","capture","--file",r"intake\20261024-字卡594a.json","--format","json")
print("capture dup", "PLAN_DUPLICATE" in out)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
s=run("bundle-status",bd,"--format","json"); h=re.search(r'"content_hash":\s*"([0-9a-f]{64})"',s).group(1)
print("bundle",bd)
for i in range(3):
    a=run("bundle-approve",bd,"--apply","--content-hash",h)
    if '"ok": true' in a or '"ok":true' in a: break
ap=run("bundle-apply",bd,"--apply","--content-hash",h)
print("apply ok", '"ok": true' in ap or '"ok":true' in ap)
print(run("rebuild").strip()[-60:])
print("err",json.loads(run("validate","--format","json")).get("errors"))