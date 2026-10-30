import json,subprocess,os,glob
F="【466 眔部】眔＝甲骨文从目下许多小点，蟾蜍的局部象形，小点是它皮肤上的疙瘩，本指蟾蜍（癩蛤蟆）；音源字，取蟾蜍叫声，义音同「沓」。"
FY="【466 眔部字族】从眔诸字皆取蟾蜍「皮衣鼓囊、爬行相及」两面。"
N="字形：古文字字形库未收。"
D=[("眔","dà",F,"本部部首字：蟾蜍的局部象形；转义为蟾蜍、蟾酥、蟾衣。","d「囤动」取「囤」：伏而囤聚。"),
("褱","huái",FY,"从衣眔声：衣如蟾蜍之皮，鼓鼓囊囊，故指怀挟、囊袋；后作「懷」。","h「豁活」取「活」：内有所藏。"),
("沓","tà",FY,"从水眔声（《说文》「語多沓沓也」）：水流重叠相及，引申繁多、重复、合沓。","t「涂突」取「涂」：重叠相涂。"),
("遝","tà",FY,"从辵眔声（《说文》「䢔也」）：行而相及，杂沓而来。","t取涂：行而相及。"),
("鰥","guān",FY,"从魚眔声（《说文》「魚也」）：大鱼；借指无妻之男（鰥夫），取鱼独行不偶。","g「隔估」取「隔」：独而相隔。"),
("䓠","tà",FY,"从艸眔声（《集韵》「菜名，生水中，大葉」）：水中大叶菜，或作𦵺。","t取涂：水生相涂。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取眔部「蟾蜍皮裹、爬行相及」两面：衣取其裹，水、辵、艸取其相及，魚取其独。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lbu-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第466部眔部（卷七十七 蛙）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡466a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡466a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡466a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))