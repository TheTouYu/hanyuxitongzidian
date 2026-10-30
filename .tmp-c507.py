import json,subprocess,os,glob
F="【426 皆部】皆＝从口从虤（二虎抬前肢直立相抗），实即「䖜」；二虎相抗而齐，故表同时、普遍、都。转义：虎威→强壮、硬实。辨证：小篆讹「曰」为「白」，《说文》「从比从白」析形不确。音源：二虎相争的吼声，义音同「亥」。"
N="字形：古文字字形库未收。"
D=[("皆","jiē","二虎直立相抗而齐，表示同时、普遍、都（《小尔雅》「同也」）。","j「聚决」取「聚」：二虎相聚而齐。"),
("喈","jiē","《说文》「鸟鸣声」，凤凰鸣喈喈；又钟铃声、哭声、风雨声之大。","j取聚：众声相聚。"),
("湝","jiē","《说文》「水流湝湝也」，水流众多；又寒。","j取聚：众水相聚。"),
("諧","xié","《说文》「詥也」——和谐；《文心雕龙》「谐之言皆也，辞浅会俗，皆悦笑也」。","j取聚：众意相聚相合。"),
("龤","xié","《说文》「乐和龤也」——《虞书》「八音克龤」，乐声和谐。","j取聚：八音相聚而和。"),
("鶛","jiē","《尔雅》「鹩鹑其雄鶛」——雄鹌鹑，好斗（原稿有明版画《斗鹑图》）。","j取聚：二鸟相聚而斗。"),
("𩤠","xié","《说文》「马和也」——马性温和，疑本指马嘶鸣相和。","j取聚：马鸣相和。"),
("階","jiē","《说文》「陛也」——台阶；又缘由、梯级、上进。","j取聚：级级相聚而上。"),
("稭","jiē","《说文》「禾稾去其皮，祭天以为席」——去穗去皮的禾茎，可编席。","j取聚：禾稿相聚成席。"),
("𤭧","jiē","《广韵》「牡瓦」——俯盖的瓦；瓦片相次相合。","j取聚：瓦片相聚。")]
for ch,p,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取皆「二虎相抗而齐」的一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"jb-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第426部「皆部」（卷七十 亥）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡426a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡426a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡426a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))