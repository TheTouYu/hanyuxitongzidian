import json,subprocess,os,glob
F="【477 侯部】侯＝甲骨文从厂从矢（厂指石，矢指箭），象用石塊製成的箭鏃，是「鍭」的初文；由箭鏃為箭之核心，引申君主、尊稱、美。音源借「猴」為聲——成年獼猴有頰囊，鼓如箭鏃。"
N="字形：古文字字形库未收。"
D=[("侯","hóu",F,"本部部首字：石箭鏃→箭之核心→君主、君侯、美。","h「豁活」取「豁」：矢發而豁。"),
("候","hòu",F,"从人侯聲：伺望、等候；引申時候、氣候、徵候。","h取豁：伺望而豁。"),
("喉","hóu",F,"从口侯聲：咽喉，聲氣出入之要道，取箭鏃當中之位。","h取豁：氣自喉豁。"),
("猴","hóu",F,"从犬侯聲：獼猴；其頰囊鼓如箭鏃，故侯為聲。","h取豁：猴躍而豁。"),
("堠","hòu",F,"从土侯聲：記里程的土堆，又斥堠（瞭望敵情）。","h取豁：土堆望豁。"),
("鍭","hóu",F,"从金侯聲：《說文》「矢金鏃翦羽」，金屬箭鏃即侯之初文本義。","h取豁：金鏃破豁。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取侯部「箭鏃居中、頰囊鼓起」两面：口取要道，人取伺望，土取標記，金取本義。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lce-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第477部侯部（卷七十八 夒）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡477a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡477a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡477a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))