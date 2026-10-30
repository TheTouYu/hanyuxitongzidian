import json,subprocess,os,glob
F="【475 毳部】毳＝从毛的三叠，毛指动物毛发，三叠表示极致；象意有三：毛之极细、绒毛之密、细毛所成之毳衣。轉義由毛之极细引申脆弱、柔美。音源借「脆」（細弱義同）。"
N="字形：古文字字形库未收。"
D=[("毳","cuì",F,"本部部首字：三毛重叠→细绒毛、毳衣、毳毛；引申脆弱柔美。","c「刺持」取「持」：毛密相持。"),
("脆","cuì",F,"从肉毳省聲：《說文》「小耎易斷也」，脆嫩、脆弱。","c取持：肉嫩易断。"),
("膬","cuì",F,"从肉毳聲：《說文》「耎易破也」，与脆同。","c取持：肉耎而膬。"),
("橇","qiāo",F,"从木毳聲：泥行乘橇，木板滑行於泥雪之上。","q「亲缺」取「缺」：泥行而缺。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取毳部「毛极细、耎易破」两面：肉取其耎，木取其滑行。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lcc-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第475部毳部（卷七十七 蛙）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡475a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡475a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡475a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))