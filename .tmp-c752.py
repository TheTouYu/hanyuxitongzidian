import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FH="【第556部「辛部」】辛（䇂）＝象小刻刀，用於刻字紋身；部内四系 言（直言）／𣓀（親，至）／新（析木）／豙（豕怒），皆承刻刀之鋒。"
N="字形：古文字字形库未收。"
D=[("霅","zhá",FH,"从雨言聲：霅霅，震電皃（《說文》「霅霅，震電皃」）。","zh「凿总」取「凿」：電凿而總。"),
("圁","yín",FH,"从囗言聲：圁水，地名（《說文》「圁水」）。","y「续消」取「续」：水绕而续。"),
("琂","yán",FH,"从玉言聲：石之似玉者（《說文》「石之似玉者」）。","y取续消：玉润而续。"),
("䇾","yán",FH,"从竹言聲：大簫也（《說文》「大簫也」），管樂器。","y取续消：竹聲而续。"),
("狺","yín",FH,"从犬言聲：犬吠聲（《說文》「犬吠聲」），狺狺。","y取续消：吠续而消。"),
("瘖","yīn",FH,"从疒音聲：不能言也（《說文》「不能言也」），失聲。","y取续消：聲塞而续。"),
("寴","qīn",FH,"从宀親聲：至也（《說文》「至也」），同「親」，親密。","q「亲缺」取「亲」：屋下而亲。"),
("瀙","qìn",FH,"从水親聲：瀙水（《說文》「瀙水」），水名。","q取亲缺：水亲而缺。"),
("襯","chèn",FH,"从衣親聲：近身衣也（《說文》「近身衣也」），襯衣、襯托。","ch「刺持」取「持」：衣近而持。"),
("嚫","chèn",FH,"从口親聲：嚫施（《集韻》），梵語布施。","ch取刺持：口施而持。"),
("豙","yì",FH,"从豕从辛：豕怒毛豎也（《說文》「豕怒毛豎」），一曰殘艾。","y取续消：豕怒而续。"),
("顡","ài",FH,"从頁豙聲：癡不聰明也（《說文》「癡不聰明也」）。","ai「豁活」取「活」：面癡而活。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"辛部言／親／豙系同取「刻刀之鋒、直言、相親、怒張」一面：霅震電、圁水、琂玉、䇾簫、狺吠、瘖失聲、寴親、瀙水、襯衣、嚫施、豙豕怒、顡癡；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":556,"name":"辛"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lxin2-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第556部「辛部」（卷九十二 辛）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡556b2026-10-24","risk":"low","claims":cl},open(r"intake\20261024-字卡556b.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261024-字卡556b.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))