import json,subprocess,os,glob
F="【494 旦部余支】旦部除「日出見影」一系外，尚有从倝（旗幟輝煌）一支：倝本象「中」形旗幟，西周晚期方框演作旦而得聲。"
N="字形：古文字字形库未收。"
D=[("担","dān",F,"从手旦聲：以肩荷物（本作儋、擔），引申承當。","d「囤动」取「囤」：物囤於肩。"),
("倝","gàn",F,"本部内字根：依西周金文與「雗」甲骨文，本同「㫃」，象「中」形旗幟；方框演作旦，象意旗幟輝煌，或指九旗之「大常」（日月為常）。","g「隔估」取「隔」：旗隔風而揚。"),
("翰","hàn",F,"从羽倝聲：赤羽、高飛之羽，引申文翰、翰墨。","h「豁活」取「豁」：羽張而豁。"),
("雗","hàn",F,"从隹倝聲：白雉（《爾雅》「雗雉」），取倝之聲。","h取豁：雉羽開豁。"),
("茬","chá",F,"从木旦聲：樹木砍伐後留下的殘樁（《集韻》「邪斫木也」）。","ch「刺持」取「刺」：刀刺留茬。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取旦部「日出見影、旗幟輝煌」兩面：手取其荷，羽取其飛，木取其樁。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lcp-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第494部旦部（卷八十 干）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡494b2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡494b.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡494b.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))