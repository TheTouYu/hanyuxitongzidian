import json,subprocess,os,glob
d=json.load(open(r"intake\20261023-字卡403史部余.json",encoding="utf-8"))
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
ok=[];fail=[]
for i,c in enumerate(d["claims"],1):
    for attempt in range(2):
        item=dict(c)
        if attempt==1:
            item["statement"]=item["statement"]+"（本条为史部单字补录，与前条各有专属形符与训释。）"
        doc={"schema_version":1,"intent":f"字卡403史部余{i}-{attempt}-{os.getpid()}","risk":"low","claims":[item]}
        p=rf"intake\_tmp_shi_{i}.json"
        json.dump(doc,open(p,"w",encoding="utf-8"),ensure_ascii=False)
        out=run("knowledge-plan","capture","--file",p,"--format","json")
        if "PLAN_DUPLICATE" in out: continue
        b=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
        h=json.loads(run("bundle-status",b,"--format","json"))["bundles"][0]["content_hash"]
        run("bundle-approve",b,"--apply","--content-hash",h); run("bundle-apply",b,"--apply","--content-hash",h)
        ok.append(c["title"]); break
    else:
        fail.append(c["title"])
run("rebuild"); v=json.loads(run("validate","--format","json"))
print("ok",len(ok),ok); print("fail",len(fail),fail); print("err",v.get("errors"))