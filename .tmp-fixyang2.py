import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
YANG="養 癢 𧓲 懩 攁 瀁 𩜒 𥶑 㔦 䑆 鱶 䭥".split()
QIANG="羌 猐 𡬎 唴 𥇉 㳾 琷 𦏱 蜣 㛨 𥓌 𪁸".split()
md=""
for f in glob.glob(r"knowledge\**\*.md",recursive=True): md+=open(f,encoding="utf-8").read()
blocks=dict((m.group(2),m.group(1)) for m in re.finditer(r"<!-- CLAIM:START (clm_[0-9A-F]+) -->\s*\n### (.+?)\n\n([\s\S]*?)\n\n#### 适用边界",md))
info={}
for ch in YANG+QIANG:
    key=[k for k in blocks if k.startswith(ch+"（字卡")]
    if not key: continue
    k=key[0]; cid=blocks[k]
    m=re.search(r"<!-- CLAIM:START "+cid+r" -->\s*\n### "+re.escape(k)+r"\n\n([\s\S]*?)\n\n#### 适用边界",md)
    info[ch]=(cid,m.group(1).strip())
print("found",len(info))
o=run("knowledge-plan","init","--intent","羊部族归属订正c","--risk","low","--baseline","worktree")
pid=re.search(r"pln_[0-9a-f]+",o).group(0)
for ch,(cid,stmt) in info.items():
    fam="養" if ch in YANG else "羌"
    b=f"源自《系統漢語》第523部「羊部」·{fam}系（卷八十七 羊）；字卡五步规程。"
    r=run("knowledge-plan","revise-claim",pid,"--claim-id",cid,"--statement",stmt,"--boundary",b,"--semantic-declaration","clarify","--reason","養/羌為羊部內字族，非獨立部")
    if not '"ok": true' in r: print("REVFAIL",ch,r[:150])
print("CHECK",run("knowledge-plan","check",pid,"--mode","delta")[:60])
print("FIN",run("knowledge-plan","finalize",pid,"--format","json")[:100])
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
r=run("bundle-status",bd,"--format","json")
try:
    h=json.loads(r)["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
except Exception as e: print("bundle err",bd,str(e)[:80],r[:120])