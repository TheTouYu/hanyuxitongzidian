import sys,json,os,glob
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
ROOT=r"D:\系统汉字"
d=json.load(open(os.path.join(ROOT,"web","public","cards","易.json"),encoding="utf-8"))
rows=[]
for g in [s for s in d["sections"] if s.get("groups")][0]["groups"]: rows+=g["rows"]
for ch,py,rad,txt in rows:
    json.dump({"char":ch,"pinyin":py,"level":3,"parent":"易","bus":[{"num":367,"name":"易"}],"sections":[
      {"key":"shiyi","label":"釋義","text":txt,"cites":[]},
      {"key":"zili","label":"字理分析","text":"聲旁「易」：其字形、本義、轉義、辯證、音源、字族衍義見字根卡「易」。","cites":[]},
      {"key":"shengmu","label":"聲母擬態","text":f"今讀 {py}，按聲母取緒論擬態義一面（推）。","cites":[]}]},
      open(os.path.join(ROOT,"web","public","cards",ch+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("衍字卡",len(rows))