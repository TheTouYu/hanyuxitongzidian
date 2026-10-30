import json,subprocess,os,glob
B383="源自《系統漢語》第383部「糸部」；字卡五步规程。"
B384="源自《系統漢語》第384部「系部」；字卡五步规程。"
K="topic-zika-shizi"
rows=[
("絲",B383,"絲 sī：从糸之二迭，本屬迭體字，指絲線繞成的絲束或織物，或指絲線特別細長（《說文》蠶所吐也，从二糸）。"),
("鷥",B383,"鷥 sī：从鳥絲省聲，鷺鷥即白鷺，頭上冠羽似絲束（郭璞注「頭上毛似絲」），取細長如絲。"),
("噝",B383,"噝 sī：象聲字，形容尖細的長聲；與絲同取「細長」之狀以定聲。"),
("𨖾",B383,"𨖾 biān：从辵，振繩墨也（《玉篇》布千切），行不絕也（《字彙》）；繩墨之線長而振，行如線不絕。"),
("蕬",B383,"蕬 sī：从艸絲聲，菟蕬即菟絲（《爾雅》女蘿菟絲），或指蕬草（江南水草葉如薤）；二物皆絲狀。"),
("系",B384,"系 xì：从手抓絲形，象意手將多根絲相連表示聯結，亦可象拈出絲頭即絲緒；轉義繼承、譜系。"),
("係",B384,"係 xì：从人从系，系亦聲，拴結捆綁；甲骨文象用繩索勒住脖子，或紮束頭髮形，今簡化作系。"),
("乿",B384,"乿 zhì／luàn：从糸，《集韻》理也（或作𦠋𠩺，通作治），luàn 古同亂；一繩之收緒則治、棼緒則亂。"),
("𥒶",B384,"𥒶 huà：从石，《字彙補》聲也，石聲；系部旁支，以石定類。"),
("𧚃",B384,"𧚃 xì：从衣，《集韻》䙎帶也或作𧚃𦃝，即衣帶；《正字通》謂俗系字，與系、係同取繫。"),
]
cl=[]
for i,(ch,b,st) in enumerate(rows,1):
    cl.append({"id":f"bn-{i:03d}","node":"hanzi-yinyuan","topic_id":K,"title":f"{ch}（字卡）","statement":st,"boundary":b,"permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
json.dump({"schema_version":1,"intent":"字卡383絲384系2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡384系部.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡384系部.json","--format","json")
print("capture tail:", out[-160:].replace("\n"," "))
files=sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)
b=os.path.basename(files[-1])[:-5]
st=json.loads(run("bundle-status",b,"--format","json")); h=st["bundles"][0]["content_hash"]
print("bundle",b,h[:12])
print(run("bundle-approve",b,"--apply","--content-hash",h)[:80].replace("\n"," "))
print(run("bundle-apply",b,"--apply","--content-hash",h)[:80].replace("\n"," "))
run("rebuild")
v=json.loads(run("validate","--format","json")); print("errors",v.get("errors"))