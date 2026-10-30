import json,subprocess,os,glob,re
fix=json.load(open(r".tmp-fixbd.json",encoding="utf-8"))
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
o=run("knowledge-plan","init","--intent","重挂部号fix-2026-10-23","--risk","low","--baseline","worktree","--format","json")
pid=re.search(r"pln_[0-9a-f]+",o).group(0)
ok=0
for f in fix:
    r=run("knowledge-plan","revise-claim",pid,"--claim-id",f["id"],"--statement",f["statement"],"--boundary",f["boundary"],"--semantic-declaration","clarify","--reason","訂正部號：原標部名與原稿目錄不符","--format","json")
    if "clm_" in r: ok+=1
print("revised",ok,"/",len(fix))
run("knowledge-plan","check",pid,"--mode","delta","--format","json")
run("knowledge-plan","finalize",pid,"--format","json")
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))