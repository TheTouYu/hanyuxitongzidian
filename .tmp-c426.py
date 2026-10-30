import json,subprocess,os,glob
BS=("【403 史部】部首史（㕜shǐ）：甲骨文从又持「中」（中心、中正），象意调解纠纷、物资交易的中人——民间称公证人，朝廷称史官，需执笔书契。轉義：史官→史书。辯證：「事」本从又持干（干＝树杈武器），本义狩猎作战，引申插入刺入与树立；「中」「干」形近混同，故《说文》「事，职也，从史之省声」不确；「吏」是「事」的分化（持武器维持秩序为吏，持干狩猎为事）；「夬」（扳指，引申分决）与「史」形近，从夬者多讹从史。本应分史、事二部，因字混淆合置一部。音源：借音字，古事采可通，古事士通用。字族衍义：①指「干」的刺入 ②指「中」的公正明了 ③形近「夬」之讹，指分决。")
N="字形：古文字字形库未收；原稿史部有「▲民国时期的契约文书」可参。"
D=[
("𪗧","shǐ",BS,"《字彙》「师止切，音史。齿好」——齿好。","史族①之齿：以「齿」定其处，齿利如刺。","sh「失收」取「收」：齿收而啮。"),
("𡶈","shǐ",BS,"《字彙》「所几切，音史。山也」——山名。","史族①之山：以「山」定其形。","sh「失收」取「收」：山收其势。"),
("㳏","shì",BS,"《集韵》「㳏，水名，在河南，或从吏」——水名。","史族①之水：以「水」定其名。","sh「失收」取「收」：水收于道。"),
("𥥥","shì",BS,"《集韵》「穴也」——洞穴。","史族①之穴：以「穴」定其处，刺入而成穴。","sh「失收」取「收」：穴收其气。"),
("㤦","lì",BS,"《集韵》「力志切，音吏。忧也」——忧思。","史族②之心：以「心」定其情，吏事而忧。","l「攏離」取「攏」：忧攏于心。"),
("𧨴","zì",BS,"《类篇》「言入也」——言语刺入人心。","史族①之言：以「言」定其用，言入如刺。","z「凿总」取「凿」：言凿而入。"),
("𩂝","shài",BS,"《汉典》「𩂃的讹字」；𩂃《集韵》「雨疾也」；yīng《龙龛》「𩂝误，霙正，雨雪杂也」。","史族③之讹：形近而误，记作讹变借形。","sh「失收」取「失」：雨失而骤。"),
("𧊍","jué",BS,"《字彙补》「心紫切，音史，龙属」；《广博物志》「明月之珠，藏于蚌中，𧊍龙伏之」；《史记》作蚗——蚗之讹字，指蟪蛄或龙属。","史族③之虫：以「虫」定其类，形近「蚗」而讹。","j「聚决」取「决」：伏而决出。"),
("𨽄","shì",BS,"《广韵》「山阜突也」；《玉篇》「𨸏䆕也」——凿开山陵的通道；《说文》「𨼱，𨸏䆕也，从𨺅，决省声」。","史族③之阜：以「阜」定其地，凿陵为道，正合「决」。","sh「失收」取「收」：道收于山。"),
("𣓊","zì",BS,"《玉篇》「木名」；《正字通》「讹字」。","史族①之木：以「木」定其类，记名而已。","z「凿总」取「凿」：木凿而名。"),
("𡸪","zì",BS,"《字彙补》「庄吏切，音倳。刃也」——刃。","史族①之刃：以「山」形近借，记其刃义。","z「凿总」取「凿」：刃凿而利。"),
("𥑏","shǐ",BS,"《玉篇》「石名」；jué《正字通》「砄字之讹」——石名，实为「砄」之讹。","史族③之石：以「石」定其类，形近而讹。","sh「失收」取「收」：石收其质。"),
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
ST={"𪗧":"《字彙》「齿好」。","𡶈":"《字彙》「山也」。","㳏":"《集韵》「水名，在河南，或从吏」。","𥥥":"《集韵》「穴也」。","㤦":"《集韵》「忧也」。","𧨴":"《类篇》「言入也」——言语刺入人心。","𩂝":"《汉典》「𩂃的讹字」；𩂃《集韵》「雨疾也」。","𧊍":"《字彙补》「龙属」；明月之珠藏于蚌中，𧊍龙伏之——蚗之讹字。","𨽄":"《广韵》「山阜突也」；《玉篇》「𨸏䆕也」——凿开山陵的通道。","𣓊":"《玉篇》「木名」；《正字通》「讹字」。","𡸪":"《字彙补》「刃也」。","𥑏":"《玉篇》「石名」；《正字通》「砄字之讹」。"}
cl=[{"id":f"bsi-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{d[0]}（字卡）",
   "statement":f"{d[0]}（{d[1]}）：{ST[d[0]]}","boundary":"源自《系統漢語》第403部「史部」（卷六十六 采）；字卡五步规程。","permission":"public",
   "fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,d in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡403史部清完2026-10-23","risk":"low","claims":cl},
          open(r"intake\20261023-字卡403史部余.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡403史部余.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    b=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",b,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",b,"--apply","--content-hash",h); run("bundle-apply",b,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",b,"err",v.get("errors"))