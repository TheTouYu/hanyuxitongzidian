import json,subprocess,os,glob,re
cid=None; body=None
for f in glob.glob(r"knowledge\**\*.md",recursive=True):
    t=open(f,encoding="utf-8").read()
    for m in re.finditer(r"<!-- CLAIM:START (clm_[0-9A-F]+) -->\s*\n### 簁（字卡）\n(.*?)#### 适用边界\n(.*?)<!-- CLAIM:END", t, re.S):
        cid=m.group(1); body=m.group(2).strip(); bound=m.group(3).strip()
if not cid: print("claim not found"); raise SystemExit
print("cid",cid)
new="簁（shāi）：《说文》「簁箄，竹器也，从竹徙聲」——竹筛；《集韵》「可以取粗去細」。声旁「徙」取「成群迁移」一面：筛中颗粒随筛面移动、成群相逐，故曰徙；形旁「竹」定其为竹编之器。"
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","init","--intent","簁取义修正2026-10-23","--risk","medium","--baseline","worktree")
pid=re.search(r"(pln_[0-9a-f]+)",out)
print("plan",pid.group(1) if pid else out[:120])
if not pid: raise SystemExit
pid=pid.group(1)
r=run("knowledge-plan","revise-claim",pid,"--claim-id",cid,"--statement",new,"--boundary",bound,
      "--semantic-declaration","clarify","--reason","簁取义修正：筛中颗粒成群迁动","--format","json")
print("rev",("ok" in r) or r[:120])
tmp=r"D:\系统汉字\.tmp-shai.json"
open(tmp,"w",encoding="utf-8").write(new)
run("knowledge-plan","check",pid,"--mode","delta")
f=run("knowledge-plan","finalize",pid,"--format","json")
b=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",b,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",b,"--apply","--content-hash",h); run("bundle-apply",b,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",b,"err",v.get("errors"))