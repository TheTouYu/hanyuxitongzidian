import subprocess,os,re,json
ROOT=r"D:\系统汉字"
ENV=dict(os.environ); ENV["PATH"]=ROOT+r"\.runtime\mingit\cmd;"+ENV["PATH"]
PY=ROOT+r"\.runtime\venv\Scripts\python.exe"; SH=ROOT+r"\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=ROOT,capture_output=True,env=ENV)
    return (r.stdout+b"\n"+r.stderr).decode("utf-8","replace")
md=open(ROOT+r"\knowledge\hanzi-yinyuan\02y-zika.md",encoding="utf-8").read()
i=md.find("### 槮·")
print(md[i:i+260])
print("validate:",json.loads(run("validate","--format","json")).get("errors"))
r=subprocess.run([ROOT+r"\tools\git.cmd","add","web/public/cards/槮.json","knowledge","data/knowledge"],cwd=ROOT,capture_output=True,env=ENV)
r=subprocess.run([ROOT+r"\tools\git.cmd","commit","-m","fix: 槮归594彡部参系（卡与条）"],cwd=ROOT,capture_output=True,env=ENV)
print((r.stdout+b"\n"+r.stderr).decode("utf-8","replace")[:300])