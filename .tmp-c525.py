import json,subprocess,os,glob
F="【434 釆部·番支】番（fán）＝从甶（面具，代指簸箕状器具）从釆（分辨），象意用簸箕簸扬淘洗、筛出谷米杂质——播之初文；亦解为兽类宽圆足印（《说文》「兽足谓之番」）。"
N="字形：古文字字形库未收。"
D=[("翻","fān",F,"《说文》「飞也，从羽番声」——反复、翻覆；簸扬时上下翻动。","f「附分」取「分」：翻而分。"),
("燔","fán",F,"《说文》「爇也，从火番声」——翻来覆去地烧烤；宗庙炙肉亦曰燔。","f取分：翻烤而分。"),
("璠","fán",F,"《说文》「玙璠，鲁之宝玉」——纹理颜色皆美的玉，近看瑟若。","f取分：理分而美。"),
("羳","fán",F,"《说文》「黄腹羊」——肚皮黄色，如肚皮翻出。","f取分：腹翻而分。"),
("蟠","fán",F,"《说文》「鼠妇也，从虫番声」——鼠妇虫背有横文、多足，翻石而见；又盘曲。","f取分：翻而见之。"),
("㸋","fán",F,"《说文》「宗庙火孰肉，从炙番声」——反来覆去烤熟的祭肉。","f取分：翻炙而分。"),
("膰","fán",F,"《广韵》「祭余熟肉」——祭祀剩下的熟肉，分赐于人。","f取分：分胙。"),
("繙","fān",F,"《说文》「冤也，从糸番声」——反复、杂乱；缤繙，风吹旗貌。","f取分：丝乱而分。"),
("播","bō",F,"《说文》「穜也，一曰布也，从手番声」——下种、传布、扬弃；播种图可证。","b「闭剥」取「剥」：撒种而分。"),
("譒","bò",F,"《说文》「𢾭也，从言番声」——布告；谣传。","b取剥：言布而分。"),
("磻","bō",F,"《说文》「以石箸隿𦅾也，从石番声」——系石于射鸟丝缕上；能翻飞之石。","b取剥：石飞而分。"),
("皤","pó",F,"《说文》「老人白也，从白番声」——老人须发白；素也，大腹。","p「拼辟」取「辟」：发白而分。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取番部「簸扬翻动」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lb8-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第434部「釆部」（卷七十三 釆）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡434b2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡434b.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡434b.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))