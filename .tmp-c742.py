import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FH="【第555部「樂部」】樂＝甲骨文从絲从木，象意有二：絲弦繃於木（琴瑟，yuè）或產絲之柞樹（櫟之初文，lì）；字族取「治病、光潔、堅硬、車碾」諸面。"
N="字形：古文字字形库未收。"
D=[("樂","lè/yuè",FH,"从絲从木：絲弦繃木為琴瑟（羅振玉說），五聲八音總名；又指柞樹（櫟之初文）。","l「拢离」取「拢」：弦拢而離。"),
("藥","yào",FH,"从艸樂聲：治病艸（《說文》「治病艸」），藥物。","y「续消」取「续」：艸续而消。"),
("𤻲","liáo",FH,"从疒樂聲：治也（《說文》「治也」），即療。","l取拢离：病拢而離。"),
("嚛","hù",FH,"从口樂聲：食辛也（《說文》「食辛也」）。","h「豁活」取「豁」：辛而豁。"),
("纅","yào",FH,"从糸樂聲：絲色也（《說文》「絲色也」）。","y取续消：絲色而续。"),
("瓅","lì",FH,"从玉樂聲：玉光（《集韻》），玓瓅。","l取拢离：玉光而離。"),
("鑠","shuò",FH,"从金樂聲：銷金也（《說文》「銷金也」），光明、閃爍。","sh「失收」取「失」：金銷而收。"),
("爍","shuò",FH,"从火樂聲：灼爍，光也（《說文》「灼爍，光也」）。","sh取失收：火灼而收。"),
("皪","lì",FH,"从白樂聲：白皃（《集韻》），鮮明。","l取拢离：白而離。"),
("櫟","lì",FH,"从木樂聲：木也（《說文》「木也」），柞樹、橡實。","l取拢离：木坚而離。"),
("礫","lì",FH,"从石樂聲：小石也（《說文》「小石也」）。","l取拢离：石小而離。"),
("轢","lì",FH,"从車樂聲：車所踐也（《說文》「車所踐也」），碾壓。","l取拢离：車碾而離。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"樂系同取「木上絲弦、光潔堅硬」一面：藥治病、𤻲治、嚛辛、纅絲色、瓅玉光、鑠銷金、爍火、皪白、櫟柞、礫小石、轢車碾；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":555,"name":"樂"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lyue-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第555部「樂部」（卷九十一 火）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡555a2026-10-24","risk":"low","claims":cl},open(r"intake\20261024-字卡555a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261024-字卡555a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))