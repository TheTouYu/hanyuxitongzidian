import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F="【第570部「丯部」】丯＝「七」的上下各刻一橫，表鍥刻多道紋路（《六書故》「丯即㓞字，以丯為聲」）；音源為刻畫聲；字族 㓞（刀刻）／害（割之初文）／憲／戟。"
N="字形：古文字字形库未收。"
D=[("丯","jiè",F,"从七上下各刻一橫：鍥刻紋路之形（《釋名》「契，刻也」），刻識其數。","j「聚决」取「聚」：刻聚而决。"),
("𡕗","hài",F,"从夂丯聲：相遮要害也（《說文》），要害處立柵欄為障。","h「豁活」取「豁」：遮隔而豁。"),
("砉","xū",F,"从石丯聲：物相離聲（《廣韻》「砉然」），刻石之聲→迅疾、豁然。","x「续消」取「续」：聲裂而续。"),
("湱","huò",F,"从水丯聲：漰湱大波相激聲（《集韻》）。","h取豁活：波激而豁。"),
("騞","huō",F,"从馬丯聲：刀解牛聲（《集韻》），馬行疾貌。","h取豁活：解裂而豁。"),
("剨","huò",F,"从刀丯聲：破聲（《集韻》）。","h取豁活：刀破而豁。"),
("𢝇","huò",F,"从心丯聲：心驚皃（《集韻》），聞裂聲而驚。","h取豁活：心驚而豁。"),
("𤊴","huò",F,"从火丯聲：火光（《集韻》），刻石火星四濺。","h取豁活：火迸而豁。"),
("㓞","qià",F,"从刀丯聲：巧㓞也（《說文》「巧㓞也」），象用刀刻畫。","q「亲缺」取「亲」：刀刻而亲。"),
("契","qì",F,"从大从㓞：大約也（《說文》），刻木為券、分持為憑；引申契合、割斷。","q取亲缺：刻合而亲。"),
("鍥","qiè",F,"从金契聲：鐮也（《說文》），又刻也、斷絕。","q取亲缺：刃割而亲。"),
("挈","qiè",F,"从手㓞聲：縣持也（《說文》「縣持也」），提挈、牽引。","q取亲缺：手提而亲。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"丯部同取「刻裂之聲、割刻之器」一面：砉砉裂聲、湱波激、騞解牛、剨破、𢝇心驚、𤊴火星、㓞刀刻、契刻券、鍥鐮、挈提；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":570,"name":"丯"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"ljie-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第570部「丯部」（卷九十四 七）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
p=r"intake\20261024-字卡570a.json"
for it in range(8):
    json.dump({"schema_version":1,"intent":f"字卡570a{it}-2026-10-24","risk":"low","claims":cl},open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p,"--format","json")
    if "PLAN_DUPLICATE" not in out:
        print("ok claims",len(cl)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",cl[idx]["title"]); cl.pop(idx)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))