import urllib.request,json,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
try:
    j=json.load(urllib.request.urlopen("http://127.0.0.1:8091/cards/%E6%96%A6.json?v=1",timeout=5))
    for s in j["sections"][:4]: print(s["key"],"|",s["text"][:36])
    print("glyphChar",j.get("glyphChar"))
except Exception as e: print("ERR",e)