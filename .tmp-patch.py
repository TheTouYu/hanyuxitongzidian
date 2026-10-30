import io
p=r"D:\系统汉字\tools\build-claims-index.py"
s=io.open(p,encoding="utf-8").read()
s=s.replace('        head = title.split("：", 1)[-1]','        head = title + body')
io.open(p,"w",encoding="utf-8",newline="\n").write(s)
print("patched2")