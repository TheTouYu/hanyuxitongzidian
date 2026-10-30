import json,subprocess,os,glob
F="【443 卝部】卝（guàn/kuàng）＝商金文人头上两角，指少年「總角」发式；轉義：幼稚→未冶炼的矿石（矿）。辯證：丱、卝、𦫳同源，楷化多混「艹」（卝多作声符、艹多作形符）。音源：借音，总角如鹭之冠羽。"
F2="【443 乖支】乖（guāi）＝卝之二叠，象十分幼稚顽皮；多指奇异歪斜。辯證：《说文》「从𦫳而𠔁」析形不确。音源：借音，义音同癸（睽/乖）。"
N="字形：古文字字形库未收。"
D=[("卝","guàn",F,"《集韻》「丱，束髪皃」；《周禮》注「卝之言礦也，金玉未成器曰礦」——总角少年；未炼矿石。","g「隔估」取「隔」：角分而隔。"),
("乖","guāi",F2,"《广韵》「睽也、離也、戾也、背也」；《广雅》「差也」——十分幼稚顽皮，引申乖违、奇异。","g取隔：背戾而隔。"),
("𨥑","kuàng",F,"《集韻》「銅鐵樸石也，或作礦、鑛、𨥑」——未冶炼的铜铁矿。","k「口控」取「控」：石含而控。"),
("芇","mián",F,"《说文》「相當也」；《廣韻》「今人賭物相折謂之芇」——等值、相当。","m「蒙末」取「蒙」：对折而蒙。"),
("㭉","huá",F,"《说文》「兩刃臿也，从木，𦫳象形」；《康典》「鏵本字」——两刃锹，刀叉。","h「豁活」取「活」：刃分而活。"),
("𢇅","guān",F,"《说文》「織絹从糸貫杼也，从絲省，卝聲」——丝线穿入梭中。","g取隔：线穿而隔。"),
("聯","lián",F,"《说文》「連也，从耳，从絲」——连接、联句、对联。","l「拢离」取「拢」：丝连而拢。"),
("關","guān",F,"《说文》「以木橫持門戶也，从門𢇅聲」——门闩；引申閉、机关、关系、通。","g取隔：门闩而隔。"),
("𪚁","lián",F,"《说文》「齒見皃，从齒䏈聲」——牙齿相连成排。","l取拢：齿排而拢。"),
("𡠒","guān",F,"《集韻》「女字」——女子名用字。","g取隔：借声记名。"),
("𢠶","huàn",F,"《集韻》「患，或作𢤒」——忧患。","h「豁活」取「活」：忧结而活。"),
("㾩","guāi",F2,"《廣韻》「惡瘡」；《集韻》「疥疾」——恶疮、疥。","g取隔：疮结而隔。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取卝部「总角／门闩穿连」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lbv-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第443部「卝部」（卷七十四 雈）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡443a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡443a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡443a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))