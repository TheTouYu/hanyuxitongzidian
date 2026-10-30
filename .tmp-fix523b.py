import re,json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
md=open(r"knowledge\hanzi-yinyuan\02y-zika.md",encoding="utf-8").read()
blocks=re.findall(r"<!-- CLAIM:START (clm_[0-9A-F]+) -->\s*\n### (.+?)\n([\s\S]*?)<!-- CLAIM:END",md)
tgt=[(c,t) for c,t,b in blocks if "523部" in b]
print("claims to fix:",len(tgt))
if tgt:
    plan=run("knowledge-plan","init","--intent","部号订正：㓝系归522刅部","--risk","low","--baseline","worktree")
    m=re.search(r"pln_[0-9a-f]+",plan)
    print("init tail:",plan.strip().splitlines()[-1][:120])
    if m:
        pid=m.group(0); nb="源自《系統漢語》第522部「刅部」（卷八十六 良，含㓝系）；字卡五步规程。"
        ok=0
        for cid,title in tgt:
            out=run("knowledge-plan","revise-claim",pid,"--claim-id",cid,"--boundary",nb,"--semantic-declaration","clarify","--reason","523应为522刅部，㓝系属之")
            if "REV" in out: ok+=1
        print("revised",ok)
        print(run("knowledge-plan","check",pid,"--mode","delta")[:160])
        print(run("knowledge-plan","finalize",pid)[:260])
for f in glob.glob(r"web\public\cards\*.json"):
    d=json.load(open(f,encoding="utf-8"))
    if any(b.get("num")==523 for b in d.get("bus",[])):
        d["bus"]=[{"num":522,"name":"刅"}]
        json.dump(d,open(f,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("cards fixed")