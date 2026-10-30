import json,subprocess,os,glob,time
d=json.load(open(r"intake\20261023-字卡403史部余.json",encoding="utf-8"))
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
def ingest(claims,tag):
    doc={"schema_version":1,"intent":f"字卡403史部余{tag}{int(time.time())}","risk":"low","claims":claims}
    p=rf"intake\_tmp_shi_{tag}.json"; json.dump(doc,open(p,"w",encoding="utf-8"),ensure_ascii=False)
    out=run("knowledge-plan","capture","--file",p,"--format","json")
    if "PLAN_DUPLICATE" in out: return False
    b=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",b,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",b,"--apply","--content-hash",h); run("bundle-apply",b,"--apply","--content-hash",h)
    return True
cs=d["claims"]
for tag,grp in (("A",cs[:4]),("B",cs[4:8]),("C",cs[8:])):
    print(tag,ingest(grp,tag))
run("rebuild"); v=json.loads(run("validate","--format","json")); print("err",v.get("errors"))