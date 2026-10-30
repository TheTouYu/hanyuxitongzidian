import json,io,sys,glob,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
ok=bad=0; samp=[]
for p in glob.glob(r"D:\系统汉字\web\public\cards\*.json"):
    if p.endswith("index.json"): continue
    d=json.load(io.open(p,encoding="utf-8"))
    for s in d.get("sections",[]):
        if s.get("key")=="shengmu" and (s.get("text") or "").strip():
            t=s["text"]
            if re.match(r"^[a-z]{1,2}「.+?」取「.+?」：",t) or t.startswith("零聲母") or t.startswith("零声母"): ok+=1
            else:
                bad+=1
                if len(samp)<6: samp.append((d.get("char"),t[:30]))
print("规范",ok,"不合",bad,samp)