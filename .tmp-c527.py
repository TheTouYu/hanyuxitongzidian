import json,subprocess,os,glob
F="【434 釆部·番支】番＝簸箕簸扬筛杂（播之初文）；字族取翻动、繁殖、兽足诸面。"
N="字形：古文字字形库未收。"
D=[("憣","fān",F,"《正字通》「心变动」——心思翻动不宁。","f「附分」取「分」：心翻而分。"),
("襎","fán",F,"《广韵》「襎裷，幭也」——拭物或盖物的布帕；又长袖。","f取分：帕展而分。"),
("𤳖","fān",F,"《玉篇》「却也」；《集韵》「番，更次也，或作𤳖」——更替轮值。","f取分：次第而分。"),
("𤺏","pān",F,"《集韵》「病死」；《广韵》「弃𤺏」——弃置病亡。","p「拼辟」取「辟」：弃而分。"),
("㽃","pān",F,"《玉篇》「㽃瓳，大㼾甎也」——大砖；开封城火器迸发时「㽃瓳飞鸣」。","p取辟：块分为砖。"),
("嶓","bō",F,"《尚书·禹贡》「嶓冢导漾」——梁州嶓山，形如冢，故名。","b「闭剥」取「剥」：山形分冢。"),
("藩","fān",F,"《说文》「屏也，从艸潘声」——篱笆、屏障；藩国屏卫。","f取分：篱分内外。"),
("蕃","fán",F,"《说文》「艸茂也，从艸番声」——茂盛、滋生繁殖。","f取分：草分而茂。"),
("橎","fán",F,"《说文》「木也，读若樊」；《集韵》「坚木，不华而实」——坚木。","f取分：木坚而分。"),
("䪤","fán",F,"《说文》「小蒜也，从韭番声」——小蒜、百合蒜，重瓣之意。","f取分：瓣分而重。"),
("蹯","fán",F,"《集韵》引《说文》「兽足谓之番」——兽足掌、兽迹（番之足印义的分化）。","f取分：趾分而印。"),
("僠","bō",F,"《集韵》「番番，勇也，或从人」——勇壮之貌。","b取剥：勇而分。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取番部「翻动／繁殖／兽足」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lba-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第434部「釆部」（卷七十三 釆）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡434d2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡434d.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡434d.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))