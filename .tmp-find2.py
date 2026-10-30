import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
t=io.open(r"D:\系统汉字\web\server.mjs",encoding="utf-8").read().split("\n")
print("\n".join("%d|%s"%(i+1,t[i]) for i in range(1436,1452)))
print("----968----")
print("\n".join("%d|%s"%(i+1,t[i]) for i in range(966,984)))