import sys,json,glob,subprocess,os
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
ROOT=r"D:\系统汉字"
n=0
for fp in glob.glob(ROOT+r"\web\public\cards\*.json"):
    d=json.load(open(fp,encoding="utf-8"))
    for s in d["sections"]:
        if s["key"]=="shengmu" and s["text"].startswith("聲母義：零聲母——"):
            s["text"]="聲母義：本部未列於緒論 119 部聲母義表（02z）；按該字聲母取擬態義一面，此欄待補。"
            n+=1
            break
    json.dump(d,open(fp,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("回退",n)
ENV=dict(os.environ); ENV["PATH"]=ROOT+r"\.runtime\mingit\cmd;"+ENV["PATH"]
subprocess.run([ROOT+r"\tools\git.cmd","add","web/public/cards"],cwd=ROOT,capture_output=True,env=ENV)
r=subprocess.run([ROOT+r"\tools\git.cmd","commit","-m","cards: 撤回误标零声母，改回待补"],cwd=ROOT,capture_output=True,env=ENV)
print((r.stdout+r.stderr).decode("utf-8","replace")[:80])