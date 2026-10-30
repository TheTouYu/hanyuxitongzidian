import json,subprocess,os,re,glob
ROOT=r"D:\系统汉字"
ENV=dict(os.environ); ENV["PATH"]=ROOT+r"\.runtime\mingit\cmd;"+ENV["PATH"]
PY=ROOT+r"\.runtime\venv\Scripts\python.exe"; SH=ROOT+r"\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=ROOT,capture_output=True,env=ENV)
    return (r.stdout+b"\n"+r.stderr).decode("utf-8","replace")
def git(*a):
    r=subprocess.run([ROOT+r"\tools\git.cmd"]+list(a),cwd=ROOT,capture_output=True,env=ENV)
    return (r.stdout+b"\n"+r.stderr).decode("utf-8","replace")
cp=ROOT+r"\web\public\cards\槮.json"
c=json.load(open(cp,encoding="utf-8"))
for s in c["sections"]:
    if s["key"]=="bengen":
        s["text"]="【第594部「彡部」·參系】彡＝三丿，象細長而多之物；彡部之下立二級字根參：參＝三根算籌並列（三為其異體），本義相參、並列，引申眾多、細密；槮从木、以參為聲，故屬參系，非徑屬彡部。"
json.dump(c,open(cp,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
md=open(ROOT+r"\knowledge\hanzi-yinyuan\02y-zika.md",encoding="utf-8").read()
m=re.search(r"<!-- CLAIM:START (clm_[0-9A-F]+) -->\s*\n### 槮·shēn",md)
print("claim",m.group(1) if m else None)
if m:
    cid=m.group(1)
    st="槮（屬594彡部之參系，从木參聲）：木長皃（《說文》「木長皃」）；又 積柴水中取魚（罧）。"
    bd="源自《系統漢語》第594部「彡部」·參系（卷九十七 殸）；字卡五步规程。"
    p=run("knowledge-plan","init","--intent","槮归参系2026-10-24","--risk","low","--baseline","worktree")
    pid=re.search(r"pln_[0-9a-f]+",p)
    print("pid",pid.group(0) if pid else p[-200:])
    print(run("knowledge-plan","revise-claim","--plan-id",pid.group(0),"--claim-id",cid,"--statement",st,"--boundary",bd,"--semantic-declaration","clarify","--reason","槮属彡部参系，非径属彡部")[-200:])
    run("knowledge-plan","check","--plan-id",pid.group(0),"--mode","delta")
    print(run("knowledge-plan","finalize","--plan-id",pid.group(0))[-200:])
    bnd=os.path.basename(sorted(glob.glob(ROOT+r"\data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=re.search(r'"content_hash":\s*"([0-9a-f]{64})"',run("bundle-status",bnd,"--format","json")).group(1)
    print(run("bundle-approve",bnd,"--apply","--content-hash",h)[-80:]); print(run("bundle-apply",bnd,"--apply","--content-hash",h)[-80:])
    print(run("rebuild")[-40:]); print("err",json.loads(run("validate","--format","json")).get("errors"))
print(git("add","web/public/cards/槮.json","knowledge","data/knowledge")[-40:])
print(git("commit","-m","fix: 槮归594彡部参系（卡与条）")[-100:])