import json,subprocess,os
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
r=subprocess.run([PY,SH,"knowledge-plan","capture","--file",r"intake\20261023-字卡531b.json","--format","json"],cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
print((r.stdout or r.stderr)[:1200])