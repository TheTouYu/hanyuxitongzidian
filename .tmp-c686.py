import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F="【第534部「爿部」·將系】將＝从寸（手）从醬省聲，手持肉以獻祭，《說文》「帥也」；引申扶助、率領、將要。"
N="字形：古文字字形库未收。"
D=[("將","jiāng",F,"从寸从醬省：帥也（《說文》），持肉献祭→扶助、率领、将要。","j「聚决」取「聚」：持而聚。"),
("獎","jiǎng",F,"从犬將聲：《說文》「嗾犬厲之也」，嗾犬使前；引申勸勉、褒賞。","j取聚决：嗾犬而决。"),
("槳","jiǎng",F,"从木將聲：楫屬（《玉篇》），長大曰櫓、短小曰槳。","j取聚决：划水而聚。"),
("䉃","jiǎng",F,"从竹將聲：剖竹未去節謂之䉃（《說文》），即竹槳；去節則無力。","j取聚决：竹節而聚。"),
("鱂","jiāng",F,"从魚將聲：鰪鱂，小魚，善食孑孓。","j取聚决：小魚而聚。"),
("蹡","qiāng",F,"从足將聲：行貌（《說文》）；踉蹡，行不正。","q「亲缺」取「亲」：行親而缺。"),
("螿","jiāng",F,"从虫將聲：寒蜩，似蟬而小色青（《方言》注）。","j取聚决：蟲聚而决。"),
("鏘","qiāng",F,"从金將聲：玉聲／樂聲（《說文》瑲），鏘鏘，盛也。","q取亲缺：金聲親而缺。"),
("摪","jiāng",F,"从手將聲：扶也（《說文》𢪇），扶助；通作將。","j取聚决：扶而聚。"),
("漿","jiāng",F,"从水將省聲：酢漿也（《說文》），帶酸味的飲料；米汁。","j取聚决：汁聚而决。"),
("醬","jiàng",F,"从肉从酉爿聲：盬也（《說文》），以鹽醋醃製的肉醬。","j取聚决：醃聚而决。"),
("蔣","jiǎng",F,"从艸將聲：苽蔣也（《說文》），即菰（茭白）。","j取聚决：草聚而决。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"將系同取「持而聚、扶而进」一面：將言持祭、獎言嗾犬、槳䉃言划具、漿醬言汁肉；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":534,"name":"爿"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"ljiang-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"字卡（第534部將系）：{xp}",
 "boundary":"源自《系統漢語》第534部「爿部」（卷八十九 象）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡534j2026-10-24","risk":"low","claims":cl},open(r"intake\20261024-字卡534j.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261024-字卡534j.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))