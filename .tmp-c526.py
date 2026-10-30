import json,subprocess,os,glob
F="【434 釆部·番支】番＝簸箕簸扬、筛出杂质（播之初文），字族取「翻动、淘洗、盘绕」诸面。"
N="字形：古文字字形库未收。"
D=[("籓","fān",F,"《说文》「大箕也，从竹潘声，一曰蔽也」——大簸箕；有柄可推弃之器。","f「附分」取「分」：扬而分。"),
("旛","fān",F,"《说文》「幅胡也，从㫃番声」——长条形旗，下垂之幅，翻动如簸。","f取分：旗翻而分。"),
("幡","fān",F,"《说文》「书儿拭觚布也，从巾番声」——学书儿童拭简的布；又旗帜。","f取分：布拭而分。"),
("鱕","fān",F,"《集韵》引《南越志》——鼻有横骨如鐇、缘有锯齿的大鱼（锯鲨类），能使船翻。","f取分：鳍分如锯。"),
("鐇","fán",F,"《集韵》「椎也，一曰广刃斧，一曰铲也」——宽刃大斧。","f取分：斧劈而分。"),
("轓","fān",F,"《集韵》「车蔽」；《广韵》「车大箱也」——车厢两旁障蔽。","f取分：车分左右。"),
("潘","pān",F,"《说文》「淅米汁也，从水番声」——淘米水；又水盘旋曰潘。","p「拼辟」取「辟」：淘而分。"),
("𤄫","fān",F,"《说文》「大波也，从水旛声」——波浪翻涌。","f取分：波分而涌。"),
("鄱","pó",F,"《说文》「鄱阳，豫章县」——今江西鄱阳。","p取辟：地名借声。"),
("鷭","fán",F,"《集韵》「鷭䳇，鸟名，似鹝」——形似鸡、额有红块，栖沼泽。","f取分：额分而赤。"),
("噃","fān",F,"《集韵》「声也」——声音翻动。","f取分：声散而分。"),
("墦","fán",F,"《集韵》「冢也」——坟墓（坟起如翻土）。","f取分：土翻成冢。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取番部「簸扬翻动、淘洗盘绕」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lb9-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第434部「釆部」（卷七十三 釆）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡434c2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡434c.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡434c.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))