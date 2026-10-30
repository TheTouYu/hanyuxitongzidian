import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FH="【第550部「火部」耿系】耿＝从耳烓省聲，耳薄能透光（《說文》「耳箸頰也」），取「小明、耳熱不安、形近犬訛」三面；《說文》耳貼頰之說不足取。"
N="字形：古文字字形库未收。"
D=[("𦵸","gěng",FH,"从艸耿聲：芋莖也（《玉篇》「芋莖也」），芋莖皮薄呈蜂窩狀可透光。","g「隔估」取「隔」：莖薄而隔。"),
("𥉔","gěng",FH,"从目耿聲：𥉔䁅，有餘視也，一曰喜也（《玉篇》）。","g取隔估：視餘而隔。"),
("𤓐","gěng",FH,"从火耿聲：音義同耿（《字彙補》「音義同耿」）。","g取隔估：火小而隔。"),
("𢞚","gěng",FH,"从心耿聲：憂也（《集韻》「憂也」），耿介不安。","g取隔估：心憂而隔。"),
("㷦","xù",FH,"从火耿聲：同「𤋀」，《龍龕》「正作瞁，驚視也」，形近「犬」之訛。","x「续消」取「续」：驚視而续。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"耿系同取「耳薄透光、小而明」一面：𦵸芋莖透光、𥉔餘視、𤓐同耿、𢞚心憂、㷦驚視（訛）；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":550,"name":"火"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lhuo8-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第550部「火部」（卷九十一 火）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡550h2026-10-24","risk":"low","claims":cl},open(r"intake\20261024-字卡550h.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261024-字卡550h.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))