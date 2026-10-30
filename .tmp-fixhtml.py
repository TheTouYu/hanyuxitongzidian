import subprocess,sys,os
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
os.chdir(r"D:\系统汉字")
b=subprocess.run([r"tools\git.cmd","show","4a31ff098:web/public/test.html"],capture_output=True).stdout
open(r"web\public\test.html","wb").write(b)
print("bytes",len(b),"head",b[:30])