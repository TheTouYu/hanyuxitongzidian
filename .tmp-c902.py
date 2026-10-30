import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
N="字形：古文字字形库未收。"
F="【第593部「林部」】林＝二木並立（《說文》「平土有叢木曰林」），本卷借音取懸磬懸冰成林之狀；本批取「森密、禁止、散分」三面。"
D=[("槮","sēn",F,"从木參聲：木長皃（《說文》「木長皃」），樹高森然。","s「失收」取「收」：木長而收。"),
("禁","jìn",F,"从示林聲：吉凶之忌也（《說文》「吉凶之忌也」），禁忌、禁止。","j「聚决」取「聚」：忌而聚。"),
("噤","jìn",F,"从口禁聲：口閉也（《說文》「口閉也」），噤若寒蟬。","j取聚决：口閉而聚。"),
("凚","jìn",F,"从仌禁聲：寒戰（《集韻》「寒極而戰」），凜冽。","j取聚决：寒凝而聚。"),
("襟","jīn",F,"从衣禁聲：交衽也（《說文》「交衽也」），衣襟、胸懷。","j取聚决：衣交而聚。"),
("齽","jìn",F,"从齒禁聲：齽齘，切齒（《集韻》），咬牙。","j取聚决：齒切而聚。"),
("散","sàn",F,"从肉从㪔：分離也（《說文》「分離也」），分散、散漫。","s取失收：分而收。"),
("饊","sǎn",F,"从食散聲：熬稻粻饘也（《說文》），饊子，油炸麵食。","s取失收：食散而收。"),
("傘","sǎn",F,"从人从繖省：蓋也（《集韻》「傘，蓋也」），雨傘。","s取失收：蓋張而收。"),
("撒","sā",F,"从手散聲：散布也（《集韻》），撒開、撒手。","s取失收：手散而收。"),
("潸","shān",F,"从水散省聲：涕流皃（《詩》「潸焉出涕」），淚下。","sh「失收」取「收」：淚下而收。"),
("霰","xiàn",F,"从雨散聲：稷雪也（《說文》「稷雪也」），雪珠。","x「续消」取「续」：雪粒而续。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"林部同取「森密、禁止、散分」一面：槮木長、禁忌、噤口閉、凚寒戰、襟交衽、齽切齒、散分離、饊熬稻、傘蓋、撒散布、潸淚下、霰雪珠；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":593,"name":"林"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"llin2-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第593部「林部」（卷九十七 殸）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
p2=r"intake\20261024-字卡593b.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡593b{it}-2026-10-24","risk":"low","claims":cl},open(p2,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p2,"--format","json")
    if "PLAN_DUPLICATE" not in out:
        print("ok claims",len(cl)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",cl[idx]["title"]); cl.pop(idx)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))