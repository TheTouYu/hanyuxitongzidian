import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.venv\Scripts\python.exe".replace(".venv","\u200b.venv") if False else r"D:\系统汉字\.runtime\venv\Scripts\python.exe"
SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FH="【第550部「火部」】火＝象火焰上騰；字族 焦＝火所傷（《說文》「火所傷也」），引申乾枯、焦急、焦點。"
N="字形：古文字字形库未收。"
D=[("焦","jiāo",FH,"从隹从火：火所傷也（《說文》「火所傷也」）；引申乾枯、焦急、焦點。","j「聚决」取「聚」：火聚而决。"),
("鷦","jiāo",FH,"从鳥焦聲：鷦鷯（《說文》「鷦𪃦也」），小鳥。","j取聚决：鳥小而聚。"),
("蕉","jiāo",FH,"从艸焦聲：生枲也（《說文》「生枲也」），芭蕉、蕉麻。","j取聚决：草聚而决。"),
("燋","jiāo",FH,"从火焦聲：灼也（《說文》「灼也」）；又爻灼龜。","j取聚决：火灼而聚。"),
("憔","qiáo",FH,"从心焦聲：憔悴（《集韻》），憂愁瘦損。","q「亲缺」取「亲」：憂而缺。"),
("樵","qiáo",FH,"从木焦聲：木也（《說文》「木也」），取薪、樵夫。","q取亲缺：木取而缺。"),
("瞧","qiáo",FH,"从目焦聲：目昏（《集韻》），俗作看。","q取亲缺：目視而缺。"),
("礁","jiāo",FH,"从石焦聲：水中石（《集韻》），礁石。","j取聚决：石聚而决。"),
("譙","qiào",FH,"从言焦聲：嬈譊（《說文》），責讓；譙樓。","q取亲缺：責而缺。"),
("醮","jiào",FH,"从酉焦聲：冠娶禮祭（《說文》「冠娶禮祭」）。","j取聚决：祭聚而决。"),
("噍","jiào",FH,"从口焦聲：齧也（《說文》「齧也」），咀嚼。","j取聚决：齒聚而决。"),
("劁","qiāo",FH,"从刀焦聲：刈也（《說文》「刂也」），割、断。","q取亲缺：割而缺。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"焦系同取「火傷乾枯」一面：燋灼、憔憂、樵薪、瞧視、礁石、譙責、醮祭、噍齧、劁割；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":550,"name":"火"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lhuo3-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第550部「火部」（卷九十一 火）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡550c2026-10-24","risk":"low","claims":cl},open(r"intake\20261024-字卡550c.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261024-字卡550c.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))