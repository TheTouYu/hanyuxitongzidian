import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F="【第514部「匚部」】匚＝甲骨文象槽形器，指箭杆矯正器：火烤彎處、嵌槽抽拉使直，為「匡」之初文（《廣韻》「輔助也。正也」）；轉義放逐、方器、筐；辯證《說文》「匸」與「匚」同字，與「曲」形近而混；音源為抽拉箭杆之聲。"
N="字形：古文字字形库未收。"
D=[("匚","fāng",F,"本部字根：石槽矯箭之器，引申匡正、方器、筐。","f「附分」取「附」：箭附槽而直。"),
("匠","jiàng",F,"从匚从斤：木工（《說文》「木工也」），斤所以作器。","j「聚决」取「聚」：聚材而成器。"),
("𪀘","jiàng",F,"《玉篇》「巧婦也」——工雀（鷦鷯），取其巧於營巢如匠。","j取聚决：巧聚而成巢。"),
("匞","jiàng",F,"《正字通》「匠本字」——从工从匚，規矩準繩方正之意。","j取聚决：聚工而正方。"),
("䞪","jiàng",F,"从走匠聲：《說文》「行皃」——行之狀，取抽拉而行。","j取聚决：行聚而疾。"),
("驅","qū",F,"《字彙補》「與驅同」——驅使，取矯正時抽拉驅趕之勢。","q「亲缺」取「缺」：驅而離。"),
("匡","kuāng",F,"从匚从㞷（往）：對不正者使之直（《廣韻》「輔助也。正也」）。","k「口控」取「控」：控而正之。"),
("恇","kuāng",F,"从心匡聲：《說文》「怯也」——膽怯恐懼，取被矯正之不安。","k取口控：心控而怯。"),
("誆","kuāng",F,"从言匡聲：《玉篇》「狂言也」——說大話、欺騙。","k取口控：言控而誑。"),
("劻","kuāng",F,"《集韻》「劻勷，遽也」——急促不安之狀。","k取口控：迫控而遽。"),
("哐","kuāng",F,"象聲詞，多形容撞擊聲——取器物相擊之聲。","k取口控：聲撞而控。"),
("筐","kuāng",F,"从竹匡聲：《說文》「飲器，筥也」——受盛方器，匚引申為容器。","k取口控：器控而盛。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同部諧聲字分兩面：矯正整治（匠／𪀘／匞／䞪／驅）、被匚之凌亂彎曲（匡／恇／誆／劻／哐／筐）；只列本部字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":514,"name":"匚"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lfa-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}（{p}）{xp}",
 "boundary":"源自《系統漢語》第514部「匚部」（卷八十五 匚）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡514a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡514a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡514a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))