import json,subprocess,os,glob
F="【463 又部·余支】又部末诸字，多取「手持、器用、声貌」之细义：𥁓为舀水小瓯，醢为盛于瓯中的肉酱，𩑲为头颤之疾；喐、哊、詴皆口出声；䳑、䒴以鸟与草为名。"
N="字形：古文字字形库未收。"
D=[("𥁓","yòu",F,"从皿右声——《说文》「䀁，小甌也」，舀水器，有柄如手。","y「柔锐」取「柔」：器小而柔。"),
("醢","hǎi",F,"从酉𥁓——肉酱，盛于瓯器；甲骨文又象人置臼中捣，指酷刑。","h「豁活」取「活」：酱酿而活。"),
("𩑲","yòu",F,"从頁又声——颤抖之疾，头摇，《字彙》「顫疾」。","y取柔：头摇而柔。"),
("喐","yù",F,"从口有声——《集韵》「㖪，聲也」，或从郁，状声。","y取柔：声出而柔。"),
("哊","yòu",F,"从口有声——《玉篇》「吐也」，《广韵》「吐聲」。","y取柔：吐声而柔。"),
("詴","wēi",F,"从言有声——《玉篇》「呼人也」，《集韵》「呼聲」。","w「蒙末」取「末」：呼声而末。"),
("㤑","yōu",F,"从心右声——《正字通》「俗憂字」，忧之俗体。","y取柔：忧而柔。"),
("𩲾","yù",F,"从鬼有声——《字彙》「鬼皃」，鬼之状。","y取柔：鬼貌而柔。"),
("䳑","yǒu",F,"从鳥有声——《玉篇》「白鵫也」，白鹇。","y取柔：鸟白而柔。"),
("䒴","yǒu",F,"从艸有声——《集韵》「艸也」，草名。","y取柔：草柔而柔。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同为又部之细义，形符各定落点：皿受器，酉受酱，頁受颤，口与言受声，鳥与艸受名。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lbw-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第463部又部（卷七十六 又）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡463d2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡463d.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡463d.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))