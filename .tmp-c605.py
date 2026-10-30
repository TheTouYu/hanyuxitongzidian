import json,subprocess,os,glob
F="【498 爭部】爭＝甲骨文从兩「又」抓住「凵」的兩邊：凵象筐或器皿，又指手，象意兩人爭搶一器物；金文凵或演作力，見雙方用力拉扯。本義爭奪（《說文》「引也」），轉義辯論、爭執、競爭。"
N="字形：古文字字形库未收。"
D=[("爭","zhēng",F,"本部部首字：兩手爭一器→爭奪、爭執、競爭。","zh「凿总」取「凿」：手凿而奪。"),
("靜","jìng",F,"从青爭聲：《說文》「審也」，丹青明審故為靜；引申安靜。","j「聚决」取「聚」：青聚而審。"),
("淨","jìng",F,"从水爭聲：清潔（《說文》「魯北城門池也」，借為潔淨）。","j取聚：水聚而清。"),
("箏","zhēng",F,"从竹爭聲：弦樂器，取爭之聲。","zh取凿：弦張而鏘。"),
("諍","zhèng",F,"从言爭聲：直言諫止（《廣韻》「諫諍也，止也」）。","zh取凿：言直如凿。"),
("睜","zhēng",F,"从目爭聲：張目直視。","zh取凿：目張而銳。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取爭部「兩手爭器」一面：青取其審，水取其潔，言取其直。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lcq-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第498部爭部（卷八十一 釘）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡498a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡498a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡498a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["hash"] if False else json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))