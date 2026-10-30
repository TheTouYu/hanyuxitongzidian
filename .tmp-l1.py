import subprocess, os, json
env=dict(os.environ); env["PYTHONUTF8"]="1"
env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
def pkc(*a):
    r=subprocess.run([r"D:\系统汉字\.runtime\venv\Scripts\python.exe", r"D:\系统汉字\tools\pkc_tmpfix.py", *a], capture_output=True, text=True, encoding="utf-8", cwd=r"D:\系统汉字", env=env)
    return r.stdout
for q in ("羅","罗"):
    j=json.loads(pkc("knowledge-search",q,"--limit","8","--format","json"))
    print("== 搜",q)
    for r in j.get("results",[]):
        print("  ",r["claim_id"], r["title"][:64])