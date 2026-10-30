import json,subprocess,os,glob
F="【427 聿部】聿＝从又持半竹，象手持竹作工具（书写是其一种，兼可作刷、作箫、作篙、作箸）；分化出者、晝、畫、肅、肁、盡诸字。转义：竹器轻便→轻捷；书写→讲述、依循。辨证：𦘒、聿本一字，《说文》「从𦘒一聲」析形不确。音源：源自竹笔书写声。"
N="字形：古文字字形库未收。"
D=[("聿","yù","从又持半竹，象手持竹为书写之具（笔之初文）；转义轻捷、讲述、依循。","y「柔锐」取「锐」：竹笔尖利而书。"),
("䢖","yù","《玉篇》「分布也，又行貌」——分布、行走之状。","y取锐：行而分布。"),
("冿","jiān","《字汇补》「进也」；《篇海》「志也，息进也」——上进。","j「聚决」取「决」：决然而进。"),
("𨁸","lù","《集韵》「䠈𨁸，不进」，走路摇摆不进；又跛足。","l「拢离」取「离」：步散而离。"),
("𠜈","lǜ","《篇海类编》音绿；刀刻之字，其义未详。","l取离：刀离木而刻。"),
("𦘓","yì","《集韵》「勩，劳也」——劳苦（《诗》「莫知我勩」）。","y取锐：劳作磨锐。"),
("䋖","yù","《玉篇》「长貌」，《篇海》「长衣貌」——细长。","y取锐：丝长而尖细。"),
("銉","yù","《集韵》「针也」；sì 古同肆（编悬乐器，钟十六枚为一肆）。","y取锐：针尖锐利。"),
("茟","yù","《广雅》「藜也」——灰菜；wěi 通芛，草木花初生。","y取锐：草尖初生。"),
("𥱂","nú","《字汇补》「机𥱂」——织机部件。","n「纳弄」取「纳」：竹受纳入机。")]
for ch,p,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取聿「手持竹笔」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"yb-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第427部「聿部」（卷七十一 聿）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡427a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡427a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡427a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))