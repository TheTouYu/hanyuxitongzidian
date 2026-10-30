import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
# 修正玩卡声母义
p=r"web\public\cards\玩.json"
d=json.load(open(p,encoding="utf-8"))
for s in d["sections"]:
    if s["key"]=="shengmu": s["text"]="w「?」→「w」，零声母方言作影母，取「玩弄而柔」；绪论未列，标推演。"
json.dump(d,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
FY="【第543部「玉部」】玉＝象玉串形（三玉相連），《說文》「石之美」；轉義玉製品、瑞玉、美稱、磨煉。"
N="字形：古文字字形库未收。"
D=[("玫","méi",FY,"从玉攵聲：玫瑰，火齊珠（《說文》「火齊，玫瑰也」）。","m「蒙末」取「末」：珠碎而末。"),
("玡","yá",FY,"从玉牙聲：琅玡，地名／玉名。","y「柔锐」取「锐」：玉锐而洁。"),
("珉","mín",FY,"从玉民聲：石之美者（《說文》「石之美者」），似玉之石。","m取蒙末：石末而似玉。"),
("琮","cóng",FY,"从玉宗聲：瑞玉，大八寸似車釭（《說文》）。","c「刺持」取「持」：玉持而藏。"),
("琰","yǎn",FY,"从玉炎聲：璧上起美色（《說文》「璧上起美色也」）。","y取柔锐：玉光而锐。"),
("瑀","yǔ",FY,"从玉禹聲：石之似玉者（《說文》）。","y取柔锐：石似玉而锐。"),
("璆","qiú",FY,"从玉翏聲：美玉（《說文》「玉也」），可為磬。","q「亲缺」取「亲」：玉親而缺。"),
("璠","fán",FY,"从玉番聲：璵璠，魯之寶玉（《說文》）。","f「附分」取「附」：寶附而分。"),
("璣","jī",FY,"从玉幾聲：珠不圜者（《說文》「珠不圜也」）。","j「聚决」取「聚」：珠聚而决。"),
("琪","qí",FY,"从玉其聲：美玉（《集韻》「玉名」）。","q取亲缺：美玉而親。"),
("琳","lín",FY,"从玉林聲：美玉（《說文》「美玉也」）。","l「拢离」取「拢」：玉聚而拢。"),
("琬","wǎn",FY,"从玉宛聲：圭有琬者（《說文》），琬圭。","w? 取柔锐：玉婉而锐。")]
D[11]=("琬","wǎn",FY,"从玉宛聲：圭有琬者（《說文》），琬圭。","w（零声母影母），取「婉而锐」。")
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"玉系同取「石之美、似玉者亦可称」一面：珉似玉之石、璠魯寶、璣不圜珠、琮瑞玉；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":543,"name":"玉"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lyu3-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第543部「玉部」（卷九十 秋）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡543c2026-10-24","risk":"low","claims":cl},open(r"intake\20261024-字卡543c.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261024-字卡543c.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))