import subprocess,os,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
o=run("knowledge-plan","init","--intent","羊部族归属订正b","--risk","low","--baseline","worktree")
pid=re.search(r"pln_[0-9a-f]+",o).group(0); print("pid",pid)
print(run("knowledge-plan","revise-claim",pid,"--claim-id","clm_D9F167EC3048BF3C6BD940E313","--boundary","源自《系統漢語》第176部「壬部」（卷卅一 尋，巠／坙系）；字卡五步规程。","--semantic-declaration","clarify","--reason","x")[:200])
print("CHECK",run("knowledge-plan","check",pid,"--mode","delta")[:200])
print("FIN",run("knowledge-plan","finalize",pid,"--format","json")[:600])