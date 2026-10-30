import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
# card
f=r"web\public\cards\娙.json"
d=json.load(open(f,encoding="utf-8"))
d["bus"]=[{"num":176,"name":"壬"}]
B="【第176部「壬部」·巠（坙）系】坙＝从巛从壬，象經線繃直、織機上縱線；《說文》「水脈」之析不確。字族取「縱直、修長、經行」一面；娙為「𡜇」之或体（㓝族一見），本屬此部。"
for s in d["sections"]:
    if s["key"]=="bengen": s["text"]=B
    if s["key"]=="xingpang":
        s["text"]="从女坙聲（《說文》五莖切）：「長好也」，身長好貌（《玉篇》）；身材苗條，又婢（《廣雅》）。"
    if s["key"]=="hengxiang":
        s["text"]="坙（巠）系諧聲字同取「縱直、經行」一面：經／莖／徑／頸／脛／涇／陘／鋞／牼／痙／輕等，形符各定落點；娙以女定「身長好」之落點。只列本部字。"
d["sections"].insert(0,{"key":"liushu","label":"六书","text":"六书：形声（亦作「𡜇」之或体，从女、坙声）。","cites":[]})
json.dump(d,open(f,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
# claim
CID="clm_D9F167EC3048BF3C6BD940E313"
stmt="娙（xíng）从女坙聲：「長好也」，身長好貌（《說文》五莖切、《玉篇》）；又婢（《廣雅》）。《集韻》「或从刑」者為或体，非本部。"
bnd="源自《系統漢語》第176部「壬部」（卷卅一 尋，巠／坙系）；字卡五步规程。"
out=run("knowledge-plan","init","--intent","娙归属订正","--risk","low","--baseline","worktree")
pid=re.search(r"pln_[0-9a-f]+",out).group(0)
out=run("knowledge-plan","revise-claim",pid,"--claim-id",CID,"--statement",stmt,"--boundary",bnd,"--semantic-declaration","clarify","--reason","娙本属坙（巠）系，前误归㓝族")
print("rev:",out[:120])
print("check:",run("knowledge-plan","check",pid,"--mode","delta")[:80])
out=run("knowledge-plan","finalize",pid,"--format","json")
print("fin:",out[:80])
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))