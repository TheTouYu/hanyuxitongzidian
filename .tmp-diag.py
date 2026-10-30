import re,json,subprocess,os
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
print(json.dumps(json.load(open(r"web\public\cards\刑.json",encoding="utf-8"))["bus"],ensure_ascii=False))
print(json.dumps(json.load(open(r"web\public\cards\羊.json",encoding="utf-8"))["bus"],ensure_ascii=False))
plan=run("knowledge-plan","init","--intent","部号订正test","--risk","low","--baseline","worktree")
pid=re.search(r"pln_[0-9a-f]+",plan).group(0); print("pid",pid)
out=run("knowledge-plan","revise-claim",pid,"--claim-id","clm_D7049F77A6E6BF4B77F8E5F60E","--boundary","測試邊界","--semantic-declaration","clarify","--reason","測試")
print(out[:400])
print(run("knowledge-plan","abandon",pid)[:150])