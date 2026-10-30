import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FJ="【第546部「臼部」】臼＝象坎穴形（掘地為臼），後穿木石為臼，《說文》「舂也」。"
FY="【第547部「酉部」】酉＝甲骨文象釀酒器皿（尖底瓶，插火塘餘燼保溫），「酒」之初文（《釋名》「酒，酉也」）；轉義地支第十位、農曆八月、成熟成就、雞（酉時雞歸巢）。"
N="字形：古文字字形库未收。"
D=[("桕","jiù",FJ,"从木臼聲：烏桕，木名，子可榨油。","j「聚决」取「聚」：木實而聚。"),
("舊","jiù",FJ,"从萑臼聲：舊，鴟舊（貓頭鷹）；借為新舊之舊。","j取聚决：鳥旧而聚。"),
("舅","jiù",FJ,"从男臼聲：母之兄弟（《說文》「母之兄弟」）。","j取聚决：親聚而决。"),
("匶","jiù",FJ,"从匚舊聲：棺也（《說文》「棺也」），柩之或体。","j取聚决：棺藏而聚。"),
("䊆","jiù",FJ,"从米臼聲：舂糗也（《說文》），炒米粉。","j取聚决：米聚而决。"),
("嚿","jiù",FJ,"从口舊聲：嚿，聲也（《集韻》）。","j取聚决：聲聚而决。"),
("酉","yǒu",FY,"象尖底酒瓶（插火塘保温），酒之初文；引申地支、八月、成熟、雞。","y「柔锐」取「锐」：酒熟而锐。"),
("酒","jiǔ",FY,"从水酉聲：就也（《說文》「就也，所以就人性之善惡」），釀米成酒。","j取聚决：水聚而酿。"),
("酋","qiú",FY,"从酉从八（酒熟分派）：繹酒也（《說文》「繹酒也」），酋長（分酒者）。","q「亲缺」取「亲」：酒熟而親。"),
("醜","chǒu",FY,"从鬼酉聲：可惡也（《說文》「可惡也」），醜陋。","ch「刺持」取「持」：鬼持而醜。"),
("猶","yóu",FY,"从犬酋聲：玃屬（《說文》「玃屬」），猴類；借為尚且、猶豫。","y取柔锐：獸疑而锐。"),
("逎","qiú",FY,"从辵酉聲：迫也（《說文》「迫也」），遒之或体。","q取亲缺：迫而親。")]
for ch,p,F0,xp,sm in D:
    bn=546 if ch in "桕舊舅匶䊆嚿" else 547
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"臼系同取「坎臼、藏歛」一面（桕木、舊鳥、舅親、匶棺）；酉系同取「酒熟、成就」一面（酒釀、酋分、醜惡、猶疑）；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":bn,"name":"臼" if bn==546 else "酉"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lyou-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第546－547部（卷九十 秋）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡547a2026-10-24","risk":"low","claims":cl},open(r"intake\20261024-字卡547a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261024-字卡547a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))