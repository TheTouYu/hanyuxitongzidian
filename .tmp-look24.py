import sys,re,glob
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
files=glob.glob(r"D:\系统汉字\knowledge\hanzi-yinyuan\*.md")
want=["松","蜡","姜","雲","發","鬥","榖","乾","後","裏","臺"]
for ch in want:
    best=None
    for f in files:
        t=open(f,encoding="utf-8").read()
        for m in re.finditer(r"### ([^\n]*"+ch+r"[^\n]*)\n\n([^\n]{0,120})",t):
            title=m.group(1); body=m.group(2)
            if ("部" in title) or ("从" in body):
                best=(title,body); break
        if best: break
    print(ch,"|",(best[0][:40]+" ‖ "+best[1][:70]) if best else "未命中")