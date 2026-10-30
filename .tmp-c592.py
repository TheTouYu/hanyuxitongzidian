import json,subprocess,os,glob
F="【476 夒部】夒＝甲骨文象長臂猿之形（《集韻》「猱，玃猱，獼猴類。或作夒」）；音源字，取猴子的叫聲。部内「夔」另为一物：神魖如龍一足，商周青銅器玉器有其紋飾，疑即鱷魚之類，音源取雷聲。"
N="字形：古文字字形库未收。"
D=[("夒","náo",F,"本部部首字：長臂猿形的獼猴，善攀援；後作「猱」「蝚」。","n「纳弄」取「弄」：猿臂弄攀。"),
("夔","kuí",F,"从夒从攵：象有角、手、人面的一足神獸（神魖），音源取雷聲。","k「口控」取「控」：一足而控。"),
("猱","náo",F,"从犬夒聲：獼猴，善攀援，取其敏捷。","n取弄：犬猴相弄。"),
("蝚","róu",F,"从虫夒聲：蛭蝚，即水蛭，爬附如猿攀。","r「柔锐」取「柔」：蟲柔而附。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取夒部「長臂猿形、善攀附」一面：犬取獸，虫取其附。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lcd-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第476部夒部（卷七十八 夒）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡476a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡476a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡476a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))