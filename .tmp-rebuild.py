import json,io,os,sys,copy
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
tpl=json.load(io.open(os.path.join(C,"蔗.json"),encoding="utf-8"))
new=copy.deepcopy(tpl)
new.update({"char":"𤳯","head":"𤳯（𤳐）","pinyin":"zhù"})
new.pop("aliases",None)
new["sections"]=[
 {"key":"shiyi","label":"释义","text":"𤳯（𤳐）zhù《廣韻》：「章恕切，音翥。筐𤳯。」《博雅》：「𤳯，𤲙也。」筐子。畚箕。","cites":[]},
 {"key":"shengmu","label":"声母拟态","text":"zh「凿总」取「总」：筐器總收（推）。","cites":[]},
 {"key":"suoshujuan","label":"所属卷","text":"卷七 斤（第45部 石）","links":[{"ch":"卷七斤","label":"卷七 斤"},{"ch":"石","label":"45 石"}]},
]
json.dump(new,io.open(os.path.join(C,"𤳯.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print(json.dumps(new,ensure_ascii=False)[:300])