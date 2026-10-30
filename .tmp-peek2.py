import io,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
h=io.open(r"D:\系统汉字\web\public\test.html",encoding="utf-8").read()
for m in re.finditer(r"b\.num===0\?[\s\S]{0,420}",h):
    print("HEAD>>>",m.group(0)[:420].replace("\n"," ")); break
for m in re.finditer(r"x\.ch\?[\s\S]{0,300}",h):
    print("LIST>>>",m.group(0)[:300].replace("\n"," ")); break