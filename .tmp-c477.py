import json,subprocess,os,glob
B_SHOU="【414 时部（原属它部，从日从之）】时＝甲骨文及春秋金文本从日从之：「日」指太阳，「之」指足迹，太阳的足迹就是太阳照射物体所形成的影子，古人据影子的长短以知时辰，故象意时辰；或从「寺」，取圭表直立测影。转义：由圭表的直立之状，引申指笔直竖立；不同时令气候物候随之变化，故引申指形势、机会、适时（《释名》「时，期也，物之生死各应节期而至也」）。字族衍义：多指应时发生。"
B_DE="【415 得部（原属它部，从又从贝）】得＝从又从贝，象意拾取贝壳（或从「彳」）；「贝」本指钱贝，故也指获得钱财（《说文》「行有所得也」）。转义：拾取贝壳时会停下脚步，故引申指停止（碍，《集韵》「碍，止也」）。辯證：小篆把「贝」写得像「见」，故《说文》「䙷，取也，从见从寸」析形不确。音源：借音字，因有碍止义而义音同「寺」。字族衍义：①指拾贝时的样子，表示走走停停。"
N="字形：古文字字形库未收。"
D=[
("时","shí",B_SHOU,"甲骨文从日从之——太阳的足迹即影子，据此知时；或从寺，取圭表直立。","应时族之日：以「日」定其时，日影即时刻。","sh「失收」取「收」：影收而时定。"),
("塒","zhì",B_SHOU,"《说文》「鸡栖垣为塒」——鸡窝；鸡能报时，故从时。","应时族之土：以「土」定其处，鸡栖而知时。","zh「凿总」取「总」：鸡总归于埘。"),
("蒔","shì",B_SHOU,"《说文》「更别种」——移栽；《广雅》「立也」。","应时族之艸：以「艸」定其物，移栽须应时。","sh「失收」取「收」：秧收而种。"),
("榯","shí",B_SHOU,"《玉篇》「树木立也」；《类篇》「落榯，持门枢」——应时而或关或开。","应时族之木：以「木」定其物，立木如圭表。","sh「失收」取「收」：木收而立。"),
("𥻵","cí",B_SHOU,"福建风俗逢年过节所吃的稻饼（餈之俗字），冬至收𥻵泥于门前，应时节之意。","应时族之米：以「米」定其物，节令之食。","c「刺持」取「持」：持米为饼。"),
("鰣","shí",B_SHOU,"《正韵》「鱼名，似鲂肥美，江东四月有之」——鲥鱼，春夏之交溯河而上，应时而来。","应时族之魚：以「魚」定其物，应时洄游。","sh「失收」取「收」：鱼收于时。"),
("得","dé",B_DE,"《说文》「行有所得也」——拾取贝壳而得财。","拾贝族①之彳：以「彳」定其行，行而拾得。","d「囤动」取「囤」：囤步而拾。"),
("㧹","tè",B_DE,"《玉篇》「拳打」——取拳状如贝之意。","拾贝族①之手：以「手」定其动，拳如贝而击。","t「涂突」取「突」：突出而击。"),
("䅞","nè",B_DE,"《集韵》「谷穰也」——谷物脱粒后所剩的茎秆、稃，形如贝壳。","拾贝族①之禾：以「禾」定其物，稃如贝。","n「纳弄」取「纳」：纳壳于场。"),
("䎪","nè",B_DE,"《字汇》「谷䎪」；《正字通》「当是槌谷具」——打谷的槌。","拾贝族①之耒：以「耒」定其器，槌谷如拾贝。","n「纳弄」取「弄」：弄谷而脱。"),
("䚟","dǎi",B_DE,"《玉篇》「角也」；《字汇》「角心」——与好歹之歹同。","拾贝族①之角：以「角」定其物，角心如贝。","d「囤动」取「动」：角动而触。"),
("㕌","ài",B_DE,"《玉篇》「张幕也，又石名」；《正字通》「㝵字之讹」。","碍止族之阜：以「阜」定其地，张幕如碍。","零声母不系（今读 ài 影母字，不列七组）。"),
]
def card(ch,p,BEN,desc,xp,sm):
    return {"char":ch,"pinyin":p,"bus":[],"sections":[
      {"key":"bengen","label":"字根本义","text":BEN,"cites":[]},
      {"key":"zigen","label":"字形","text":N,"cites":[]},
      {"key":"xingpang","label":"形旁声旁","text":desc,"cites":[]},
      {"key":"hengxiang","label":"横向对照","text":"同取本部「应时而生／拾取而止」一面，形符各定其落点；故声符给义、形符定落点。","cites":[]},
      {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]}
for t in D:
    ch,p,BEN,desc,xp,sm=t
    json.dump(card(ch,p,BEN,desc,xp,sm),open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("写卡",len(D))
cl=[{"id":f"bdc-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{t[0]}（字卡）",
   "statement":f"{t[0]}（{t[1]}）：{t[3]}","boundary":("源自《系統漢語》第414部「时部」（卷六十七 足）；字卡五步规程。" if t[2]==B_SHOU else "源自《系統漢語》第415部「得部」（卷六十七 足）；字卡五步规程。"),
   "permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,t in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡414时415得2026-10-23","risk":"low","claims":cl},
          open(r"intake\20261023-字卡414时415得.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡414时415得.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))