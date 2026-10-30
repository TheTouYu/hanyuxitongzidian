import json,subprocess,os,glob
F="【435 甹部】甹＝从丂从西，鸟在巢边伸颈鸣叫；字族取「鸣叫、放任、摇曳」诸面。"
F2="【436 𠬜部】𠬜（pān）＝象双手两边分拨，本义扒开、攀附（攀之初文）；核心实为棥（林木交叉如篱），故樊篱、阻碍义由此出。"
N="字形：古文字字形库未收。"
D=[("䳙","xǐng",F,"《集韵》「鸧䳙，水鸟，似鹭，色苍」——苍色水鸟。","x「续消」取「消」：鸟掠而消。"),
("𦶊","píng",F,"《集韵》「水中浮草」——浮萍（俗蓱字）。","p「拼辟」取「辟」：浮而分。"),
("𦰝","píng",F,"《集韵》「荓蜂，𢊏曳也，通作甹」；又草名马帚。","p取辟：牵引而分。"),
("䀻","pìn",F,"《玉篇》「视也」——视看。","p取辟：视而分。"),
("𧮹","pìn",F,"郭璞注《穆天子传》「有鸟𧮹人」——音义未详，疑鸟名。","p取辟：借声。"),
("𥭢","pīng",F,"《集韵》「舟车篷」——舟车上的篷盖。","p取辟：篷分覆。"),
("𦀔","pīng",F,"《集韵》「吴人数絮」；《字汇》「敝絮」——旧絮。","p取辟：絮分而敝。"),
("𩩍","pīng",F,"《集韵》「肋骨」——肋骨分列如篦。","p取辟：骨分而列。"),
("騁","chěng",F,"《说文》「直驰也，从马甹声」——径直奔驰，引申放任。","ch「刺持」取「持」：放而持缰。"),
("涄","pīng",F,"《集韵》「水貌」——水之貌。","p取辟：水分。"),
("𥪁","pīng",F,"《类篇》「使也」——使令。","p取辟：使而分。"),
("樊","fán",F2,"《说文》「鸷不行也，从棥，棥亦声」——马负过重止而不前；樊篱、樊笼、纷杂、边缘。","f「附分」取「分」：篱分内外。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取本部「鸟鸣放任／双手分拨」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lbc-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第435－436部（卷七十三 釆）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡436a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡436a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡436a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))