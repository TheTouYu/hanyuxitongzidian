import json,subprocess,os,glob
F="【469 龜部】龜＝象烏龜形；古人視龜為靈物，甲蟲三百六十而神龜為長，背陰向陽、上高象天、下平法地；龜殼曾作貨幣，故引申貨幣、進獻。音源借音（龜不叫），以其背圓，義音同「規」。"
W="【470 瓦部】瓦＝象兩片瓦一覆一仰相扣之形，本指蓋屋之瓦；轉指凡陶器已燒之總名。音源字，取蓋瓦相擊之聲；其形半圓，故義音同「圭」。"
N="字形：古文字字形库未收。"
D=[("龜","guī",F,"本部部首字：靈龜→貨幣、進獻；龜甲亦占卜之具。","g「隔估」取「隔」：甲自相隔。"),
("瓦","wǎ",W,"本部部首字：屋瓦→陶器總名。","w「蒙末」取「蒙」：覆而相蒙。"),
("瓶","píng",W,"从缶并声（瓦部字）：汲水器，小口大腹，取并合之意。","p「拼辟」取「拼」：拼合而瓶。"),
("甌","ōu",W,"从瓦區声：小盆，取區藏之意。","k「口控」取「控」：器小而受控。"),
("瓴","líng",W,"从瓦令声：盛水瓶，屋上仰瓦承溜亦曰瓴。","l「拢离」取「拢」：聚水而拢。"),
("瓮","wèng",W,"从瓦公声：大腹敛口陶器，取公（中空）之意。","w取蒙：中空而蒙。"),
("瓷","cí",W,"从瓦次声：以高嶺土燒成，堅致似瓦而細。","c「刺持」取「持」：持土成器。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取瓦部「覆仰相扣、中空受物」两面：缶瓦旁定陶器，令公次并各定其用。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lbx-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第469－470部（卷七十七 蛙）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡470a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡470a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡470a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))