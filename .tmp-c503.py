import json,subprocess,os,glob
F="【425 秝部】秝＝从二禾，象禾苗排列稀疏，也象秸秆堆积（分化作厤）；转义：禾的春种秋收→经过（歷）、编绳→缠束（𧝏）、过滤→沥、编簟→并列夹持（兼）、作柴火→陶鬲（㽁）。音源：借音字，义音同「鬲」。"
N="字形：古文字字形库未收。"
D=[("秝","lì","《说文》「稀疏適也。从二禾」——禾苗排列稀疏、株距分明；亦象秸秆堆积。","l「拢离」取「离」：禾苗稀疏、株距相离。"),
("𪅼","lì","《玉篇》「鸟似鹰而大」。","l「拢离」取「离」：鹰大而离。"),
("𪙱","lì","《集韵》「齿病」；齿稀疏之病。","l取离：齿稀疏。"),
("𡐰","lì","《集韵》「坑也」；亦作壢。","l取离：地中空离。"),
("𡮰","lì","《集韵》「㝺𡮰，小劣也」——细小鄙劣。","l取离：细小零星。"),
("磿","lì","《说文》「石声也。从石厤声」——石相击的细声。","l取离：声碎而离。"),
("厤","lì","《说文》「治也。从厂秝声」——治理；与歷同，经历，亦作曆。","l取离：逐一经过而离。"),
("𡓸","lì","《集韵》「积也」——堆叠。","l取离：禾稿分开堆积。"),
("𠠝","lì","《集韵》「割也」；刀割秸秆。","l取离：割断使离。"),
("㻺","lì","《集韵》「玉名」；疑以秸秆抛光玉器。","l取离：磨擦使分离。")]
for ch,p,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取秝「排列／堆积而离析」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"bl-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第425部「秝部」（卷七十 亥）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡425a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡425a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡425a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))