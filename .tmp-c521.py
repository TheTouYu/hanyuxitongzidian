import json,subprocess,os,glob
F="【430 戾部】戾＝犬立而欲扑，引申乖张凶残；本部余字多取「立而不稳、曲戾不顺」之状。"
FY="【431 翊部】翊＝从羽立声，象羽毛支起、展翅欲飞，为「翼」之初文；转义辅助（翼之两旁）。字族指展翅状。"
N="字形：古文字字形库未收。"
D=[("悷","lì",F,"《集韵》「懔悷，悲貌」——悲痛欲哭之状。","l「拢离」取「离」：悲气郁而不散。"),
("錑","lèi",F,"《玉篇》「平版具也」；《集韵》「钻也」——凿子一类工具。","l取离：钻木使离。"),
("䓞","lì",F,"《说文》「艸也，可以染留黄」——即狗尾巴草，一名戾草，可染黄。","l取离：草穗垂下而离。"),
("綟","lì",F,"《说文》「帛戾艸染色」——帛色黑而黄；东海有草名䓞，染此色因名綟。","l取离：染草而色变。"),
("㑦","lì",F,"《广韵》「怒也，又很㑦也」——本作戾，俗作㑦。","l取离：怒而背戾。"),
("𥓎","lù",F,"《广韵》「硉矹，石崖不稳貌」——石崖高危不稳。","l取离：石危而欲坠。"),
("㪐","lù",F,"《玉篇》「㪐㩿，不滑利」——不顺畅、不稳。","l取离：物离而滞。"),
("捩","liè",F,"《正韵》「琵琶拨也，或作棙」；《增韵》「紾也」，拗折。","l取离：拨弦拗折。"),
("𨁸","lù",F,"《广韵》「𨁸䠈，行不进也」；又跛足。","l取离：行蹇而离。"),
("翊","yì",FY,"从羽立声，羽毛支起、展翅欲飞——翼之初文；转义辅助。","y「柔锐」取「锐」：羽张而锐。"),
("𥡪","yì",FY,"《集韵》「黍稷蕃芜貌」，亦作翼——禾稼繁盛如展翅。","y取锐：穗张如翼。"),
("熤","yì",FY,"《集韵》「人名」——后魏有张熤。","y取锐：借声记名。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取本部「曲戾／展翅」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lb4-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第430－431部（卷七十一 聿）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡430b2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡430b.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡430b.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))