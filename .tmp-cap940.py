# -*- coding: utf-8 -*-
import json,io,os,re,glob,subprocess,sys,time
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
ENV["PYTHONUTF8"]="1"; ENV["PYTHONIOENCODING"]="utf-8"
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,env=ENV)
    return (r.stdout or b"").decode("utf-8","replace")+(r.stderr or b"").decode("utf-8","replace")
raw=open(r"D:\字谱智能体\汉字简体繁体对照表大全资料.txt","rb").read().decode("gb18030")
pairs=[]; seen=set()
for s,f in re.findall(r"([\u3400-\u9fff])=([\u3400-\u9fff])",raw):
    if s in seen: continue
    seen.add(s); pairs.append((s,f))
N=90
chunks=[pairs[i:i+N] for i in range(0,len(pairs),N)]
claims=[]
for k,ch in enumerate(chunks,1):
    body="；".join(f"{s}={f}" for s,f in ch)
    claims.append({"id":f"fjc-{k:03d}","node":"hanzi-yinyuan","topic_id":"topic-fanjian-duizhao",
      "title":f"繁简对照（第{k}段·{ch[0][0]}起）",
      "statement":f"繁简对照第{k}段，共{len(ch)}组：{body}。",
      "boundary":"《汉字简体繁体对照表》分段记录；单字检索以字卡别名索引为准。",
      "permission":"public","fact_classes":["evidence_scope"],
      "duplicate_resolution":"create_distinct_with_boundary"})
claims[0].update({"topic_path":"knowledge/hanzi-yinyuan/03f-fanjian-duizhao.md","topic_title":"繁简对照",
  "topic_summary":"《汉字简体繁体对照表》2,762 组简繁对应（分段记录），供简繁互检与字卡别名。","topic_keywords":["繁简对照","简体","繁体"]})
p=r"D:\系统汉字\intake\20261028-fj-summary.json"
json.dump({"schema_version":1,"intent":f"繁简汇总{time.strftime('%Y%m%d-%H%M%S')}","risk":"low","claims":claims},
          io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("段数",len(chunks))
out=run("knowledge-plan","capture","--file",p,"--format","json")
j=json.loads(out) if out.strip().startswith("{") else {}
print("ok",j.get("ok"),"ops",(j.get("semantic_diff") or {}).get("operations"),"err",str(j.get("errors"))[:200])
if j.get("ok"):
    bd=j["bundle_id"]; h=j["content_hash"]
    print(run("bundle-approve",bd,"--apply","--content-hash",h)[:80])
    print(run("bundle-apply",bd,"--apply","--content-hash",h)[:80])
    print(run("rebuild")[-120:]); print(run("validate","--format","json")[:120])