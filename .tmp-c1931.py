import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\tools\check-bu.py"
t=io.open(p,encoding="utf-8").read()
if "PREFIX" not in t:
    t=t.replace("SM = re.compile", "PREFIX = re.compile(r'^(本義|本义|轉義|转义|辯證|辩证|音源)[：:]')\nSM = re.compile",1)
    # 在检查声母处之前加前缀检查
    t=t.replace("        if not sm:", "        for s0 in (c.get('sections') or []):\n            if PREFIX.match((s0.get('text') or '').strip()):\n                err.append(f\"{ch}: 栏内重复前缀 → {s0.get('text')[:20]}\")\n        if not sm:",1)
    io.open(p,"w",encoding="utf-8",newline="\n").write(t); print("checker patched")