import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F="【第580部「麗部」】麗＝象無杈角之鹿（麂），引申配偶、附著、美麗；字族多从麗聲，取「附麗、離散、華美」諸面。"
N="字形：古文字字形库未收。"
D=[("邐","lǐ",F,"从辵麗聲：迤邐（《集韻》），道路曲折連延。","l「拢离」取「离」：路曲而离。"),
("躧","xǐ",F,"从足麗聲：舞履也（《說文》「躧，舞履也」），躧履、躧步。","x「续消」取「续」：步續而消。"),
("孋","lí",F,"从女麗聲：女字（《集韻》），戎狄名；又美。","l取拢离：女美而离。"),
("廲","lí",F,"从广麗聲：廲廔，綺窗（《集韻》），窗欞交疏。","l取拢离：屋列而离。"),
("彲","chī",F,"从鹿麗聲：若龍而黃（《說文》引《周書》），螭之或體。","ch「刺持」取「持」：龍盤而持。"),
("鸝","lí",F,"从鳥麗聲：黃鸝（《集韻》），黃鶯。","l取拢离：鳥鳴而离。"),
("鱺","lí",F,"从魚麗聲：魚名（《集韻》），鰻鱺。","l取拢离：魚伏而离。"),
("㿛","lì",F,"从疒麗聲：癧之或體（《集韻》），瘰癧、惡疾。","l取拢离：疾結而离。"),
("襹","shī",F,"从衣麗聲：襳襹，衣長貌（《集韻》），羽毛衣。","sh「失收」取「收」：衣垂而收。"),
("矖","xǐ",F,"从目麗聲：索視也（《集韻》），視察。","x取续消：目視而消。"),
("灑","sǎ",F,"从水麗聲：洒也（《說文》「灑，汛也」），灑水、散落。","s「失收」取「收」：水散而收。"),
("囇","lì",F,"从日麗聲：曬之或體（《集韻》），日光曝物。","l取拢离：日曝而离。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"麗聲餘字同取「連延、附麗、華美」一面：邐路曲、躧舞履、孋女美、廲綺窗、彲龍、鸝黃鶯、鱺鰻、㿛癧、襹衣長、矖索視、灑水、囇曝；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":580,"name":"麗"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lli2-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第580部「麗部」（卷九十五 離）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
p=r"intake\20261024-字卡580b.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡580b{it}-2026-10-24","risk":"low","claims":cl},open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p,"--format","json")
    if "PLAN_DUPLICATE" not in out:
        print("ok claims",len(cl)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",cl[idx]["title"]); cl.pop(idx)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))