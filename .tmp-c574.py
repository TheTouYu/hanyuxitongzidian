import json,subprocess,os,glob
F="【460 卷部】卷＝从卩从龹，象膝曲之形（《说文》「厀曲也」），引申卷曲、书卷；461 川部＝贯穿通流水。"
N="字形：古文字字形库未收。"
D=[("卷","juǎn",F,"《说文》「厀曲也」——膝弯屈曲；引申卷曲、书卷、卷帙。","j「聚决」取「聚」：曲而聚。"),
("捲","juǎn",F,"《集韵》「斂也」——把物卷起、收拢。","j取聚：手卷而聚。"),
("鬈","quán",F,"《说文》「髮好也」——头发卷曲美好。","q「亲缺」取「缺」：发卷而缺。"),
("菤","quán",F,"《说文》「菤耳，卷耳也」——卷耳草，实如鼠耳。","q取缺：草卷而缺。"),
("婘","quán",F,"《集韵》「美也」——美好，取卷曲柔媚。","q取缺：美曲而缺。"),
("惓","quán",F,"《集韵》「惓惓，謹也」——恳切、谨慎。","q取缺：心切而缺。"),
("錈","juǎn",F,"《集韵》「屈金也」——把金属屈卷。","j取聚：金卷而聚。"),
("鬳","yàn",F,"《说文》「鬲屬」——陶鬲一类，取卷曲之形。","y「柔锐」取「锐」：器曲而锐。"),
("川","chuān",F,"《说文》「貫穿通流水也」——三画象水流贯穿。","ch「刺持」取「持」：水贯而持。"),
("州","zhōu",F,"《说文》「水中可居曰州」——水中陆地，古九州。","zh「凿总」取「总」：水聚而总。"),
("順","shùn",F,"《说文》「理也，从頁从巛」——头顺水流，引申顺从、顺利。","sh「失收」取「收」：顺而收。"),
("巡","xún",F,"《说文》「視行也，从辵川聲」——巡视、往来查看。","x「续消」取「续」：行续而消。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取卷／川支「卷曲、贯穿」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lbb-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第460－461部（卷七十五 叀）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡460a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡460a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡460a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))