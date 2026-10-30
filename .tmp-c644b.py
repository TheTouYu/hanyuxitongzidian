import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
CH="養 癢 𧓲 懩 攁 瀁 𩜒 𥶑 㔦 䑆 鱶 䭥".split()
txt=""
for f in glob.glob(r"knowledge\**\*.md",recursive=True):
    txt+=open(f,encoding="utf-8").read()
have=[c for c in CH if f"### {c}" in txt]
miss=[c for c in CH if c not in have]
print("have",have); print("miss",miss)
d=json.load(open(r"intake\20261023-字卡524a.json",encoding="utf-8"))
d["claims"]=[c for c in d["claims"] if any(c["title"].startswith(m) for m in miss)]
d["intent"]="字卡524a2-2026-10-23"
if d["claims"]:
    json.dump(d,open(r"intake\20261023-字卡524a2.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡524a2.json","--format","json")
    print("dup2:", "PLAN_DUPLICATE" in out)
    if "PLAN_DUPLICATE" not in out:
        bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
        h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
        run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
        run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"),"n",len(d["claims"]))
else: print("no missing claims")