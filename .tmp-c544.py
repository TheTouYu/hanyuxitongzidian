import json,subprocess,os,glob
F="【439 扁部】扁＝门牌，本义「署」；诸字取门牌之扁、薄、普遍、分别四面。"
N="字形：古文字字形库未收。"
D=[("蝙","biān",F,"《说文》「蝙蝠也，从虫扁聲」——蝙蝠，体扁如门牌而善飞。","b「闭剥」取「剥」：翼展而分。"),
("猵","biān",F,"《说文》「獺屬，从犬扁聲」——水獭；猵狙，似猿之兽。","b取剥：兽分而伏。"),
("甂","biān",F,"《说文》「似小瓿，大口而卑」——扁形盆盂。","b取剥：器扁而分。"),
("艑","biàn",F,"《正字通》「艑艖，舟名」；《通雅》「形扁，故呼為扁子」——浅船。","b取剥：舟扁而分。"),
("萹","biān",F,"《说文》「萹茿也，从艸扁聲」；《爾雅》「竹萹蓄」——萹竹，布地而生。","b取剥：枝叶铺分。"),
("鍽","biān",F,"《玉篇》「金鍽」——金饰之名。","b取剥：金薄而分。"),
("鯿","biān",F,"《玉篇》「鯾，魴魚也」；《集韻》「似魴」——鳊鱼，身扁。","b取剥：鱼扁而分。"),
("徧","biàn",F,"《说文》「帀也，从彳扁聲」——周匝一遍，即「遍」。","b取剥：行周而分。"),
("揙","biàn",F,"《说文》「撫也，从手扁聲」；《玉篇》「搏也、擊也」——抚摩、击打。","b取剥：手抚而分。"),
("偏","piān",F,"《说文》「頗也，从人扁聲」——偏斜不平；旁侧、半、属。","p「拼辟」取「辟」：侧而分。"),
("翩","piān",F,"《说文》「疾飛也，从羽扁聲」——轻举疾飞；翩跹。","p取辟：羽展而分。"),
("諞","piǎn",F,"《说文》「便巧言也，从言扁聲」——巧言。","p取辟：言巧而分。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取扁部「扁平／普遍/分别」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lbr-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第439部「扁部」（卷七十三 釆）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡439d2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡439d.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡439d.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))