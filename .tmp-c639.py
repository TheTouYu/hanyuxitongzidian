import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FC="【第522部「刅部」】刅＝西周金文象枝葉對生之形，為「荊」之初文；枝條柔韌可編可鞭→懲罰、創傷；音源義音同「良」。"
FJ="【第523部「㓝部」】㓝＝从井从刅，象荊條編結（→創造）或抽打傷痕（→刑罰）；「荊、刱、㓝、刑」本同源。"
N="字形：古文字字形库未收。"
D=[("𨎛","liáng",FC,"从車梁省聲：車梁（《集韻》）。","l「拢离」取「拢」：車木攏。"),
("墚","liáng",FC,"从土梁省聲：黃土高原條狀嶺岡（《漢典》）。","l取拢离：土岡而離。"),
("簗","zhù",FC,"从竹梁省聲：築之訛；疑為荊條編的魚簍，魚入而不能出。","zh「凿总」取「凿」：編竹而總。"),
("𨄈","liáng",FC,"从足梁聲：跳𨄈，走也（《集韻》）。","l取拢离：足跳而離。"),
("粱","liáng",FC,"从米梁省聲：似粟而大（《說文》「米名也」）。","l取拢离：米粒攏聚。"),
("䘐","nǜ",FC,"从血从刅：衄之或作，鼻出血（《正字通》）。","n「纳弄」取「纳」：血納而出。"),
("𢞤","nì",FC,"从心刅聲：同惄，心之飢、憂思（《廣韻》）。","n取纳弄：憂納於心。"),
("𠛂","chuāng",FC,"从刀从刅：創傷（《集韻》「刅，《說文》傷也」）。","ch「刺持」取「刺」：刀刺而傷。"),
("侀","xíng",FJ,"从人刑聲：成也，即「形」字（《廣韻》）。","x「续消」取「续」：人形成而續。"),
("娙","xíng",FJ,"从女刑聲：好也，女身長謂之娙（《集韻》）。","x取续消：女長而續。"),
("㭢","xīn",FJ,"从木刑聲：小几（《字彙》「机也」）。","x取续消：木器而續。"),
("𤏾","zhēng",FJ,"从火刑聲：煮魚煎肉曰𦙫，肉上劃井字以便入味（《集韻》）。","zh「凿总」取「凿」：劃井而煎。"),
("𧨘","xíng",FJ,"从言刑聲：𧨘笑，同「形笑」，即嘲笑。","x取续消：言笑而續。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同卷兩部同源：梁支取「橋梁樑木／穀米／創傷」（𨎛／墚／簗／𨄈／粱／䘐／𢞤／𠛂）、㓝支取「編結成形／抽打入味」（侀／娙／㭢／𤏾／𧨘）；只列本部字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":522 if F0 is FC else 523,"name":"刅" if F0 is FC else "㓝"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lchuangb-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}（{p}）{xp}",
 "boundary":"源自《系統漢語》第522－523部（卷八十六 良）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡522b2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡522b.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡522b.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))