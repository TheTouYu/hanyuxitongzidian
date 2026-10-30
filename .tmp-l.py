import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
L=io.open(r"D:\系统汉字\web\public\test.html",encoding="utf-8").read().split("\n")
for i in range(92,116): print(i+1, L[i])