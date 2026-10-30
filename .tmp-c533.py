import json,subprocess,os,glob
F="【437 八部·分支】分（fēn）＝从刀八声，象意用刀剖开；引申分配、给与、隔开、半、分量、名分。"
N="字形：古文字字形库未收。"
D=[("份","bīn",F,"《说文》「文质僣也，从人分声」——文质相半，份份（彬彬）；又整体之一部分。","b「闭剥」取「剥」：分而各半。"),
("粉","fěn",F,"《说文》「傅面者也，从米分声」——研米使分散，故粉为碎屑通称。","f「附分」取「分」：碎而分。"),
("鼢","fén",F,"《说文》「地行鼠，伯劳所作也」——鼢鼠，地下打洞损根。","f取分：穴土而分。"),
("枌","fén",F,"《说文》「榆也」——白榆，皮捣成粉可充饥（榆面）。","f取分：皮粉而分。"),
("坋","fèn",F,"《说文》「尘也，一曰大防也」——灰尘；大堤。","f取分：土散而分。"),
("魵","fén",F,"《说文》「鱼名，出薉邪头国」——斑鱼；小鱼曰𩸂。","f取分：鳞斑而分。"),
("羒","fèn",F,"《说文》「牂羊也」；《尔雅》「羊牡羒」——白色公羊。","f取分：羊分牝牡。"),
("盼","pàn",F,"《说文》「美目盼兮，从目分声」——眸子黑白分明；顾视。","p「拼辟」取「辟」：目分黑白。"),
("攽","bān",F,"《说文》「分也，从攴分声」——使分开；减也。","b取剥：分而与之。"),
("貧","pín",F,"《说文》「财分少也，从贝从分」——缺钱、穷困。","p取辟：财分而少。"),
("掰","bāi",F,"用手把东西分开或折断；撕开、揭穿。","b取剥：手掰而剥。"),
("氛","fēn",F,"《说文》「祥气也，从气分声」——预示吉凶的云气；凶气。","f取分：气分而兆。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取分部「剖分」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lbg-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第437部「八部」（卷七十三 釆）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡437b2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡437b.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡437b.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))