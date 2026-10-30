import io,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for f in ("web/public/test.html","web/public/app.html"):
    t=io.open(f,encoding="utf-8").read().split("\n")
    print("==",f)
    for i,l in enumerate(t):
        if ("indexOf(q" in l or ".includes(q" in l or "toLowerCase().includes" in l) and ("c" in l or "h" in l):
            print(i+1,"|",l.strip()[:170])