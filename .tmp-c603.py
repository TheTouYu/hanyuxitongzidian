import json,subprocess,os,glob
F="【493 善部】善＝甲骨文象目上有角之形，象意牛羊鹿等有角類動物的頭部；借音字，角狀如「干」，故義音同。本義美好、善良，引申擅長、喜愛。"
F2="【494 旦部】旦＝象太陽剛从海面升起、水裏有倒影之形，象意日初出時（《玉篇》「早也、朝也、曉也」）；借音字，義音从蟬（蟬須待日出羽化，古或以為太陽神）。"
N="字形：古文字字形库未收。"
D=[("善","shàn",F,"本部部首字：有角獸頭→美好、善良、擅長。","sh「失收」取「收」：角收而善。"),
("膳","shàn",F,"从肉善聲：食之精美者，取善之美義。","sh取收：味收而膳。"),
("繕","shàn",F,"从糸善聲：修補使之完善（《說文》「補也」）。","sh取收：綴收而繕。"),
("鱔","shàn",F,"从魚善聲：黃鱔，《正字通》「鱔，俗鱓字」，所从單本同干。","sh取收：體長收曲。"),
("旦","dàn",F2,"本部部首字：日出海面而見倒影→早晨、天明。","d「囤动」取「囤」：日囤於海。"),
("但","dàn",F2,"从人旦聲：本義脫衣露身（通「袒」），引申只、僅。","d取囤：身囤而露。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"善部取「有角獸頭、美善」一面，旦部取「日出見影」一面；形符各定落點。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lco-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第493－494部（卷八十 干）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡494a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡494a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡494a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))