import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
G=r"D:\系统汉字\web\public\glyphs"
idx=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8")).get("chars") or {}
for ch in ("箘","箟","箟","菌"):
    if ch in idx:
        fs=idx[ch].get("files"); print(ch,fs[:10] if fs else fs)
        for f in (fs or [])[:3]:
            print("  exists",f,os.path.exists(os.path.join(G,f)))
print("dirs with 8 files:", [d for d in os.listdir(G) if os.path.isdir(os.path.join(G,d)) and len([x for x in os.listdir(os.path.join(G,d)) if x.lower().endswith(('.png','.jpg'))])==8][:12])