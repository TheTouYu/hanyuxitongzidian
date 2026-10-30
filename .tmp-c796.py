import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F1="【第571部「力部」】力＝耒之初文（曲木加橫木），引申力量、功勞、能力；字族②取「力氣、功效」，③擬聲。"
F2="【第571部「力部」·男支】男＝从田从力（力亦聲），象耒耕；耒耕需成年男子，引申男性、兒子、勝任（男爵）。"
N="字形：古文字字形库未收。"
D=[("劣","liè",F1,"从力从少：弱也（《說文》），力少則弱，引申鄙薄、不足。","l「拢离」取「离」：力少而离。"),
("仂","lè",F1,"从人力聲：數之餘也（《正字通》），稅什一、勤勞。","l取拢离：餘數而离。"),
("㔹","lè",F1,"从十力聲：材十人也（《說文》），材力十倍於人。","l取拢离：力倍而离。"),
("忇","lè",F1,"从心力聲：功大也（《玉篇》），又思也。","l取拢离：心勞而离。"),
("艻","lè",F1,"从艸力聲：蘿艻、香菜（《玉篇》）；又艻木可為柵。","l取拢离：草蔓而离。"),
("牞","jiū",F1,"从牛力聲：牛大力（《玉篇》），古國名。","j「聚决」取「聚」：牛力而决。"),
("劽","liè",F1,"从列力聲：有力也（《集韻》）。","l取拢离：力列而离。"),
("嘞","lei",F1,"从口勒聲：語氣詞（《漢典》），表提醒；又嘮叨。","l取拢离：語緩而离。"),
("叻","lè",F1,"从口力聲：石叻（馬來語，即新加坡），象聲字。","l取拢离：聲促而离。"),
("氻","lè",F1,"从水力聲：泉聲也（《玉篇》），水聲。","l取拢离：泉流而离。"),
("男","nán",F2,"从田从力：丈夫也（《說文》「言男用力于田也」），成年男子；引申兒子、勝任、男爵。","n「纳弄」取「纳」：田力而纳。"),
("莮","nán",F2,"从艸男聲：萓莮（《玉篇》），萱草，即宜男，妊婦佩之求生男。","n取纳弄：草茂而纳。"),
("侽","nán",F2,"从人男聲：男子（《集韻》），亦作男。","n取纳弄：人壯而纳。"),
("娚","nán",F2,"从女男聲：女字（《集韻》），又稱姊妹。","n取纳弄：女婉而纳。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"力部②取「力少、力餘、力倍、力大」之別（劣、仂、㔹、忇、艻、牞、劽）與擬聲（嘞、叻、氻）；男支取「田力所出」（男、莮、侽、娚）；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":571,"name":"力"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lli3-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第571部「力部」（卷九十四 七）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
p=r"intake\20261024-字卡571b.json"
for it in range(8):
    json.dump({"schema_version":1,"intent":f"字卡571b{it}-2026-10-24","risk":"low","claims":cl},open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p,"--format","json")
    if "PLAN_DUPLICATE" not in out:
        print("ok claims",len(cl)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",cl[idx]["title"]); cl.pop(idx)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))