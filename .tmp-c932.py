import sys,glob,os,json,subprocess
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
ROOT=r"D:\系统汉字"
ENV=dict(os.environ); ENV["PATH"]=ROOT+r"\.runtime\mingit\cmd;"+ENV["PATH"]
n=0
for fp in glob.glob(ROOT+r"\web\public\cards\*部.json"):
    ch=os.path.basename(fp)[:-5]
    real=ch[:-1]
    if len(real)!=1: continue
    d=json.load(open(fp,encoding="utf-8")); d["char"]=real
    out=rf"{ROOT}\web\public\cards\{real}.json"
    if os.path.exists(out): os.remove(fp)
    else: json.dump(d,open(out,"w",encoding="utf-8"),ensure_ascii=False,indent=1); os.remove(fp)
    n+=1
print("renamed",n)
subprocess.run([ROOT+r"\tools\git.cmd","add","-A","web/public/cards"],cwd=ROOT,capture_output=True,env=ENV)
r=subprocess.run([ROOT+r"\tools\git.cmd","commit","-m","cards: 修正部首卡名(去部字)"],cwd=ROOT,capture_output=True,env=ENV)
print((r.stdout+r.stderr).decode("utf-8","replace")[:120])