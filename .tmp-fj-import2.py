# -*- coding: utf-8 -*-
import json,io,os,re,subprocess,sys,time
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
ENV["PYTHONUTF8"]="1"; ENV["PYTHONIOENCODING"]="utf-8"
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,env=ENV)
    return (r.stdout or b"").decode("utf-8","replace")+(r.stderr or b"").decode("utf-8","replace")
C=r"D:\系统汉字\web\public\cards"
have={}
for fn in os.listdir(C):
    if not fn.endswith(".json") or fn=="index.json": continue
    try: d=json.load(io.open(os.path.join(C,fn),encoding="utf-8"))
    except: continue
    for k in [d.get("char"),d.get("trad"),d.get("simp")]+list(d.get("aliases") or []):
        if k: have[k]=1
raw=open(r"D:\字谱智能体\汉字简体繁体对照表大全资料.txt","rb").read().decode("gb18030")
pairs=[]; seen=set()
for s,f in re.findall(r"([\u3400-\u9fff])=([\u3400-\u9fff])",raw):
    if s in seen: continue
    seen.add(s); pairs.append((s,f))
todo=[(s,f) for s,f in pairs if s not in have and f not in have]
state=r"D:\系统汉字\.tmp-fj-state.json"
done=json.load(io.open(state,encoding="utf-8")).get("done",0) if os.path.exists(state) else 0
log=r"D:\系统汉字\.tmp-fj-log.txt"
def L(m):
    open(log,"a",encoding="utf-8").write(time.strftime("%H:%M:%S ")+m+"\n"); print(m)
B=20
while done < len(todo):
    chunk=todo[done:done+B]; ok=False
    for attempt in range(3):
        claims=[{"id":f"fj-{i:04d}","node":"hanzi-yinyuan","topic_id":"topic-fanjian-duizhao",
          "title":f"{s}＝{f}（繁简对照·第{i}组）",
          "statement":f"第{i}组：简体「{s}」，繁体作「{f}」。",
          "boundary":"繁简对照表之一；仅用于简繁互检与字卡别名。","permission":"public",
          "fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"}
          for i,(s,f) in enumerate(chunk,done+1)]
        p=r"D:\系统汉字\intake\20261028-fj-batch.json"
        json.dump({"schema_version":1,"intent":f"繁简{time.strftime('%Y%m%d-%H%M%S')}-{attempt}","risk":"low","claims":claims},
                  io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
        out=run("knowledge-plan","capture","--file",p,"--format","json")
        try: j=json.loads(out)
        except: j={}
        if j.get("ok") and j.get("bundle_id"):
            bd=j["bundle_id"]
            h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
            run("bundle-approve",bd,"--apply","--content-hash",h)
            ap=run("bundle-apply",bd,"--apply","--content-hash",h)
            if '"applied": true' in ap or '"applied":true' in ap:
                ok=True; break
        L(f"retry{attempt} {json.dumps(j.get('errors',[]),ensure_ascii=False)[:200]}")
        time.sleep(3)
    if not ok:
        L(f"GIVEUP at {done}"); break
    done+=len(chunk); json.dump({"done":done},io.open(state,"w",encoding="utf-8"))
    L(f"batch ok {done}/{len(todo)} {chunk[0][0]}-{chunk[-1][0]}")
    if done % 100 == 0:
        run("rebuild"); run("validate","--format","json")
        subprocess.run([r"D:\系统汉字\tools\git.cmd","add","knowledge","data/knowledge","intake"],cwd=r"D:\系统汉字",capture_output=True,env=ENV)
        subprocess.run([r"D:\系统汉字\tools\git.cmd","commit","-m",f"knowledge: 繁简对照入库 {done}/{len(todo)}"],cwd=r"D:\系统汉字",capture_output=True,env=ENV)
        L("checkpoint "+str(done))
L("DONE "+str(done))