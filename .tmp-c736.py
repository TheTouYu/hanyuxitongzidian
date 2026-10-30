import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FH="【第552部「尞部」】尞＝从木从火，架柴而燒（《說文》「柴祭天也」），燎之初文；字族取「燃燒所生之光、遠、明、纏」諸面。"
N="字形：古文字字形库未收。"
D=[("尞","liáo",FH,"从木从火：柴祭天也（《說文》「柴祭天也」），即燎；焚柴祭天。","l「拢离」取「拢」：柴拢而離。"),
("燎","liáo",FH,"从火尞聲：放火也（《說文》「放火也」），燎原、庭燎。","l取拢离：火拢而離。"),
("僚","liáo",FH,"从人尞聲：好貌（《說文》「好皃」），同官曰僚。","l取拢离：人拢而離。"),
("寮","liáo",FH,"从宀尞聲：穿也（《說文》「穿也」），小屋、同官。","l取拢离：屋拢而離。"),
("療","liáo",FH,"从疒尞聲：治也（《說文》「治也」），醫治。","l取拢离：病拢而離。"),
("遼","liáo",FH,"从辵尞聲：遠也（《說文》「遠也」）。","l取拢离：行遠而離。"),
("瞭","liǎo",FH,"从目尞聲：目明也（《說文》「目明也」）。","l取拢离：目明而離。"),
("撩","liáo",FH,"从手尞聲：理也（《說文》「理也」），撩撥。","l取拢离：手拢而離。"),
("嘹","liáo",FH,"从口尞聲：嘹喨（《集韻》），聲清遠。","l取拢离：聲遠而離。"),
("潦","lǎo",FH,"从水尞聲：雨水大貌（《說文》「雨水大皃」），積水。","l取拢离：水聚而離。"),
("憭","liǎo",FH,"从心尞聲：慧也（《說文》「慧也」）。","l取拢离：心慧而離。"),
("繚","liáo",FH,"从糸尞聲：纏也（《說文》「纏也」），繚繞。","l取拢离：絲缠而離。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"尞系同取「焚柴之光遠而散」一面：燎原、僚官、寮屋、療治、遼遠、瞭明、撩撥、嘹亮、潦水、憭慧、繚纏；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":552,"name":"尞"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lliao-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第552部「尞部」（卷九十一 火）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡552a2026-10-24","risk":"low","claims":cl},open(r"intake\20261024-字卡552a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261024-字卡552a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))