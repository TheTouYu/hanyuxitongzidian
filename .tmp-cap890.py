# -*- coding: utf-8 -*-
import json,io,os,re,subprocess,sys,time,glob
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
raw=open(r"D:\字谱智能体\汉字简体繁体对照表大全资料.txt","rb").read().decode("gb18030")
pairs=[]
seen=set()
for s,f in re.findall(r"([\u3400-\u9fff])=([\u3400-\u9fff])",raw):
    if s in seen: continue
    seen.add(s); pairs.append((s,f))
pairs.sort()
N=400
batch=pairs[:N]
claims=[]
for i,(s,f) in enumerate(batch,1):
    claims.append({"id":f"fj-{i:04d}","node":"hanzi-yinyuan","topic_id":"topic-fanjian-duizhao",
      "title":f"{s}＝{f}（繁简对照·第{i}组）",
      "statement":f"第{i}组：简体「{s}」，繁体作「{f}」。",
      "boundary":"繁简对照表（3,145 组）之一；用于简繁互检与字卡别名。",
      "permission":"public","fact_classes":["evidence_scope"],
      "duplicate_resolution":"create_distinct_with_boundary"})
draft={"schema_version":1,"intent":f"繁简对照表入库{time.strftime('%Y-%m-%d %H:%M:%S')}","risk":"low","claims":claims}
p0=r"D:\系统汉字\intake\20261028-繁简对照-01.json"
json.dump(draft,io.open(p0,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",p0,"--format","json")
print("dup:", "PLAN_DUPLICATE" in out, "err:", "ERROR" in out[:400])
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json"))
    print("bundle",bd,"errors",v.get("errors"))