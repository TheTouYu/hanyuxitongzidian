import io,re,sys,os,tempfile,subprocess
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
f=r"D:\系统汉字\web\public\test.html"
h=io.open(f,encoding="utf-8").read()
css=".cim{height:1em;width:auto;vertical-align:-.12em}.chead .ch .cim{height:.95em;width:auto;vertical-align:-.1em}"
if ".cim{" not in h:
    h=h.replace("</style>", css+"\n</style>",1)
    io.open(f,"w",encoding="utf-8",newline="\n").write(h); print("css added")
else:
    print("existing cim css:", re.search(r"\.cim\{[^}]*\}",h).group(0))