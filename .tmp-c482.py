import json,subprocess,os,glob
BXI="【416 昔部（从日𡿧声）】昔＝从日𡿧声：太阳入水为夜，或水面映日；引申指过去、以往（《玉篇》「往也、久也、昨也」），又引申指涂饰（与「错」通）。字族衍义：①涂饰／错磨交错 ②往昔→安置、吝惜、时间久。"
BZH="【416 甾部（原属𡿧部）】甾＝甲骨文从屮（草）被水淹没之形，后演变为从田𡿧声，指水淹田：冬天为防水田长草、泥硬开坼，放水浸渍，并放草秸沤肥。转义：浸渍后的田泥土变黑，故引申指黑色（分化作「缁」）。辯證：「甾」与「𠙾」（盛酒浆瓦器）形近，小篆混作一字，《说文》「东楚名缶曰甾」所释当为「𠙾」而非「甾」。字族衍义：①草木被淹死→直立、参差 ②浸渍之泥→黑色。"
N="字形：古文字字形库未收。"
D=[
{"ch":"措","p":"cuò","ben":BXI,"xp":"《说文》「置也」——放置、举投、施布；又通「刺」。","sm":"c「刺持」取「刺」：置而如刺。"},
{"ch":"厝","p":"cuò","ben":BXI,"xp":"《说文》「厉石也」——磨刀石；又「置也」安置、归葬。","sm":"c「刺持」取「刺」：石刺而砺。"},
{"ch":"惜","p":"xī","ben":BXI,"xp":"《说文》「痛也」——哀痛、可惜；《玉篇》「吝也」、爱惜。","sm":"x「续消」取「消」：惜其消尽。"},
{"ch":"醋","p":"zuò","ben":BXI,"xp":"《说文》「客酌主人也」——客以酒回敬主人；后指酸酒、醯。","sm":"c「刺持」取「刺」：酸刺于舌。"},
{"ch":"腊","p":"xī","ben":BXI,"xp":"《集韵》「乾肉也，从残肉，日以晞之」——乾肉；今为臘之简化。","sm":"x「续消」取「消」：日晒而消水。"},
{"ch":"借","p":"jiè","ben":BXI,"xp":"《说文》「假也」——暂时使用他人财物；又助也、凭藉。","sm":"j「聚决」取「决」：借而决之。"},
{"ch":"蜡","p":"qù","ben":BXI,"xp":"《说文》「蝇䏣也」——蛆；又水母（䖳）、年终祭名（䄍）。","sm":"q「亲缺」取「缺」：祭缺而蜡。"},
{"ch":"㳻","p":"sè","ben":BXI,"xp":"《说文》「所以壅水也」——堵水的土坝，抬高水位而水从上游漫流。","sm":"s「失收」取「收」：水收而壅。"},
{"ch":"𨛳","p":"xí","ben":BXI,"xp":"《广韵》「乡名」——乡名用字。","sm":"x「续消」取「消」：地名借声。"},
{"ch":"葘","p":"zī","ben":BZH,"xp":"《说文》「不耕田也」——一年不耕之田，草塞其中；亦作菑、灾。","sm":"z「凿总」取「凿」：草凿而塞。"},
{"ch":"錙","p":"zī","ben":BZH,"xp":"《说文》「六铢也」——古重量单位，四锱为一两，借指微小（锱铢）。","sm":"z「凿总」取「总」：微小而总聚。"},
{"ch":"緇","p":"zī","ben":BZH,"xp":"《说文》「帛黑色」；《释名》「缁，滓也，泥缁黑色者曰滓」——黑帛。","sm":"z「凿总」取「总」：染总而黑。"},
]
for e in D:
    sec=[{"key":"bengen","label":"字根本义","text":e["ben"],"cites":[]},
         {"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":e["xp"],"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取本部「往昔之久／水淹而黑」一面，形符各定其落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":e["sm"],"cites":[]}]
    json.dump({"char":e["ch"],"pinyin":e["p"],"bus":[],"sections":sec},open(rf"web\public\cards\{e['ch']}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("写卡",len(D))
cl=[{"id":f"bdc-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{e['ch']}（字卡）",
   "statement":f"{e['ch']}（{e['p']}）：{e['xp']}","boundary":"源自《系統漢語》第416部「𡿧部」（卷六十九 舄）；字卡五步规程。",
   "permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,e in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡416c2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡416c.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡416c.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))