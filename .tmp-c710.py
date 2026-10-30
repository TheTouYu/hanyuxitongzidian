import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FY="【第543部「玉部」】玉＝象玉串形（三玉相連、一貫其間），《說文》「石之美……象三玉之連」；轉義玉製品、瑞玉、佩玉、美稱、磨煉。"
N="字形：古文字字形库未收。"
D=[("瓏","lóng",FY,"从玉龍聲：玉聲（《說文》「玉聲也」），玲瓏。","l「拢离」取「拢」：聲聚而玲。"),
("瑩","yíng",FY,"从玉熒聲：玉色（《說文》「玉色也」），明淨。","y「柔锐」取「锐」：玉光而锐。"),
("璽","xǐ",FY,"从玉爾聲：王者印（《說文》「王者印也」），璽印。","x「续消」取「续」：印信而續。"),
("環","huán",FY,"从玉睘聲：璧屬（《說文》「璧也」），圓環、環繞。","h「豁活」取「豁」：環转而活。"),
("理","lǐ",FY,"从玉里聲：治玉也（《說文》），順理剖析→條理。","l取拢离：治玉而离。"),
("珍","zhēn",FY,"从玉㐱聲：寶也（《說文》），珍寶、珍重。","zh「凿总」取「凿」：寶而凿。"),
("玩","wán",FY,"从玉元聲：弄也（《說文》），把玩、玩好。","w? 用 r 取柔锐：玩弄而柔。"),
("班","bān",FY,"从玨从刀：分瑞玉也（《說文》），分班、班次。","b「闭剥」取「剥」：分玉而剥。"),
("瑞","ruì",FY,"从玉耑聲：以玉為信也（《說文》），瑞玉、祥瑞。","r取柔锐：信玉而锐。"),
("琢","zhuó",FY,"从玉�豕聲：治玉也（《說文》），雕琢。","z「凿总」取「凿」：雕凿而总。"),
("玟","mín",FY,"从玉文聲：玉名（《說文》「玉也」）；又玟瑰。","m「蒙末」取「末」：玉文而末。"),
("琇","xiù",FY,"从玉秀聲：玉名（《說文》「玉也」）。","x取续消：玉秀而續。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"玉系同取「石之美、需治乃成器」一面：理琢治玉、班分瑞玉、瑞為信、環璧屬、璽王印；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":543,"name":"玉"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lyu2-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第543部「玉部」（卷九十 秋）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡543b2026-10-24","risk":"low","claims":cl},open(r"intake\20261024-字卡543b.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261024-字卡543b.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))