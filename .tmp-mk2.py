import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
s=io.open(r"D:\系统汉字\.tmp-run2.mjs",encoding="utf-8").read()
s=s.replace('globalThis.window={};','globalThis.window={addEventListener(){}};')
s=s.replace('globalThis.document={','globalThis.document={body:{appendChild(){}},')
io.open(r"D:\系统汉字\.tmp-run3.mjs","w",encoding="utf-8",newline="\n").write(s)
print("ok")