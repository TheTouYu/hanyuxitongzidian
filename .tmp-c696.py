import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FN="【第536部「囊部」】囊＝甲骨文象两头扎起的无底口袋（《廣韻》「袋也」）；转义敛藏（《正字通》「凡蓄藏者皆曰囊」）。辩证《说文》「从㯻省，襄省聲」析形不确，亦为襄、囊相混之因。音源借音：袋盛物鼓出，襄本有肥义，音义可通。"
FC="【第537部「長部」】長＝甲骨文象人长发拄杖之形，表年长（《廣雅》「老也」），所拄杖亦为权杖→首领（《廣雅》「君也」）；转义久远多→长处→增进→抚育；辩证《说文》以拄杖为倒亡，不确；音源借音（抚育义音同「羊」，古長、羊通用）。"
N="字形：古文字字形库未收。"
D=[("囊","náng",FN,"象两头扎起的无底口袋；引申敛藏、装塞。","n「纳弄」取「纳」：袋纳而藏。"),
("囔","nāng",FN,"从口囊聲：小聲說話，嘟囔自語。","n取纳弄：聲纳而弄。"),
("攮","nǎng",FN,"从手囊聲：推攮、刺；又攮包（暗藏）。","n取纳弄：推纳而弄。"),
("灢","nǎng",FN,"从水囊聲：水濁貌（《集韻》）。","n取纳弄：水浊而纳。"),
("齉","nàng",FN,"从鼻囊聲：鼻塞不通、語音不清。","n取纳弄：鼻塞而纳。"),
("欜","náng",FN,"从木囊聲：木名（《集韻》）。","n取纳弄：木实而纳。"),
("㚂","nǎng",FN,"从土囊聲：㚂，土穴／塵起貌。","n取纳弄：土聚而纳。"),
("儾","nàng",FN,"从人囊聲：怯懦、寬緩（《集韻》）。","n取纳弄：人缓而纳。"),
("饢","náng",FN,"从食囊聲：饢，麵餅；又食不飽貌。","n取纳弄：食纳而弄。"),
("韔","chàng",FC,"从韋長聲：《說文》「弓衣也」，藏弓之袋。","ch「刺持」取「持」：弓入袋而持。"),
("棖","chéng",FC,"从木長聲：門兩旁木（門楔）；又觸也。","ch取刺持：木撑而持。"),
("張","zhāng",FC,"从弓長聲：施弓弦也（《說文》），引申張開、陳設、張望。","zh「凿总」取「凿」：弓張而凿。")]
for ch,p,F0,xp,sm in D:
    bn=536 if ch in "囊囔攮灢齉欜㚂儾饢" else 537
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"囊系同取「装、塞、鼓出」一面（囔声、攮推、灢浊、齉塞）；長系同取「长而引張」一面（韔弓衣、棖门楔、張施弦）；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":bn,"name":"囊" if bn==536 else "長"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lnang-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第536－537部（卷八十九 象）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡537a2026-10-24","risk":"low","claims":cl},open(r"intake\20261024-字卡537a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261024-字卡537a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))