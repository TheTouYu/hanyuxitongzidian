import json,subprocess,os,glob
W="【470 瓦部】瓦＝象兩片瓦一覆一仰相扣之形，本指屋瓦，轉指陶器已燒之總名；音源取蓋瓦相擊之聲，形半圓故義音同「圭」。"
G="【471 鬼部】鬼＝甲骨文从甶（面具）从人，象人戴面具之形；由面目不可辨而表示死者魂魄（鬼之言歸也）；音如蛙鳴（蛙無項，如戴面具），民間巫術以蛙充魂。"
N="字形：古文字字形库未收。"
D=[("甄","zhēn",W,"从瓦垔声：《說文》「陶也」，陶人作瓦器；引申甄别、选拔。","zh「凿总」取「凿」：治土成器。"),
("甑","zèng",W,"从瓦曾声：蒸飯瓦器，甑算其底。","z取凿：蒸氣穿孔。"),
("甓","pì",W,"从瓦辟声：《說文》「瓴甓也」，砖。","b「闭剥」取「闭」：砖合而闭。"),
("㽉","hǎn",W,"从瓦臽声：大盆，可盛水。","h「豁活」取「豁」：中空而豁。"),
("鬼","guǐ",G,"本部部首字：戴面具者→死後魂魄、鬼方；轉指機靈、詭異。","g「隔估」取「隔」：隔於人鬼。"),
("畏","wèi",G,"从攴从鬼：擊打亡魂——雖失活性仍具能力，故懼；引申歸罪、威脅。","w「蒙末」取「蒙」：蒙面可畏。"),
("魁","kuí",G,"从鬼斗声：羹斗之大者，引申首領、魁偉、魁星。","k「口控」取「控」：首控眾。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取本部「覆扣成器／面具不可辨」两面：瓦旁定陶器，鬼旁定魂魄可畏。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lby-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第470－471部（卷七十七 蛙）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡471a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡471a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡471a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))