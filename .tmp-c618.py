import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F="【511 心部】心＝象心臟形，本義心臟；轉義心思、感情。部內从心諸字以心為義符，聲符給情狀：或怒或懼、或悔或慰，各取一面。"
N="字形：古文字字形库未收。"
D=[("情","qíng",F,"从心青聲：人之陰氣有欲者（《說文》「人之陰氣有欲者」），引申情感、情形。","q「亲缺」取「亲」：色親而情。"),
("慍","yùn",F,"从心昷聲：怒也（《說文》「怒也」），慍怒含而不發。","y「柔锐」取「柔」：怒柔於內。"),
("懼","jù",F,"从心瞿聲：恐也（《說文》「恐也」），瞿為鷹隼視物之驚。","j「聚决」取「决」：心聚而决。"),
("憾","hàn",F,"从心感聲：恨也（《說文》「恨也」），感之不平者。","h「豁活」取「豁」：感豁而憾。"),
("懌","yì",F,"从心睪聲：說（悅）也（《說文》「說也」），取睪之明察而喜。","y取柔锐：心銳而悅。"),
("悔","huǐ",F,"从心每聲：悔恨也（《說文》「悔恨也」）。","h取豁活：心豁而悔。"),
("恨","hèn",F,"从心艮聲：怨也（《說文》「怨也」），取艮之止而不通。","h取豁活：氣豁而怨。"),
("怖","bù",F,"从心布聲：惶懼（《說文》「惶也」）。","b「闭剥」取「闭」：心閉而怖。"),
("怯","qiè",F,"从心去聲：多畏也（《說文》「多畏也」），去之而退。","q取亲缺：去而心缺。"),
("恭","gōng",F,"从心共聲：肅也（《說文》「肅也」），共之於心者。","g「隔估」取「隔」：敬而相隔。"),
("恥","chǐ",F,"从心耳聲：辱也（《說文》「辱也」），聞過而心愧。","ch「刺持」取「持」：耳刺而愧。"),
("悉","xī",F,"从心从采：詳盡也（《說文》「詳盡也」），采而心審。","x「续消」取「续」：心續而盡。"),
("慰","wèi",F,"从心尉聲：安也（《說文》「安也」），尉有熨帖之義。","w?零聲母。"),
("慷","kāng",F,"从心康聲：「慷慨」，意氣激昂。","k「口控」取「控」：氣控而慷。"),
("慨","kǎi",F,"从心既聲：「慷慨」，又慨嘆。","k取口控：既而心控。")]
cl=[]
for i,(ch,p,F0,xp,sm) in enumerate(D,1):
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同以心為義符：青取色感、瞿取鷹視、艮取止塞、去取退避。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
    cl.append({"id":f"ldd-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}（{p}）{xp}",
      "boundary":"源自《系統漢語》第511部心部（卷八十四 心）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
json.dump({"schema_version":1,"intent":"字卡511c2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡511c.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡511c.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out, "n:", len(cl))
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))