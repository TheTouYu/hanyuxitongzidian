import json,subprocess,os,glob,re
p=r"web\public\cards\簁.json"
c=json.load(open(p,encoding="utf-8"))
for s in c["sections"]:
    if s["key"]=="hengxiang":
        s["text"]="迁徙族①之竹：以「竹」定其器，筛使粗细相徙。筛中颗粒随筛面移动、成群相逐，正是「徙」（成群迁移）的一面——簁之取义不在「去粗」，而在**筛中之物随之迁动**。"
    if s["key"]=="xingpang":
        s["text"]="从竹徙声，《说文》「簁箄，竹器也」——竹筛；《集韵》「可以取粗去細」。声旁「徙」给的是筛中颗粒成群迁动之状，形旁「竹」定其为竹编之器。"
json.dump(c,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("card patched")
# 找 claim
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
st=run("show-claim","--title","簁（字卡）","--format","json")
m=re.search(r'"claim_id"\s*:\s*"(clm_[0-9A-F]+)"',st)
print("claim:", m.group(1) if m else st[:80])