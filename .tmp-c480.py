import json,subprocess,os,glob
B416="【416 𡿧部（災）】𡿧＝象三水横流之形，表示洪水泛滥；后加「才」作声符，与「卂」同源，表示「载」——被洪水覆盖。转义：由洪水泛滥成灾，引申指其他自然灾害与祸害（《类篇》「害也」）。辯證：表声的「才」在小篆中演化成「一」，故《说文》「从一雝川」析形不确。字族衍义：多以衍生字「昔、甾」为声。"
BXI="【416 昔部（从日𡿧声）】昔＝从日𡿧声：「𡿧」指大水，「日」指太阳，象意太阳入水、夜晚降临（《广雅》「夜也」），或象水面映日、波光粼粼；日又引申指时间，指被洪水淹没的时候——故表示过去、以往（《玉篇》「往也、久也、昨也」）。转义：由波光日影引申指涂饰（《正字通》「与错通」）。辯證：《说文》「乾肉也，从残肉，日以晞之」所释应是「腊」而非「昔」，「乾肉」义源自往昔、放置久了。音源：借音字，义音同「舃」（鹊）。"
D=[
{"ch":"災","p":"zāi","ben":B416,"xp":"象三水横流，洪水泛滥；加「才」为声，与卂同源表覆盖。","sm":"z「凿总」取「凿」：水凿而灾。"},
{"ch":"昔","p":"xī","ben":BXI,"xp":"从日𡿧声——太阳入水为夜，亦波光映日；引申过去、以往。","sm":"x「续消」取「消」：日消而夜。"},
{"ch":"錯","p":"cuò","ben":BXI,"xp":"《说文》「金涂也」——错金：先铸槽、錾麻点，嵌金丝，再以厝石磨错使平。","sm":"c「刺持」取「刺」：錾槽如刺。"},
{"ch":"逪","p":"cuò","ben":BXI,"xp":"《说文》「迹逪也」——交错；《玉篇》「乱也」，今为「错」。","sm":"c「刺持」取「刺」：迹交如刺。"},
]
for e in D:
    sec=[{"key":"bengen","label":"字根本义","text":e["ben"],"cites":[]},
         {"key":"zigen","label":"字形","text":"字形：古文字字形库未收。","cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":e["xp"],"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取本部「洪水覆盖／错磨涂饰」一面，形符各定其落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":e["sm"],"cites":[]}]
    json.dump({"char":e["ch"],"pinyin":e["p"],"bus":[],"sections":sec},open(rf"web\public\cards\{e['ch']}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("写卡",len(D))
cl=[{"id":f"bdc-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{e['ch']}（字卡）",
   "statement":f"{e['ch']}（{e['p']}）：{e['xp']}","boundary":"源自《系統漢語》第416部「𡿧部」（卷六十九 舄）；字卡五步规程。",
   "permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,e in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡416a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡416a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡416a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))