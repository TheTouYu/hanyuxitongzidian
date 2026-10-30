import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FH="【第550部「火部」】火＝象火焰上騰；字族 耿（耳著頰之明）／煩（熱頭痛）／赤（火色）／焦（火所傷）／麃（火燒）。"
N="字形：古文字字形库未收。"
D=[("褧","jiǒng",FH,"从衣耿聲：檾也（《說文》「檾也」），罩衣（裯）。","j「聚决」取「聚」：衣聚而决。"),
("薠","fán",FH,"从艸煩聲：青薠，草名（《說文》引《詩》）。","f「附分」取「附」：草附而分。"),
("熲","jiǒng",FH,"从火頃聲：火光也（《說文》「火光也」）。","j取聚决：光聚而决。"),
("赦","shè",FH,"从攴赤聲：置也（《說文》「置也」），赦免、寬宥。","sh「失收」取「失」：釋而收。"),
("郝","hǎo",FH,"从邑赤聲：右扶風鄠盩厔鄉（《說文》），地名、姓。","h「豁活」取「豁」：地赤而豁。"),
("赫","hè",FH,"从二赤：火赤貌（《說文》「火赤皃」），顯赫。","h取豁活：火赤而豁。"),
("嚇","xià",FH,"从口赫聲：以口拒人（《說文》「以口距人」），恐嚇。","x「续消」取「续」：聲續而消。"),
("赧","nǎn",FH,"从赤𡰥聲：面慚赤也（《說文》「面慚赤也」）。","n「纳弄」取「纳」：面赤而纳。"),
("赩","xì",FH,"从赤色：赤色（《說文》「赤色也」）。","x取续消：赤而消。"),
("浾","chēng",FH,"从水赤聲：赤汁（《說文》「赤汁」）。","ch「刺持」取「持」：汁赤而持。"),
("螫","shì",FH,"从虫赦聲：毒蟲刺人（《說文》「蟲行毒也」）。","sh取失收：蟲刺而收。"),
("焃","hè",FH,"从火赫聲：火赤貌（《集韻》）。","h取豁活：火赤而豁。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"火系同取「赤色、光熱」一面：赫赫火赤、赧赩面赤、浾赤汁、赦釋、螫毒；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":550,"name":"火"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lhuo2-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第550部「火部」（卷九十一 火）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡550b2026-10-24","risk":"low","claims":cl},open(r"intake\20261024-字卡550b.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261024-字卡550b.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))