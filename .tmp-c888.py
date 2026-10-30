import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
N="字形：古文字字形库未收。"
F="【第592部「冬部」·㐭（嗇）族】㐭＝象禾稭堆積入倉之形（《說文》「穀所振入」），嗇＝从㐭从來（收禾吝惜）；轉義 吝嗇、愛惜；音源同冬。此族取「收倉、牆蔽、懸挂」三面。"
D=[("嗇","sè",F,"从㐭从來：愛濇也（《說文》「愛濇也」），收禾吝惜→吝嗇、節省。","s「失收」取「收」：收而嗇。"),
("穡","sè",F,"从禾嗇聲：穀可收曰穡（《說文》「穀可收曰穡」），收穫、農事。","s取失收：禾收而嗇。"),
("濇","sè",F,"从水嗇聲：不滑也（《說文》「不滑也」），滯澀。","s取失收：水澀而嗇。"),
("薔","qiáng",F,"从艸嗇聲：薔薇（《說文》「薔虞，蓼」；《本草》薔薇），蔓生有刺。","q「亲缺」取「缺」：蔓刺而缺。"),
("蘠","qiáng",F,"从艸牆聲：蘠靡，虋冬也（《說文》），薔薇之苗；麥門冬。","q取亲缺：草蔓而缺。"),
("㱇","xì",F,"从欠嗇聲：悲意（《說文》「悲意」）；又恐懼，「㱇然而駭」。","x「续消」取「续」：悲而续。"),
("牆","qiáng",F,"从嗇爿聲：垣蔽也（《說文》「垣蔽也」），磚石砌成承架房頂、隔內外者（《釋名》「障也」）。","q取亲缺：垣隔而缺。"),
("廧","qiáng",F,"从广牆聲：同牆（《玉篇》「牆垣也，廧同上」）；又與嗇同。","q取亲缺：屋牆而缺。"),
("嬙","qiáng",F,"从女牆省聲：婦官也（《說文新附》），宮廷女官掌器物；又女字。","q取亲缺：女官而缺。"),
("懎","sè",F,"从心嗇聲：恨也（《玉篇》），悲恨、恐懼。","s取失收：恨而嗇。"),
("繬","sè",F,"从糸嗇聲：緙也、縫也（《廣韻》），繩。","s取失收：縫而嗇。"),
("檣","qiáng",F,"从木嗇聲：船檣，帆柱也（《玉篇》），掛帆桅杆，船帆如牆。","q取亲缺：桅立而缺。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"㐭族同取「收倉、牆蔽、懸挂」一面：嗇惜、穡收、濇澀、薔蔓、蘠草、㱇悲、牆垣、廧牆、嬙女官、懎恨、繬縫、檣桅；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":592,"name":"冬"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"ldong3-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第592部「冬部」（卷九十七 殸）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
p=r"intake\20261024-字卡592c.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡592c{it}-2026-10-24","risk":"low","claims":cl},open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p,"--format","json")
    if "PLAN_DUPLICATE" not in out:
        print("ok claims",len(cl)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",cl[idx]["title"]); cl.pop(idx)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))