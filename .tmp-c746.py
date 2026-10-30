import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FH="【第550部「火部」】火＝象火焰上騰；部内七系 火／耿／煩／赤／焦／麃／熯／難，焦系取「火所傷、乾枯、憔悴」一面。"
N="字形：古文字字形库未收。"
D=[("鷦","jiāo",FH,"从鳥焦聲：鷦鷯也（《說文》「鷦鷯也」），巧婦鳥。","j「聚决」取「聚」：鳥聚而决。"),
("蕉","jiāo",FH,"从艸焦聲：生枲也（《說文》「生枲也」），芭蕉、蕉麻。","j取聚决：草聚而决。"),
("燋","jiāo",FH,"从火焦聲：所以然持火也（《說文》「所以然持火也」），火把；又灼焦。","j取聚决：火聚而决。"),
("顦","qiáo",FH,"从頁焦聲：顦顇也（《說文》「顦顇也」），枯瘦憔悴。","q「亲缺」取「缺」：面枯而缺。"),
("嫶","qiáo",FH,"从女焦聲：憔悴（《集韻》），面瘦弱。","q取亲缺：女瘦而缺。"),
("蟭","jiāo",FH,"从虫焦聲：蟭螟，螳螂卵房（《集韻》）。","j取聚决：蟲聚而决。"),
("樵","qiáo",FH,"从木焦聲：散木也（《說文》「散木也」），采薪、樵夫。","q取亲缺：木散而缺。"),
("醮","jiào",FH,"从酉焦聲：冠娶禮祭也（《說文》「冠娶禮祭也」），再醮。","j取聚决：酒聚而决。"),
("潐","jiào",FH,"从水焦聲：盡也（《說文》「盡也」），水盡。","j取聚决：水盡而决。"),
("噍","jiào",FH,"从口焦聲：齧也（《說文》「齧也」），嚼食。","j取聚决：口聚而决。"),
("鐎","jiāo",FH,"从金焦聲：鐎斗也（《說文》「鐎斗也」），溫器。","j取聚决：金聚而决。"),
("譙","qiào",FH,"从言焦聲：嬈譙也（《說文》），責讓；譙樓。","q取亲缺：言責而缺。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"焦系同取「火傷而枯、小而聚」一面：鷦鷯、蕉麻、燋火把、顦憔悴、嫶瘦、蟭螟、樵散木、醮祭、潐水盡、噍齧、鐎斗、譙責；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":550,"name":"火"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lhuo6-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第550部「火部」（卷九十一 火）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡550f2026-10-24","risk":"low","claims":cl},open(r"intake\20261024-字卡550f.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261024-字卡550f.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))