import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FY="【第524部「養部」】養＝甲骨文从攴从羊，象持鞭牧羊；音源本羊聲。轉義：飼養牲畜→供奉侍候→修飾→驅使→快樂。字族分四面：羊病瘙癢／牧羊蕩漾近侍／反芻／飼養蓄積。"
N="字形：古文字字形库未收。"
D=[("養","yǎng",FY,"从攴从羊：持鞭牧羊，引申飼養、供養、修飾、驅使、快樂。","y「圆容」取「圆」：牧養而周。"),
("癢","yǎng",FY,"从疒養聲：膚欲搔（《集韻》），取羊病瘙癢。","y取圆容：癢在皮中。"),
("𧓲","yǎng",FY,"从虫養聲：蛘，蟲名，搔蛘（《集韻》）。","y取圆容：蟲癢而圓。"),
("懩","yǎng",FY,"从心養聲：心所欲也，又心憂不定（《集韻》）。","y取圆容：心欲而動。"),
("攁","yǎng",FY,"从手養聲：發動也（《集韻》）。","y取圆容：手動而發。"),
("瀁","yàng",FY,"从水養聲：瀁瀁無涯際，水溢蕩貌（《玉篇》）。","y取圆容：水蕩而遠。"),
("𩜒","nǎng",FY,"从食養聲：近也、忽也，咫尺見也（《五音集韻》）。","n「纳弄」取「纳」：近而納。"),
("𥶑","qiǎng",FY,"从竹養聲：竹名（《集韻》）。","q「亲缺」取「亲」：竹節相親。"),
("㔦","yǎng",FY,"从力養聲：勸也、勸勉（《玉篇》）。","y取圆容：勉而周。"),
("䑆","yǎng",FY,"从肉養聲：䑆䑆，欲吐，取羊反芻（《集韻》）。","y取圆容：反芻而吐。"),
("鱶","xiǎng",FY,"从魚養聲：魚腊，剖開晾乾之魚（《集韻》）。","x「续消」取「消」：魚腊而消。"),
("䭥","yàng",FY,"从食養聲：餌也、糕餅（《玉篇》）。","y取圆容：食團而圓。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同部諧聲字分四面：羊病瘙癢（癢／𧓲／懩／攁）、牧羊蕩漾近侍（瀁／𩜒／𥶑／㔦）、反芻（䑆）、飼養蓄積（鱶／䭥）；只列本部字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":524,"name":"養"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lyang2-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}（{p}）{xp}",
 "boundary":"源自《系統漢語》第524部「養部」（卷八十七 羊）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡524a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡524a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡524a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))