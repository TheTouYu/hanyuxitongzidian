import json,subprocess,os,sys
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return r.stdout
out=run("knowledge-plan","list","--format","json")
plans=json.loads(out)
if isinstance(plans,dict): plans=plans.get("plans",[])
openp=[p for p in plans if p.get("state")=="open"]
pid=openp[-1]["plan_id"]
print("plan",pid)
fin=json.loads(run("knowledge-plan","finalize",pid,"--format","json"))
print("fin keys",list(fin)[:8])
b=fin.get("bundle_id") or fin.get("finalized_bundle_id")
print("bundle",b)
st=json.loads(run("bundle-status",b,"--format","json"))
h=st["bundles"][0]["content_hash"]; print("hash",h)
print(run("bundle-approve",b,"--apply","--content-hash",h)[:200])
print(run("bundle-apply",b,"--apply","--content-hash",h)[:200])
print(run("pkc","x")[:0] if False else "")
print(run("rebuild")[:120])
v=json.loads(run("validate","--format","json")); print("errors",v.get("errors"))