import subprocess,os,re,glob,json
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","init","--intent","慍部属订正2026-10-23","--risk","low","--baseline","worktree")
pid=re.search(r"pln_[0-9a-f]+",out).group(0); print("plan",pid)
r=run("knowledge-plan","revise-claim",pid,"--claim-id","clm_A9A17716106ED7AB0E6DC609F5",
 "--statement","慍（yùn）从心𥁕聲：怒也、怨恨（《說文》「怒也。从心𥁕聲」）；𥁕（昷）＝从囚从皿，婴儿浴盆温水，温之初文。",
 "--boundary","源自《系統漢語》第282部「囗部」之𥁕（昷）支（卷五十 豕）；字卡五步规程。",
 "--semantic-declaration","clarify","--reason","慍属𥁕支，非心部")
print("rev:", '"ok": true' in r)
fin=run("knowledge-plan","finalize",pid,"--format","json"); print("fin:", '"ok": true' in fin)
cands=[f for f in glob.glob(r"data\knowledge\bundles\bnd_*.json")]
cands.sort(key=os.path.getmtime,reverse=True)
bd=None
for f in cands[:5]:
    try:
        d=json.load(open(f,encoding="utf-8"))
        if "bundles" in d: bd=os.path.basename(f)[:-5]; break
    except: pass
print("bundle",bd)
if bd:
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("err",v.get("errors"))