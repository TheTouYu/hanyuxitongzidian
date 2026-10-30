import json,subprocess,os,glob
BZH="【416 甾部（原属𡿧部）】甾＝甲骨文从屮（草）被水淹没之形，后演变为从田𡿧声，指水淹田：冬天为防水田长草、泥硬开坼，放水浸渍，并放草秸沤肥。转义：浸渍后的田泥土变黑，故引申指黑色（分化作「缁」）。辯證：「甾」与「𠙾」（盛酒浆瓦器）形近，小篆混作一字，《说文》「东楚名缶曰甾」所释当为「𠙾」而非「甾」。字族衍义：①草木被淹死→直立、参差 ②浸渍之泥→黑色。"
N="字形：古文字字形库未收。"
D=[
{"ch":"䎩","p":"zī","xp":"《玉篇》「耕也，亦田一岁也」；通作葘——一年不耕之田。","sm":"z「凿总」取「凿」：耕凿而田。"},
{"ch":"輜","p":"zī","xp":"《说文》「軿车前，衣车后也」——有帷盖的车；輜重即行军所携器械粮草。","sm":"z「凿总」取「总」：杂物总载。"},
{"ch":"鶅","p":"zī","xp":"《广韵》「东方雉名」；《尔雅》「鶅鵵轨」——猫头鹰。","sm":"z「凿总」取「总」：羽总而斑。"},
{"ch":"𡸟","p":"zī","xp":"《集韵》「𡸟嶷，不齐貌」——参差不齐。","sm":"z「凿总」取「凿」：石凿而参差。"},
{"ch":"椔","p":"zī","xp":"《广韵》「木立死」——直立的枯木（水淹草死后直立之状）。","sm":"z「凿总」取「总」：枯木总立。"},
{"ch":"鯔","p":"zī","xp":"《本草》「鲻鱼，似鲤，身圆头扁，骨软」——生于江海浅水，背黑绿腹白。","sm":"z「凿总」取「总」：鱼总而黑。"},
{"ch":"淄","p":"zī","xp":"《水经》「淄水，出泰山莱芜县原山」——淄河，在山东；俗传禹理水功毕，土石黑，波若漆。","sm":"z「凿总」取「总」：水总而黑。"},
]
for e in D:
    sec=[{"key":"bengen","label":"字根本义","text":BZH,"cites":[]},
         {"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":e["xp"],"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取甾部「水淹草死而直／泥浸久而黑」一面，形符各定其落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":e["sm"],"cites":[]}]
    json.dump({"char":e["ch"],"pinyin":e["p"],"bus":[],"sections":sec},open(rf"web\public\cards\{e['ch']}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("写卡",len(D))
cl=[{"id":f"bdc-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{e['ch']}（字卡）",
   "statement":f"{e['ch']}（{e['p']}）：{e['xp']}","boundary":"源自《系統漢語》第416部「𡿧部」（卷六十九 舄）；字卡五步规程。",
   "permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,e in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡416d2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡416d.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡416d.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))