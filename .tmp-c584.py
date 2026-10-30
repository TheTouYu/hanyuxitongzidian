import json,subprocess,os,glob
F="【467 圭部】圭＝甲骨文象上尖下方的玉圭，西周金文讹作相叠的「土」；古人天圆地方，圭上圆下方、琮内圆外方，皆象天地，龟背圆腹方其纹亦如圭。転义为标准（量之所起）、洁净。音源借蛙鸣（其状如蛙）。"
N="字形：古文字字形库未收。"
D=[("圭","guī",F,"本部部首字：玉圭→标准、洁净、圭田。","g「隔估」取「隔」：圭为界限之器。"),
("吉","jí",F,"从口圭声：捧圭对鬼神说祈福之语，吉礼为五礼之首，引申吉祥。","j「聚决」取「聚」：聚福而吉。"),
("壹","yī",F,"从壺吉声：塞口的壶，引申闭塞、专一。","y「续消」取「续」：一而不散。"),
("姞","jí",F,"从女吉声——《说文》「黃帝之後百䱔姓，后稷妃家也」，古姓。","j取聚：姓聚而吉。"),
("詰","jié",F,"从言吉声——《说文》「問也」，追问、责问；引申诘屈。","j取聚：追问而聚。"),
("劼","jié",F,"从力吉声——《说文》「愼也」；《廣韻》「用力也」，勤谨用力。","j取聚：力聚而劼。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取圭部「礼器定界、捧圭祈福」两面：口言取祈福，壺取塞，女力言取分属。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lbv-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第467部圭部（卷七十七 蛙）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡467a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡467a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡467a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))