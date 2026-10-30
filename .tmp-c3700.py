import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\䒶.json"
d={"char":"䒶","head":"䒶","pinyin":"tiān","noRoot":True,"bus":[{"num":26,"name":"弋"}],
 "sections":[
  {"key":"shiyi","label":"释义","text":"䒶 tiān 《玉篇》：“古文天字。”","cites":[]},
  {"key":"ezhi","label":"讹字说明","text":"③形近字之訛（原文未列具體字）","cites":[]}]}
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("ok")