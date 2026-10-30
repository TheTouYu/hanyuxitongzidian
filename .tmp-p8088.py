import io
files=[r"web\server.mjs",r"web\start.cmd",r"web\README.md",r"prompts\web-kb.prompt.md",r"HANDOVER.md"]
for f in files:
    t=io.open(f,encoding="utf-8").read()
    n=t.replace("127.0.0.1:8080","127.0.0.1:8088").replace("process.env.PORT || 8080","process.env.PORT || 8088").replace("| `PORT` | `8080` |","| `PORT` | `8088` |")
    if n!=t:
        io.open(f,"w",encoding="utf-8",newline="\n").write(n); print("patched",f)
    else: print("same",f)