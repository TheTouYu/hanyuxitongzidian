import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\test.html"; t=io.open(p,encoding="utf-8").read()
if 'http-equiv="Cache-Control"' not in t:
    t=t.replace("<meta charset=\"utf-8\">","<meta charset=\"utf-8\">\n<meta http-equiv=\"Cache-Control\" content=\"no-store, no-cache, must-revalidate\">\n<meta http-equiv=\"Pragma\" content=\"no-cache\">",1)
    io.open(p,"w",encoding="utf-8").write(t)
print("meta ok")