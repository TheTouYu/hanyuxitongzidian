import json,subprocess,os,glob
F="【425 秝部】秝＝从二禾，象禾行稀疏或秸秆堆积；本部余字同取「排列成行／堆叠相离」一面：坑陷、层叠、夹持、行列分明。"
N="字形：古文字字形库未收。"
D=[("攊","lì","《广韵》「击口也」——击打口部。","l取离：击使开离。"),
("𡳸","lì","《说文》「履下也」——鞋底，多层相叠。","l取离：层叠相离。"),
("壢","lì","《集韵》「坑也」——地陷为坑。","l取离：土离成坑。"),
("䥶","lì","《集韵》「鬲，鼎属」——三足炊器；秸稿为柴以烧陶。","l取离：火离器成。"),
("䍽","lì","《集韵》「羖䍽，山羊」；多毛曰羖䍽，或指阉羊。","l取离：毛离而长。"),
("𥌮","lì","《广韵》「𥌮𥉶，视明貌」——目光分明。","l取离：视物分明相离。"),
("𪙽","lì","《集韵》「齿病」；齿疏之病。","l取离：齿疏而离。"),
("儮","lì","《集韵》「人名」——专名用字。","l取离：借声记名。")]
for ch,p,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取秝「行行相离」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"bl3-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第425部「秝部」（卷七十 亥）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡425c2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡425c.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡425c.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))