import json,subprocess,os,glob
F="【479 爰部】爰＝甲骨文與「寽」形近，兩手各持「一」的一端，象以藤狀物相牽拉；金文或改「一」為「帀」（倒生），上手下手分指俯拉與攀援。轉義為援助、又作虛詞「為、于、曰」。音源借猿善攀援為聲（古袁、爰通用）。"
N="字形：古文字字形库未收。"
D=[("爰","yuán",F,"本部部首字：兩手牽藤相引→攀援、援助、於是。","y「续消」取「续」：牽引相續。"),
("援","yuán",F,"从手爰聲：《說文》「引也」，攀引、援救、援引。","y取续：手引相續。"),
("媛","yuán",F,"从女爰聲：美女，《詩》「邦之媛也」。","y取续：女美相牽。"),
("緩","huǎn",F,"从糸爰聲：繩鬆則緩，引申舒緩、寬緩。","h「豁活」取「豁」：鬆而豁。"),
("暖","nuǎn",F,"从日爰聲：日氣溫和，暖如相援而近。","n「纳弄」取「纳」：日氣內納。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取爰部「牽引相助、柔緩相續」两面：手引、女美、絲緩、日暖各定其一。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lcg-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第479部爰部（卷七十八 夒）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡479a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡479a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡479a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))