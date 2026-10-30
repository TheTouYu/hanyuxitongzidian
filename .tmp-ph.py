import json,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=json.load(open(r"D:\系统汉字\web\public\glyphs\photos\index.json",encoding="utf-8"))
ph=p.get("photos") or p
for ch in "奚谿徯榽蒵傒縘㨙膎鞵雞騱鼷只枳抧疻軹":
    print(ch, len(ph.get(ch,[]) or []))