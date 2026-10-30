import glob,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
n=sum(1 for f in glob.glob(r"D:\系统汉字\web\public\cards\*.json") if "取一面" in io.open(f,encoding="utf-8").read())
print("已回滚；仍含「取一面」",n)