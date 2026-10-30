import json,subprocess,os,time
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
d=json.load(open(r"intake\20261022-字卡383糸部.json",encoding="utf-8"))
d["intent"]="字卡383糸部首10字2026-10-22b"
json.dump(d,open(r"intake\20261022-字卡383糸部.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261022-字卡383糸部.json","--format","json")
print(out[-600:])