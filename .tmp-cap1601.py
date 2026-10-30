import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\tools\check-bu.py"
t=io.open(p,encoding="utf-8").read()
old='    if d.get("parent") != parent:'
new='    if d.get("parent") != parent and parent not in (d.get("parents") or []):'
assert old in t
io.open(p,"w",encoding="utf-8",newline="\n").write(t.replace(old,new,1))
print("patched")