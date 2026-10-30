import json,subprocess,os,glob
F="【444 雈部】雈＝苍鹭；诸字取鹭之「盯水面、鸣声亮、颈曲、逐鱼」诸面。"
N="字形：古文字字形库未收。"
D=[("觀","guān",F,"《说文》「諦視也，从見雚聲」——细看、仰视；楼观、景观。","g「隔估」取「隔」：目视而隔。"),
("矔","guàn",F,"《说文》「目多精也，益州謂瞋目曰矔」——目光炯炯、全神贯注。","g取隔：目注而隔。"),
("懽","huān",F,"《说文》「喜𠭥也，从心雚聲」；《爾雅》「懽懽愮愮，憂無告也」——欢喜，亦忧。","h「豁活」取「活」：心喜而活。"),
("驩","huān",F,"《说文》「馬名，从馬雚聲」；《正字通》「讙、懽、歡並通」——马名；通欢、观。","h取活：马欢而活。"),
("讙","huān",F,"《说文》「嘩也，从言雚聲」——喧哗；责让。","h取活：声喧而活。"),
("歡","huān",F,"《说文》「喜樂也，从欠雚聲」——喜悦欢乐。","h取活：喜而气舒。"),
("孉","quán",F,"《廣韻》「婘，美皃，孉同」——美好。","q「亲缺」取「缺」：美而缺。"),
("爟","guàn",F,"《说文》「取火于日，官名，舉火曰爟」——《周禮》司爟掌行火之政令。","g取隔：取火而隔。"),
("鱹","guàn",F,"《集韻》「人名」；疑同「鰥」，掠食性鱼，如鹭食鱼。","g取隔：鱼食而隔。"),
("貛","huān",F,"《说文》「野豕也，从豸雚聲」——獾，穴地而處；亦公狼。","h取活：穴兽而活。"),
("權","quán",F,"《说文》「黃華木，一曰反常」——黄华木；引申秤锤、权变、权柄、摄官。","q取缺：衡而制缺。"),
("虇","quán",F,"《集韻》「竹葦萌」；「萑葦之類初生者皆曰虇」——苇竹嫩芽。","q取缺：芽出而缺。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取雈部「鹭之视／鸣／曲颈」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lbx-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第444部「雈部」（卷七十四 雈）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡444a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡444a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡444a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))