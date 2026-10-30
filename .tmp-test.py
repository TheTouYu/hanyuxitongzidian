# -*- coding: utf-8 -*-
import json,urllib.request,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
B="http://127.0.0.1:8088/"
def get(p):
    with urllib.request.urlopen(B+p,timeout=10) as r: return r.status,r.read().decode("utf-8")
ok=[]
try:
    s,t=get("api/health"); h=json.loads(t)
    ok.append(("health",s,f"claims={h.get('claims')} mode={h.get('mode')}"))
except Exception as e: ok.append(("health","ERR",str(e)[:60]))
for ch in ["㠯","士","示","奚","台"]:
    try:
        s,t=get("cards/"+urllib.parse.quote(ch)+".json"); d=json.loads(t)
        labs=[x.get("label") for x in d["sections"]]
        ok.append(("card "+ch,s,f"level={d.get('level')} 栏={len(labs)} 末栏={labs[-1]}"))
    except Exception as e: ok.append(("card "+ch,"ERR",str(e)[:50]))
try:
    s,t=get("cards/index.json"); idx=json.loads(t); L=idx if isinstance(idx,list) else idx.get("chars") or idx.get("idx") or []
    ok.append(("index",s,f"{len(L)} 条"))
except Exception as e: ok.append(("index","ERR",str(e)[:60]))
try:
    s,t=get("test.html"); ok.append(("test.html",s,f"{len(t)} bytes, 含rootLink={'rootLink' in t}"))
except Exception as e: ok.append(("test.html","ERR",str(e)[:60]))
for r in ok: print(*r)