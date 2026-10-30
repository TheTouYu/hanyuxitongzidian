import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for f in [r"D:\系统汉字\web\public\test.html", r"D:\系统汉字\web\public\index.html"]:
    h=io.open(f,encoding="utf-8").read()
    if "goCard(" in h: print("skip",f); continue
    h=h.replace('onclick=\\"open(\'','onclick=\\"goCard(\'')
    # 若上面未命中（不同转义），再试普通替换
    h=h.replace("onclick=\\\"open('", "onclick=\\\"goCard('")
    h=h.replace('onclick="open(\'','onclick="goCard(\'')
    if "window.goCard=open" not in h:
        h=h.replace("async function tryDirect(", "try{window.goCard=open;}catch(e){}\n  async function tryDirect(",1)
    io.open(f,"w",encoding="utf-8",newline="\n").write(h)
    print("patched",f, "goCard=",h.count("goCard("))