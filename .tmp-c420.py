import json,subprocess,os,glob
BS=("【才部·存声】「存」从子才声：「子」指小孩，「才」指才能，表小孩能力之有限与潜在；《集韵》「在也」、《玉篇》「有也」。转义：由小孩能力有限，引申需照看培育（《说文》「恤问也」）。字族衍义：多指反复、重叠、再三。")
BZ=("【才部·𢦏声】「𢦏（𢦒）」从戈才声：「才」指花果之梗，从戈表用戈割取，本义指采摘花果；转义伤害（《说文》「伤也」）。字族衍义：①指梗，表示承载 ②指采摘，表示受伤害之后的剩余。")
N="字形：古文字字形库未收；原稿才部有「▲花的结构图」，𢦏族有「▲《种竹斋》局部（明 仇英）」。"
D=[
("荐","jiàn",BS,"从艸存声，《说文》「荐席也」在甸切——草席；《玉篇》「重也、数也、再也」、《集韵》「聚也」。","存族①：以「艸」定其质，草席重叠而铺，即「反复」之在。","j「聚决」取「聚」：草聚而成席。"),
("栫","jiàn",BS,"从木存声，《说文》「以柴木壅也」徂闷切——柴木壅塞；《玉篇》柴木壅水，《韵会》捕鱼具，《博雅》地篱，《广韵》围也。","存族②：以「木」定其用，层层围塞，正是重叠加围。","j「聚决」取「聚」：木聚而壅。"),
("洊","jiàn",BS,"《玉篇》「瀳，水至也；洊同上，又仍也」；《集韵》「再也」——屡次、接连。","存族③：以「水」定其势，一至再至。","j「聚决」取「聚」：水聚而连至。"),
("侟","jiàn",BS,"《正字通》「荐、荐并同」——推荐。","存族④：以「人」定其人，荐而后进。","j「聚决」取「聚」：聚而荐之。"),
("拵","cún",BS,"《集韵》「据也」；zùn《集韵》「插也」——据守，或插置。","存族⑤：以「手」定其动，据而不去。","z「凿总」取「总」：总持之。"),
("袸","jiàn",BS,"《类篇》「衣带」；《玉篇》「褰脬衣」；zùn《集韵》「衣衿」——衣襟、衣带。","存族⑥：以「衣」定其处，重复缠结。","j「聚决」取「聚」：衣聚而系。"),
("臶","jiàn",BS,"《集韵》「再至也，或从水」「重也，或作荐」——再至、重叠。","存族⑦：以「至」定其数，再接而重。","j「聚决」取「聚」：重聚。"),
("珔","jiàn",BS,"《集韵》「才甸切，音荐。玉名」。","存族⑧：以「玉」定其质，记名而已。","j「聚决」取「决」：玉质坚而能决。"),
("銌","zùn",BS,"《集韵》「钻也」；《正字通》「俗鐏字」——戈柄下端的圆锥形金属套。","存族⑨：以「金」定其器，套柄而固。","z「凿总」取「凿」：凿柄而纳。"),
("截","jié",BZ,"《玉篇》「𢧵，齐也、治也、断也，亦作截」——切断、齐整。","𢦏族②之直：以「戈」定其动，割而断之，正是采摘之刃。","j「聚决」取「决」：决断而齐。"),
("裁","cái",BZ,"从衣𢦏声，《说文》「制衣也」昨哉切；《尔雅》「节也」、《篇海》「裁度也」——剪裁、删减、度量、控制。","𢦏族②之制：以「衣」定其物，割取而制衣。","c「刺持」取「刺」：剪刺入布。"),
("载","zài",BZ,"从车𢦏声，《说文》「乘也」作代切；《六书故》「所载之物为载」、《正字通》「承也、胜也」——乘坐、运载、承载。","𢦏族①之承：以「车」定其载，梗承花果即车承物。","z「凿总」取「总」：总载于车。"),
]
def card(ch,p,Bx,a,b,c):
    return {"char":ch,"pinyin":p,"bus":[],"sections":[
      {"key":"bengen","label":"字根本义","text":Bx,"cites":[]},
      {"key":"zigen","label":"字形","text":N,"cites":[]},
      {"key":"xingpang","label":"形旁声旁","text":a,"cites":[]},
      {"key":"hengxiang","label":"横向对照","text":b,"cites":[]},
      {"key":"shengmu","label":"声母义","text":c,"cites":[]}]}
for ch,p,Bx,a,b,c in D:
    json.dump(card(ch,p,Bx,a,b,c),open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("写卡",len(D))
ST={"荐":"《说文》「荐席也，从艸存声」；《玉篇》「重也、数也、再也」——草席，引申重迭屡次。","栫":"《说文》「以柴木壅也」——柴木壅塞；又围也、捕鱼具。","洊":"《玉篇》「水至也；又仍也」；《集韵》「再也」——屡次、接连。","侟":"《正字通》「荐、荐并同」——推荐。","拵":"《集韵》「据也」；又「插也」。","袸":"《类篇》「衣带」；《集韵》「衣衿」——衣襟、衣带。","臶":"《集韵》「再至也」「重也，或作荐」。","珔":"《集韵》「玉名」。","銌":"《集韵》「钻也」；《正字通》「俗鐏字」——戈柄下端的圆锥形金属套。","截":"《玉篇》「𢧵，齐也、治也、断也，亦作截」。","裁":"《说文》「制衣也，从衣𢦏声」；《尔雅》「节也」——剪裁、删减、度量。","载":"《说文》「乘也，从车𢦏声」；《正字通》「承也、胜也」——乘坐运载，又承载。"}
cl=[{"id":f"bzai-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{d[0]}（字卡）",
   "statement":f"{d[0]}（{d[1]}）：{ST[d[0]]}","boundary":"源自《系統漢語》第400部「才部」（卷六十六 采）；字卡五步规程。","permission":"public",
   "fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,d in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡400才部存支𢦏支2026-10-23","risk":"low","claims":cl},
          open(r"intake\20261023-字卡400才部存支.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡400才部存支.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    b=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",b,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",b,"--apply","--content-hash",h); run("bundle-apply",b,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",b,"err",v.get("errors"))