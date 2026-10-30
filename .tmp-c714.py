import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FY="【第543部「玉部」】玉＝象玉串形，《說文》「石之美」；轉義玉製品、瑞玉、美稱、磨煉。"
N="字形：古文字字形库未收。"
D=[("瑄","xuān",FY,"从玉宣聲：璧大六寸謂之瑄（《說文》）。","x「续消」取「续」：璧圆而續。"),
("瑋","wěi",FY,"从玉韋聲：玉名（《廣韻》），珍奇。","w（零声母）取「围而珍」：玉珍而围。"),
("瑗","yuàn",FY,"从玉爰聲：大孔璧（《說文》「大孔璧」），瑗玉。","y「柔锐」取「锐」：璧孔而锐。"),
("璉","liǎn",FY,"从玉連聲：瑚璉，宗廟盛黍稷之器（《說文》「瑚璉也」）。","l「拢离」取「拢」：器聚而拢。"),
("璟","jǐng",FY,"从玉景聲：玉光（《集韻》「玉光也」）。","j「聚决」取「聚」：光聚而决。"),
("璜","huáng",FY,"从玉黃聲：半璧曰璜（《說文》），佩玉。","h「豁活」取「豁」：半璧而活。"),
("璘","lín",FY,"从玉粦聲：璘玢，玉文（《集韻》）。","l取拢离：玉纹而拢。"),
("璲","suì",FY,"从玉遂聲：瑞玉（《說文》「瑞玉也」），佩璲。","s「失收」取「收」：佩玉而收。"),
("瑱","tiàn",FY,"从玉真聲：以玉充耳（《說文》「以玉充耳也」）。","t「涂突」取「涂」：充耳而涂。"),
("璩","qú",FY,"从玉豦聲：環屬（《說文》「環屬」）。","q「亲缺」取「亲」：環親而缺。"),
("瓊","qióng",FY,"从玉敻聲：赤玉（《說文》「赤玉也」），瓊瑤。","q取亲缺：赤玉而親。"),
("瓔","yīng",FY,"从玉嬰聲：瓔珞，似玉之飾。","y取柔锐：飾垂而锐。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"玉系同取「璧、環、佩、瑞」形制一面：瑄大璧、瑗大孔璧、璜半璧、璩環屬、瓔垂飾；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":543,"name":"玉"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lyu4-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第543部「玉部」（卷九十 秋）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡543d2026-10-24","risk":"low","claims":cl},open(r"intake\20261024-字卡543d.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261024-字卡543d.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))