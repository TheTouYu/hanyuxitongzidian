import re,json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
md=open(r"knowledge\hanzi-yinyuan\02y-zika.md",encoding="utf-8").read()
blocks=re.findall(r"<!-- CLAIM:START (clm_[0-9A-F]+) -->\s*\n### (.+?)\n\n([\s\S]*?)\n\n#### 适用边界\n\n([\s\S]*?)\n\n<!-- CLAIM:END",md)
tgt=[(c,t,s,b) for c,t,s,b in blocks if "523部" in b and "卷八十六" in b]
print("targets",len(tgt))
plan=run("knowledge-plan","init","--intent","部号订正：㓝系归522刅部","--risk","low","--baseline","worktree")
pid=re.search(r"pln_[0-9a-f]+",plan).group(0)
nb="源自《系統漢語》第522部「刅部」（卷八十六 良，含㓝系）；字卡五步规程。"
ok=0
for cid,title,stmt,old in tgt:
    o=run("knowledge-plan","revise-claim",pid,"--claim-id",cid,"--statement",stmt,"--boundary",nb,"--semantic-declaration","clarify","--reason","㓝系属522刅部，非523")
    if '"ok": true' in o: ok+=1
print("revised",ok)
print(run("knowledge-plan","check",pid,"--mode","delta")[:120])
fin=run("knowledge-plan","finalize",pid); print("fin ok:", '"ok": true' in fin)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
print("bundle",bd)
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("err",v.get("errors"))
n=0
for f in glob.glob(r"web\public\cards\*.json"):
    d=json.load(open(f,encoding="utf-8")); bus=d.get("bus")
    if isinstance(bus,list) and bus and isinstance(bus[0],dict) and bus[0].get("num")==523 and bus[0].get("name")=="㓝":
        d["bus"]=[{"num":522,"name":"刅"}]
        json.dump(d,open(f,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("cards fixed",n)