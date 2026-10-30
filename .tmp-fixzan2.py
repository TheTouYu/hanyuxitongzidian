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
pid="pln_3d9c4fb038fbe14872452ecbff"
cid="clm_4B0857314AF7EAF4B1868E0BCD"
st="槮（屬594彡部之參系，从木參聲）：木長皃（《說文》「木長皃」）；又 積柴水中取魚（罧）。"
bd="源自《系統漢語》第594部「彡部」·參系（卷九十七 殸）；字卡五步规程。"
print(run("knowledge-plan","revise-claim",pid,"--claim-id",cid,"--statement",st,"--boundary",bd,"--semantic-declaration","clarify","--reason","槮屬彡部參系")[-160:])
print(run("knowledge-plan","check",pid,"--mode","delta")[-160:])
print(run("knowledge-plan","finalize",pid)[-160:])
bnd=os.path.basename(sorted(glob.glob(ROOT+r"\data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
s=run("bundle-status",bnd,"--format","json")
h=re.search(r'"content_hash":\s*"([0-9a-f]{64})"',s)
print("bundle",bnd,"hash",bool(h))
if h:
    hh=h.group(1)
    print(run("bundle-approve",bnd,"--apply","--content-hash",hh)[-100:])
    print(run("bundle-apply",bnd,"--apply","--content-hash",hh)[-100:])
    run("rebuild"); print("err",json.loads(run("validate","--format","json")).get("errors"))
git("add","web/public/cards/槮.json","knowledge","data/knowledge"); print(git("commit","-m","fix: 槮归594彡部参系（卡与条）")[-90:])