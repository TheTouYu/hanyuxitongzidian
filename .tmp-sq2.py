import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
t=io.open("web/public/app.html",encoding="utf-8").read().split("\n")
for i,l in enumerate(t):
    if "filter(" in l and ("c:" in l or "x.c" in l or "it.c" in l or ".c" in l):
        print(i+1,"|",l.strip()[:170])