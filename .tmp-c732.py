import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FH="【第550部「火部」】火＝象火焰上騰；字族 麃＝从鹿从火，火燒山林（《說文》「麤也」），引申白色、疾行、肥盛。"
N="字形：古文字字形库未收。"
D=[("麃","páo",FH,"从鹿从火：火燒山林所驅之獸（《說文》「麤也」）；转义白色、疾行、肥盛。","p「拼辟」取「拼」：火驅而拼。"),
("鑣","biāo",FH,"从金麃聲：馬銜也（《說文》「馬銜也」），馬嚼子。","b「闭剥」取「闭」：銜口而闭。"),
("儦","biāo",FH,"从人麃聲：行貌（《說文》「行皃」），眾人行走。","b取闭剥：行眾而闭。"),
("瀌","biāo",FH,"从水麃聲：雨雪瀌瀌（《說文》引《詩》）。","b取闭剥：雨密而闭。"),
("臕","biāo",FH,"从肉麃聲：肥肉（《廣韻》），牲畜肥滿。","b取闭剥：肉滿而闭。"),
("犥","piāo",FH,"从牛麃聲：牛黃白色（《說文》「牛黃白色」）。","p取拼辟：色白而拼。"),
("藨","biāo",FH,"从艸麃聲：鹿藿也（《說文》），藨草、莓。","b取闭剥：草蔓而闭。"),
("穮","biāo",FH,"从禾麃聲：耨鉏田也（《說文》「耨鉏田也」），耘田。","b取闭剥：田耘而闭。"),
("皫","piǎo",FH,"从白麃聲：色白（《說文》「色白也」）。","p取拼辟：色白而拼。"),
("表","biǎo",FH,"从衣从毛：上衣也（《說文》「上衣也」），外衣→表面、表章。","b取闭剥：衣外而闭。"),
("蔈","biāo",FH,"从艸麃聲：苕之黃華（《說文》「苕之黃華也」）。","b取闭剥：華黃而闭。"),
("嫖","piào",FH,"从女麃聲：輕也（《說文》「輕也」），輕捷。","p取拼辟：輕捷而拼。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"麃系同取「火燒所生之白、疾、肥」一面：鑣銜、儦行、瀌雨、臕肥、犥白牛、藨草、穮耘、皫白、表衣、蔈華、嫖輕；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":550,"name":"火"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lhuo4-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第550部「火部」（卷九十一 火）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡550d2026-10-24","risk":"low","claims":cl},open(r"intake\20261024-字卡550d.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261024-字卡550d.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))