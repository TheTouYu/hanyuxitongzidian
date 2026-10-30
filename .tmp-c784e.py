import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
p=r"intake\20261024-字卡569b.json"
d=json.load(open(p,encoding="utf-8"))
for it in range(6):
    d["intent"]=f"字卡569b{it+3}-2026-10-24"
    json.dump(d,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p,"--format","json")
    if "PLAN_DUPLICATE" not in out:
        print("ok claims",len(d["claims"]),"titles",[c["title"] for c in d["claims"]])
        bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
        h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
        run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
        run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
        break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1))
    print("drop",d["claims"][idx]["title"])
    d["claims"].pop(idx)