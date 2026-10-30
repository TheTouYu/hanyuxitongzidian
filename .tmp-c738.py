import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FH="【第553部「巤部」】巤＝从毛从㲋（獸足），象獸毛長而散（《說文》「毛巤也」），獵之初文；字族取「長毛、田獵、腊祭、纏繞、踐越」諸面。"
N="字形：古文字字形库未收。"
D=[("巤","liè",FH,"从毛从㲋（獸足）：毛巤也（《說文》「毛巤也」），獸長毛；獵之初文。","l「拢离」取「拢」：毛拢而離。"),
("獵","liè",FH,"从犬巤聲：放獵逐禽也（《說文》「放獵逐禽也」），田獵。","l取拢离：犬逐而離。"),
("臘","là",FH,"从肉巤聲：冬至後三戌臘祭百神（《說文》），年終大祭。","l取拢离：祭聚而離。"),
("蠟","là",FH,"从虫巤聲：蜜滓也（《說文》「蜜滓也」），蜂蠟。","l取拢离：蠟聚而離。"),
("邋","lā",FH,"从辵巤聲：邋遢，行不謹（《廣韻》）。","l取拢离：行散而離。"),
("鬣","liè",FH,"从髟巤聲：髮鬣鬣也（《說文》「髮鬣鬣也」），馬鬃。","l取拢离：髮長而離。"),
("儠","liè",FH,"从人巤聲：長壯儠儠也（《說文》）。","l取拢离：人長而離。"),
("擸","liè",FH,"从手巤聲：理持也（《說文》「理持也」），折斷、整理。","l取拢离：手拢而離。"),
("躐","liè",FH,"从足巤聲：踐也（《說文》「踐也」），逾越、躐等。","l取拢离：足踐而離。"),
("攦","lì",FH,"从手麗聲：折也（《說文》「折也」）；或作攦。","l取拢离：折而離。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"巤系同取「長毛散開、牽引而離」一面：獵犬、臘祭、蠟蜜、邋行、鬣鬃、儠長、擸理、躐踐；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":553,"name":"巤"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"llie-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第553部「巤部」（卷九十一 火）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡553a2026-10-24","risk":"low","claims":cl},open(r"intake\20261024-字卡553a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261024-字卡553a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))