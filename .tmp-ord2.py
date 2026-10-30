import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
old="const SEC_ORDER=['benyi','benyi2','zhuanyi','bianzheng','yinyuan','shengmu','zizu','zigen'];"
new="const SEC_ORDER=['benyi','benyi2','zhuanyi','bianzheng','yinyuan','shiyi','shengmu','zizu','zigen'];"
for h in [r"D:\系统汉字\web\public\test.html", r"D:\系统汉字\web\public\index.html"]:
    s=io.open(h,encoding="utf-8").read()
    assert old in s, h
    io.open(h,"w",encoding="utf-8",newline="\n").write(s.replace(old,new,1))
print("order fixed: 释义→声母拟态")