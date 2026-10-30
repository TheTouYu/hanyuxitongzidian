import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FH="【第556部「辛部」】辛（䇂）＝象小刻刀，刻字紋身；部内四系 言／𣓀親／新／豙。辛辣之味亦由辛來，故从辛之字多兼「刺、痛、細」義。"
N="字形：古文字字形库未收。"
D=[("鋅","xīn",FH,"从金辛聲：剛也（《集韻》「剛也」），《玉篇》同「釨」；今指鋅（Zn）。","x「续消」取「续」：金剛而续。"),
("觪","xīng",FH,"从角辛聲：角弓調利也（《玉篇》「角弓調利也」），用角便也。","x取续消：角調而续。"),
("辤","cí",FH,"从辛从受：不受也（《說文》「不受也」），受辛宜辭之；籀文从台。","c「刺持」取「持」：辭受而持。"),
("䅸","shēn",FH,"从禾莘聲：穀名（《集韻》「穀名」）；又草木叢生（音 zú）。","sh「失收」取「收」：穀收而聚。"),
("莘","xīn",FH,"从艸辛聲：細莘，藥艸（《集韻》），味辛辣故从辛；引申細長而眾多（shēn）。","x取续消：艸辛而续。"),
("䢄","xǐ",FH,"从朩台聲：枲，麻也（《說文》「麻也」），籀文从𣏟从辝，指麻生茂密如榛。","x取续消：麻密而续。"),
("儭","chèn",FH,"从人親聲：裏也（《廣韻》「裏也」），襯托、陪襯，與襯通。","ch「刺持」取「持」：衣裏而持。"),
("㜪","shēn",FH,"从女莘聲：有㜪，國名（《集韻》），鯀妃有㜪氏女，生禹；或作姺。","sh取失收：女聚而收。"),
("觲","xīng",FH,"从角辛聲：角弓調利也（《玉篇》），觪之俗體，見《字彙》。","x取续消：角利而续。")]
for ch,p,F0,xp,sm in D:
    num=557 if ch=="觲" else 556
    name="觲" if ch=="觲" else "辛"
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"辛系同取「刺、痛、細、聚」一面：鋅剛、觪角弓、辤辭受、䅸穀聚、莘細辛、䢄麻密、儭襯裏、㜪國名；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":num,"name":name}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lxin3-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第556部「辛部」（卷九十二 辛）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡556c2026-10-24","risk":"low","claims":cl},open(r"intake\20261024-字卡556c.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261024-字卡556c.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))