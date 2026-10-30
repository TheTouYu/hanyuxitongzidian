import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FY="【第525部「昜部」】昜＝从日从丂，象呼號、日出；轉義飛舉搖盪。字族三面：日烈／日出／日升。"
N="字形：古文字字形库未收。"
D=[("暢","chàng",FY,"从申昜聲：達也、通也（《玉篇》）；「申」本義為雷電閃動。","ch「刺持」取「持」：氣通而持。"),
("婸","dàng",FY,"从女昜聲：放也（《集韻》或作愓、偒），淫逸放蕩。","d「囤动」取「动」：女放而動。"),
("𥂸","yáng",FY,"从皿昜聲：杯也（《集韻》）。","y「圆容」取「圆」：杯圓而容。"),
("糃","tàng",FY,"从米昜聲：精米、播揚後之米（《集韻》），與餳同。","t「涂突」取「突」：米揚而突。"),
("啺","táng",FY,"从口昜聲：《說文》古文「唐」字，說大話。","t取涂突：言大而突。"),
("鐋","tàng",FY,"从金昜聲：治木之器，鐵為齗，摩平斧痕（《韻會》）。","t取涂突：刨木而突。"),
("薚","tāng",FY,"从艸昜聲：草名，蓫薚馬尾，一曰蔏陸（《爾雅》）。","t取涂突：草長而突。"),
("𦳝","tāng",FY,"从艸昜聲：草，枝枝相值、葉葉相當（《說文》），即商陸。","t取涂突：枝葉相當。"),
("蝪","tāng",FY,"从虫昜聲：王蛈蝪，土蜘蛛，穴居有蓋（《爾雅》郭注）。","t取涂突：蟲伏而突。"),
("摥","tàng",FY,"从手昜聲：推也、排也（《集韻》）。","t取涂突：推排而突。"),
("逿","dàng",FY,"从辵昜聲：失據倒也、過也（《集韻》）；行不循道。","d取囤动：行過而動。"),
("䑗","dàng",FY,"从臼昜聲：舂也、持米精（《廣韻》）。","d取囤动：舂臼而動。"),
("𧼮","tāng",FY,"从走昜聲：前走、走貌（《玉篇》）。","t取涂突：疾走而突。"),
("偒","tǎng",FY,"从人昜聲：直也、真也、長貌（《集韻》）；又放蕩。","t取涂突：人直而突。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同部諧聲字分三面：日烈（婸／偒）、日出灼熱（𥂸／糃／啺／鐋／摥／䑗）、日升飛揚（暢／薚／𦳝／蝪／逿／𧼮）；只列本部字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":525,"name":"昜"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lyang6-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}（{p}）＝{xp}",
 "boundary":"源自《系統漢語》第525部「昜部」（卷八十八 昜）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡525d2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡525d.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡525d.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))