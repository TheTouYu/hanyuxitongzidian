import json,subprocess,os,glob
F="【439 扁部】扁＝门牌，本义「署」；诸字取扁薄、斜出、火干诸面。"
N="字形：古文字字形库未收。"
D=[("蹁","pián",F,"《说文》「足不正也」；一曰拖后足马；又蹁跹，旋行貌。","p「拼辟」取「辟」：足侧而分。"),
("碥","biǎn",F,"《玉篇》收为石名，指水中沙洲、崖岸之石（原稿仅列字族，未另立专条）。","b「闭剥」取「剥」：石扁而分。"),
("惼","biǎn",F,"《玉篇》「急也」——心气褊急。","b取剥：心窄而分。"),
("媥","piān",F,"《广韵》「身轻便也」——体轻貌。","p取辟：轻侧而分。"),
("煸","biān",F,"《集韵》「火干也」——以火烘烤使干。","b取剥：火迫而分。"),
("鶣","piān",F,"《集韵》「鶣鷃，鸟名」——小鸟。","p取辟：羽轻而分。"),
("糄","biān",F,"《集韵》「米也」——米屑。","b取剥：米碎而分。"),
("犏","piān",F,"《集韵》「犏牛，出西番」——牦牛与黄牛杂交之牛。","p取辟：杂而分。"),
("騗","piàn",F,"《字彙》「躍而上馬」——骗马；今「骗」本字，引申欺骗。","p取辟：跃侧而上。"),
("褊","biǎn",F,"《说文》「衣小也」——衣狭；引申狭隘、褊急。","b取剥：衣窄而分。"),
("𪉱","biàn",F,"《玉篇》「鹽也」——盐。","b取剥：盐粒而分。"),
("𦄒","biān",F,"《集韵》「編也」——编联。","b取剥：丝编而分。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取扁部「扁薄／斜出」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lbs-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第439部「扁部」（卷七十三 釆）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡439e2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡439e.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡439e.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))