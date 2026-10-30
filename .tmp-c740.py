import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FH="【第554部「𤇾部」（熒省）】𤇾＝「熒」省去下火，甲骨文从宀內有火（屋下燈燭之光）；字族取「小而光亮、環繞、壘土、勞作、花榮」諸面。"
N="字形：古文字字形库未收。"
D=[("熒","yíng",FH,"从焱冂（宀内火）：屋下燈燭之光（《說文》「屋下燈燭之光」），引申閃爍、眩惑、螢火。","y 喻母「续消」取「续」：光续而消。"),
("螢","yíng",FH,"从虫熒省聲：螢火蟲（《字彙》「蟲名」）。","y取续消：火续而消。"),
("瑩","yíng",FH,"从玉熒省聲：玉色（《說文》「玉色」），光潔。","y取续消：玉光而续。"),
("營","yíng",FH,"从宮熒省聲：市居也（《說文》「市居也」），四周壘土為營。","y取续消：壘而续。"),
("縈","yíng",FH,"从糸熒省聲：收捲也（《說文》「收捲也」），縈繞。","y取续消：絲绕而续。"),
("塋","yíng",FH,"从土熒省聲：墓也（《說文》「墓也」），墓地。","y取续消：土聚而续。"),
("榮","róng",FH,"从木𤇾聲：桐木也（《說文》「桐木也」），引申花榮、榮耀。","r「柔锐」取「柔」：木柔而锐。"),
("勞","láo",FH,"从力𤇾聲：劇也（《說文》「劇也」），用力辛苦。","l「拢离」取「拢」：力拢而離。"),
("鶯","yīng",FH,"从鳥榮省聲：鳥也（《說文》引《詩》「有鶯其羽」），黃鸝（嘴紅如燭）。","y取续消：鳴续而消。"),
("謍","yíng",FH,"从言熒省聲：小聲也（《說文》引《詩》「謍謍青蠅」）。","y取续消：聲小而续。"),
("鎣","yíng",FH,"从金熒省聲：器也（《說文》「器也」），磨拭使光。","y取续消：磨光而续。"),
("禜","yíng",FH,"从示榮省聲：設綿蕝為營（《說文》），禳災之祭。","y取续消：祭续而消。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"𤇾系同取「屋下小火、光小而續」一面：熒燭光、螢火、瑩玉光、營壘、縈繞、塋墓、榮花、勞力、鶯羽、謍聲、鎣磨、禜祭；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":554,"name":"𤇾"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lying-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第554部「𤇾部」（卷九十一 火）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡554a2026-10-24","risk":"low","claims":cl},open(r"intake\20261024-字卡554a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261024-字卡554a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))