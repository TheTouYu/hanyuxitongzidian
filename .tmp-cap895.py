# -*- coding: utf-8 -*-
import json,io,os,subprocess,sys,time
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
ENV["PYTHONUTF8"]="1"; ENV["PYTHONIOENCODING"]="utf-8"
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,env=ENV)
    return (r.stdout or b"").decode("utf-8","replace")+(r.stderr or b"").decode("utf-8","replace")
p=r"D:\系统汉字\intake\20261028-繁简对照-01.json"
d=json.load(io.open(p,encoding="utf-8"))
d["intent"]=f"繁简对照预检{time.strftime('%H%M%S')}"
# 首条补 topic 元数据
c0=d["claims"][0]
c0.update({"topic_path":"knowledge/hanzi-yinyuan/03f-fanjian-duizhao.md","topic_title":"繁简对照",
 "topic_summary":"《汉字简体繁体对照表》3,145 组简繁对应，供字卡别名与简繁互检。","topic_keywords":["繁简对照","简体","繁体","别名"]})
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",p,"--preview-only","--format","json")
print(out[:1500])