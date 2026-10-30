import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FX="【第518部「兄部」·兄支】兄＝从人上有口，象口呼其名，表示成年（男子二十冠而字）；轉義年長、大；名字非其人，故有比況、恍惚義；音源借「光」。"
FJ="【第518部「兄部」·竟支】竟＝甲骨文从辛兄聲（辛象刻刀或髮簪），象成人儀式上的簪髮、紋身；轉義界限（境）、完畢終盡；辯證《說文》「从音从人」析形不確；「競」為竟之二疊，表緊貼相爭。"
N="字形：古文字字形库未收。"
D=[("兄","xiōng",FX,"本部字根：口呼其名，成人取字，引申年長。","x「续消」取「续」：名續而呼。"),
("況","kuàng",FX,"从水兄聲：寒水（《說文》），借表比擬、況且、更加。","k「口控」取「控」：比擬而控。"),
("貺","kuàng",FX,"从貝兄聲：賜、贈（《說文》「賜也」）。","k取口控：賜予而控。"),
("怳","huǎng",FX,"从心況省聲：狂放、模糊不清（《說文》「狂之皃」）、怳忽。","h「豁活」取「豁」：心恍而豁。"),
("眖","kuàng",FX,"从目兄聲：視也、對看（《玉篇》）。","k取口控：目視而控。"),
("竟","jìng",FJ,"本部二級字根：簪髮成人，引申界限、終盡。","j「聚决」取「决」：界决而止。"),
("境","jìng",FJ,"从土竟聲：疆界（《新附》「疆也」），經典通用竟。","j取聚决：土界而决。"),
("鏡","jìng",FJ,"从金竟聲：照形之鏡（《說文》「景也」），《釋名》「鏡，景也」。","j取聚决：光聚而照。"),
("競","jìng",FJ,"从誩从二人：強語、相逐（《說文》），為竟之二疊，表緊貼相爭。","j取聚决：爭而决。"),
("獍","jìng",FJ,"从犬竟聲：獸名，狀如虎豹而小，生而食母（《述異記》）。","j取聚决：獸決而噬。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同部諧聲字分二面：兄支取「比擬／空大模糊」（況／貺／怳／眖）、竟支取「界限終盡／緊貼相爭」（竟／境／鏡／競／獍）；只列本部字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":518,"name":"兄"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lxiong-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}（{p}）{xp}",
 "boundary":"源自《系統漢語》第518部「兄部」（卷八十五 匚）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡518a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡518a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡518a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))