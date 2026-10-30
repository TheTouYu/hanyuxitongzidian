import subprocess,os,re,glob,json
ROOT=r"D:\系统汉字"
ENV=dict(os.environ); ENV["PATH"]=ROOT+r"\.runtime\mingit\cmd;"+ENV["PATH"]
PY=ROOT+r"\.runtime\venv\Scripts\python.exe"; SH=ROOT+r"\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=ROOT,capture_output=True,env=ENV)
    return (r.stdout+b"\n"+r.stderr).decode("utf-8","replace")
p=run("knowledge-plan","init","--intent","槮旧条归参系2026-10-24","--risk","low","--baseline","worktree")
pid=re.search(r"pln_[0-9a-f]+",p).group(0)
cid="clm_6207C86F97F95B936DBD18F2D9"
st="槮（594彡部·參系，从木參聲）：積柴水中以取魚（罧），《爾雅》「槮謂之涔」；又 木長皃。"
bd="源自《系統漢語》第594部「彡部」·參系（卷九十七 殸）；字卡五步规程。"
print(run("knowledge-plan","revise-claim",pid,"--claim-id",cid,"--statement",st,"--boundary",bd,"--semantic-declaration","clarify","--reason","槮屬彡部參系，舊條誤歸林部")[-120:])
run("knowledge-plan","check",pid,"--mode","delta")
print(run("knowledge-plan","finalize",pid)[-120:])
bnd=os.path.basename(sorted(glob.glob(ROOT+r"\data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=re.search(r'"content_hash":\s*"([0-9a-f]{64})"',run("bundle-status",bnd,"--format","json")).group(1)
run("bundle-approve",bnd,"--apply","--content-hash",h); run("bundle-apply",bnd,"--apply","--content-hash",h)
run("rebuild"); print("err",json.loads(run("validate","--format","json")).get("errors"))
r=subprocess.run([ROOT+r"\tools\git.cmd","add","knowledge","data/knowledge","web/public/cards/槮.json"],cwd=ROOT,capture_output=True,env=ENV)
r=subprocess.run([ROOT+r"\tools\git.cmd","commit","-m","fix: 槮旧条改归594彡部参系"],cwd=ROOT,capture_output=True,env=ENV)
print((r.stdout).decode("utf-8","replace")[:120])