import json,glob,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for f in glob.glob(r"D:\系统汉字\web\public\cards\*.json"):
    try: d=json.load(io.open(f,encoding="utf-8"))
    except: continue
    if not isinstance(d,dict): continue
    if d.get("char") in ("似","佀"):
        print(f.split("\\")[-1], d.get("char"), d.get("trad"), d.get("simp"), d.get("level"), len(d.get("sections",[])))