import json,subprocess,os,glob
G="【471 鬼部】鬼＝从甶（面具）从人，面目不可辨，表死者魂魄（鬼之言歸也）；音如蛙鳴。本部诸字皆由「魂魄—精怪—高大可畏」三面孳乳。"
N="字形：古文字字形库未收。"
D=[("魂","hún",G,"从鬼云声：《說文》「陽气也」，魂為陽神，遊於天。","h「豁活」取「活」：氣動而活。"),
("魄","pò",G,"从鬼白声：《說文》「陰神也」，魄為陰神，附於形。","p「拼辟」取「辟」：附形而辟。"),
("魏","wèi",G,"从鬼委声：本義魏然高大，引申魏國；今作姓。","w「蒙末」取「蒙」：蒙然高大。"),
("巍","wēi",G,"从山魏声：山高巍峩，取魏之高大。","w取蒙：山蒙而高。"),
("愧","kuì",G,"从女鬼声：《說文》「慙也」，愧怍、惭愧。","k「口控」取「控」：心愧受控。"),
("魅","mèi",G,"从鬼未声：《說文》「老物精也」，魑魅、魅惑。","m「蒙末」取「末」：精末而魅。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取鬼部「陽魂／陰魄／高大／精怪」四面，形符各定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lbz-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第471部鬼部（卷七十七 蛙）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡471b2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡471b.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡471b.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))