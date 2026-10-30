import json,subprocess,os,glob
F="【427 聿部·盡】盡＝从皿从聿，聿所持竹枝是刷帚（截竹一节、剖三分之二成刷），象刷洗中空器皿；器中之物已无才须刷，故引申完毕、竭尽、极端、全部。辨证：战国古文从火作「䀆」，实为「燼」之初文。音源：本聿声（聿、尹相通），义音同「尹」。字族多指剩余、细小。"
N="字形：古文字字形库未收。"
D=[("盡","jìn","刷洗器皿，器空为尽；引申完毕、竭尽、极端、悉皆。","j「聚决」取「聚」：物聚而尽。"),
("贐","jìn","《说文》「会礼也」——《孟子》「行者必以赆」，送行之赠礼。","j取聚：聚货以赠。"),
("燼","jìn","《说文》「火余也」——燃烧后的余烬、薪柴。","j取聚：火聚成烬。"),
("嚍","jìn","《集韵》「愤也」——愤怒，即言尽辞穷之意。","j取聚：气聚而愤。"),
("壗","jìn","《广韵》「石似玉」——疑本指琢玉时产生的灰尘。","j取聚：尘聚而细。"),
("璶","jìn","《说文》「石之似玉者」——疑指玉加工后的下脚料。","j取聚：玉屑聚余。"),
("濜","jìn","《集韵》「水名，在襄阳」；《广韵》「濜溳，水流急貌」。","j取聚：水聚而急。"),
("嬧","jìn","古女子人名用字。","j取聚：借声记名。"),
("儘","jǐn","《字汇》「与尽同，皆也」——尽管、尽量。","j取聚：悉皆聚尽。"),
("孻","nái","《菽园杂记》「广东谓老人所生幼子曰孻」——幼子。","n「纳弄」取「纳」：老来得子纳入。"),
("㯸","jǐn","《玉篇》「盂也」——痰盂。","j取聚：器聚污物。"),
("𣃏","zhuó","《字汇补》「与斵同」——砍、剁碎。","zh「凿总」取「凿」：斧凿而碎。")]
for ch,p,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取尽部「器空而余」一面：余烬、余礼、余屑、余子，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"yb5-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第427部「聿部」（卷七十一 聿）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡427e2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡427e.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡427e.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))