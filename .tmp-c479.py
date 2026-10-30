import json,subprocess,os,glob
B416="【416 𡿧部（災，原属它部）】𡿧＝象三水横流之形，表示洪水泛滥；后添加「才」作声符，与「卂」同源，表示「载」——被洪水覆盖。转义：由洪水泛滥成灾，引申指其他自然灾害与祸害（《类篇》「害也」）。辯證：表声的「才」在小篆中演化成「一」，故《说文》「从一雝川」析形不确。字族衍义：多以衍生字「昔、甾」为声。"
B_XI="【416 昔部（原属𡿧部，从日𡿧声）】昔＝从日𡿧声：「𡿧」指大水，「日」指太阳，象意太阳入水、夜晚降临（《广雅》「夜也」）；或象水面映日、波光粼粼。日又引申指时间，指被洪水淹没的时候——中外神话都说远古地球曾被洪水淹没，故表示过去、以往（《玉篇》「往也、久也、昨也」）。转义：由波光日影引申指涂饰（《正字通》「与错通」）。辯證：《说文》「乾肉也，从残肉，日以晞之」所释应是「腊」而非「昔」，「乾肉」义源自往昔、放置时间久了。音源：借音字，由太阳照水而义音同「舃」（鹊）。"
N="字形：古文字字形库未收。"
D=[
("災","zāi",B416,"象三水横流，洪水泛滥；加「才」为声，与卂同源表覆盖。","应水族之川：三水横流即灾。","z「凿总」取「凿」：水凿而灾。"),
("昔","xī",B_XI,"从日𡿧声——太阳入水为夜，亦波光映日；引申过去、以往。","夜往族之日：以「日」定其时，日落于水。","x「续消」取「消」：日消而夜。"),
("錯","cuò",B_XI,"《说文》「金涂也」——错金工艺：先铸槽、鏨麻点，嵌金丝，再以厝石磨错使平。","涂饰族①之金：以「金」定其物，涂金而磨错。","c「刺持」取「刺」：錾槽如刺。"),
("逪","cuò",B_XI,"《说文》「迹逪也」——交错；《玉篇》「乱也」，今为「错」；《广雅》「背也」。","涂饰族①之辵：以「辵」定其行，行迹交错。","c「刺持」取「刺」：迹交如刺。"),
]
def card(ch,p,Bx,desc,sm):
    return {"char":ch,"pinyin":p,"bus":[],"sections":[
      {"key":"bengen","label":"字根本义","text":Bx,"cites":[]},
      {"key":"zigen","label":"字形","text":N,"cites":[]},
      {"key":"xingpang","label":"形旁声旁","text":desc,"cites":[]},
      {"key":"hengxiang","label":"横向对照","text":"同取本部「洪水覆盖／错磨涂饰」一面，形符各定其落点；故声符给义、形符定落点。","cites":[]},
      {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]}
for t in D:
    ch,p,Bx,desc,sm=t
    json.dump(card(ch,p,Bx,desc,sm),open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("写卡",len(D))
cl=[{"id":f"bdc-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{t[0]}（字卡）",
   "statement":f"{t[0]}（{t[1]}）：{t[3]}","boundary":"源自《系統漢語》第416部「𡿧部」（卷六十九 舄）；字卡五步规程。",
   "permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,t in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡416𡿧部2026-10-23","risk":"low","claims":cl},
          open(r"intake\20261023-字卡416.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡416.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))