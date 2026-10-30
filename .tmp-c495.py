import json,subprocess,os,glob
B="【421 革部】革＝甲骨文象剖剥下来摊开的整张兽皮（头、身、尾相连），引申去毛、更改、革除、急；又代指皮制品（辔首、韁绳、盾、兵革）、老迈（皮枯皱）、翅膀（《诗》「如鸟斯革」）。音源：借音字，由兵革防御之义而义音同「戒」。字族衍义：①皮带之用→捆缚、蒙鼓、勒马 ②整治皮革→改变、刻镂、火燎、碾压 ③皮革之状→宽扁薄。"
N="字形：古文字字形库未收。"
D=[("𪔨","gǔ","鼓之或体——用皮蒙鼓（《说文》「郭也，春分之音」）。","g「隔估」取「隔」：皮隔而鼓。"),
("䩧","xiè","《玉篇》「急系也」——用皮绳捆缚。","x「续消」取「续」：绳续而缚。"),
("𢃲","è","《玉篇》「紩也，一作缂」——缝补。","h「豁活」取「活」：线活而缝。"),
("𩩸","lé","即「勒」——马头络衔；有衔曰勒，无曰羁；又抑勒、刊也。","l「拢离」取「拢」：勒以拢马。"),
("㮖","jiá","《集韵》「鼓也」；《广雅》「攱也」——搁置。","j「聚决」取「决」：鼓决而鸣。"),
("諽","gé","《说文》「饰也，一曰更也」——整治、改变；又谨也。","g「隔估」取「隔」：治革而隔旧。"),
("𢯹","gé","《玉篇》「改也」；《集韵》「改治也」——整治皮革。","g「隔估」取「隔」：手治而改。"),
("緙","kè","《广韵》「紩也，又织纬」——刻丝，花纹如刻镂而成。","k「口控」取「控」：丝控如刻。"),
("煂","hè","《集韵》「烧也」——火燎去毛。","h「豁活」取「豁」：火豁而燎。"),
("𨍝","gé","《释名》「复也，重复非一之言」；同「轹」，车轮碾压。","g「隔估」取「隔」：轮隔而碾。"),
("𦑜","gé","《说文》「翅也」；《玉篇》「羽也」——皮革展开如翼（《诗》「如鸟斯革」）。","g「隔估」取「隔」：翼隔而张。"),
("䐙","gé","《集韵》「膈，肓也」——胸膈，分隔胸腹两腔的膜状肌肉。","g「隔估」取「隔」：膈以隔腔。")]
for ch,p,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":B,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取革部「整治兽皮——去毛／改换／绷张」一面，形符各定其落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("写卡",len(D))
cl=[{"id":f"bdc-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡）","statement":f"{ch}（{p}）：{xp}",
"boundary":"源自《系統漢語》第421部「革部」（卷七十 亥）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡421b2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡421b.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡421b.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))