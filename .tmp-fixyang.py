import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
YANG="養 癢 𧓲 懩 攁 瀁 𩜒 𥶑 㔦 䑆 鱶 䭥".split()
QIANG="羌 猐 𡬎 唴 𥇉 㳾 琷 𦏱 蜣 㛨 𥓌 𪁸".split()
YANG4="羕 𤡀 𩞭 㨾 樣 漾 𠍵 𡡂 𢟣 𧫛 𨖌".split()
# fix cards
for ch in YANG+QIANG:
    f=rf"web\public\cards\{ch}.json"
    d=json.load(open(f,encoding="utf-8"))
    for b in d["bus"]: b["num"],b["name"]=523,"羊"
    for s in d["sections"]:
        s["text"]=re.sub(r"【第52[45]部「(養|羌)部」[^】]*】","【第523部「羊部」·"+(("養" ) if ch in YANG else "羌")+"系】",s["text"])
    json.dump(d,open(f,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
md=""
for f in glob.glob(r"knowledge\**\*.md",recursive=True): md+=open(f,encoding="utf-8").read()
plans={}
for ch in YANG+QIANG:
    m=re.search(r"<!-- CLAIM:START (clm_[0-9A-F]+) -->\s*\n### "+re.escape(ch)+r"（字卡",md)
    if m: plans[ch]=m.group(1)
print("found",len(plans))
out=run("knowledge-plan","init","--intent","羊部族归属订正","--risk","low","--baseline","worktree")
pid=re.search(r"pln_[0-9a-f]+",out).group(0)
for ch,cid in plans.items():
    fam="養" if ch in YANG else "羌"
    b=f"源自《系統漢語》第523部「羊部」·{fam}系（卷八十七 羊）；字卡五步规程。"
    run("knowledge-plan","revise-claim",pid,"--claim-id",cid,"--boundary",b,"--semantic-declaration","clarify","--reason","養/羌為羊部內字族，非獨立部")
print("check:",run("knowledge-plan","check",pid,"--mode","delta")[:60])
out=run("knowledge-plan","finalize",pid,"--format","json"); print("fin",out[:40])
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"),"n",len(plans))