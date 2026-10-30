import io,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for h,o in [(r"D:\系统汉字\web\public\test.html",r"D:\系统汉字\.tmp-t1.js"),(r"D:\系统汉字\web\public\index.html",r"D:\系统汉字\.tmp-t2.js")]:
    s=io.open(h,encoding="utf-8").read()
    js="\n".join(re.findall(r"<script>(.*?)</script>",s,re.S))
    io.open(o,"w",encoding="utf-8").write(js)
print("extracted")