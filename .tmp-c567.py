import json,subprocess,os,glob
F="【451→452】云支余字取「云气回转、纷纭」之面；452 全部＝完具、纯色（从入从王/玉）。"
N="字形：古文字字形库未收。"
D=[("澐","yún",F,"《说文》「江水大波謂之澐」——大浪回旋。","y「柔锐」取「锐」：波涌而锐。"),
("篔","yún",F,"《集韵》「篔簹，竹名」——大竹，节长。","y取锐：竹长而锐。"),
("耘","yún",F,"《说文》「除苗間穢也」——除草，往复周遍。","y取锐：草除而锐。"),
("芸","yún",F,"《说文》「艸也，似苜蓿」——芸香草，可辟蠹。","y取锐：草香而锐。"),
("紜","yún",F,"《集韵》「紛紜，亂也」——丝绪纷乱回绕。","y取锐：丝乱而锐。"),
("曇","tán",F,"《集韵》「雲布也」——云气密布；昙花一现。","t「涂突」取「突」：云聚而突。"),
("妘","yún",F,"《说文》「祝融之後姓也」——古姓。","y取锐：借声记姓。"),
("蕓","yún",F,"《集韵》「蕓薹，菜名」——油菜（芸薹）。","y取锐：菜生而锐。"),
("全","quán",F,"《说文》「完也，从入从工」——纯玉为全；引申完备、保全。","q「亲缺」取「缺」：完而补缺。"),
("仝","tóng",F,"「同」的古字，从人从工——共同、齐同。","t取突：人同而突。"),
("痊","quán",F,"《集韵》「病瘳也」——病愈复原。","q取缺：病除而缺。"),
("筌","quán",F,"《庄子》「得魚而忘筌」——捕鱼的竹器。","q取缺：竹器而缺。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取「云气回转／完具」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lbi-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第451－452部（卷七十五 叀）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡452a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡452a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡452a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))