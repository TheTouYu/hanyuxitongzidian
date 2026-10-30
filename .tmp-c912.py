import json,subprocess,os,glob,re
ROOT=r"D:\系统汉字"
ENV=dict(os.environ); ENV["PATH"]=ROOT+r"\.runtime\mingit\cmd;"+ENV["PATH"]
PY=ROOT+r"\.runtime\venv\Scripts\python.exe"; SH=ROOT+r"\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=ROOT,capture_output=True,env=ENV)
    return (r.stdout+b"\n"+r.stderr).decode("utf-8","replace")
def git(*a):
    r=subprocess.run([ROOT+r"\tools\git.cmd"]+list(a),cwd=ROOT,capture_output=True,env=ENV)
    return (r.stdout+b"\n"+r.stderr).decode("utf-8","replace")
N="字形：古文字字形库未收。"
F0="【第595部「㦰部」】㦰（jiān）＝象戈割从（眾人）之足，對一群體全部割取，表收割、滅盡（《玉篇》「田器。又盡也」）；轉義 細小脆弱→纖細；辨證《說文》「从从持戈」析形已隔；音源借音同「冉」「三」。"
D=[("㦰","jiān",F0,"从戈割从之足：全部割取，收割、滅盡；引申纖細。古文讀若咸，讀若「攕攕女手」。","j「聚决」取「聚」：聚割而决。"),
("韱","xiān",F0,"从韭㦰聲：山韭也（《說文》「山韭也」），割韭；引申細。","x「续消」取「续」：韭續而消。"),
("𩃔","jiān",F0,"从雨㦰聲：微雨也（《說文》「微雨也」），毛毛細雨，浸漬。","j取聚决：雨微而决。"),
("纖","xiān",F0,"从糸韱聲：細也（《說文》「細也」），繒帛之細者，凡微細曰纖。","x取续消：絲細而消。"),
("孅","xiān",F0,"从女韱聲：銳細也（《說文》「銳細也」），指尖細；孅趨，巧佞。","x取续消：指細而消。"),
("攕","xiān",F0,"从手韱聲：好手皃（《說文》引《詩》「攕攕女手」），手指細長。","x取续消：手細而消。"),
("櫼","jiān",F0,"从木韱聲：楔也（《說文》「楔也」），上大下小之木尖。","j取聚决：木楔而决。"),
("鑯","jiān",F0,"从金韱聲：鐵器也（《說文》），鋼釺、刻；俗作尖。","j取聚决：鐵尖而决。"),
("籤","qiān",F0,"从竹韱聲：驗也，一曰銳也、貫也（《說文》），標識、刺入。","q「亲缺」取「亲」：竹銳而缺。"),
("讖","chèn",F0,"从言韱聲：驗也（《說文》「驗也」），預言徵驗之書；《釋名》「纖也，其義纖微」。","ch「刺持」取「持」：言微而持。"),
("襳","jiān",F0,"从衣韱聲：圭表飾、小襦、襌襦（《玉篇》），婦女上衣長帶。","j取聚决：衣飾而决。"),
("虃","jiān",F0,"从艸韱聲：艸名，百足也（《集韻》），地蜈蚣草。","j取聚决：草蔓而决。")]
rows=[]
for it in D:
    ch,p,F0_,xp,sm=it[0],it[1],it[2],it[3],it[-1]
    sec=[{"key":"bengen","label":"字根本义","text":F0_,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"㦰系同取「割取所餘之細」一面：韱山韭、𩃔微雨、纖細絲、孅指細、攕手好、櫼木楔、鑯鐵尖、籤竹銳、讖纖微之驗、襳衣帶、虃細草；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":595,"name":"㦰"}],"sections":sec},open(rf"{ROOT}\web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
    rows.append({"id":f"ljian1-{len(rows)+1:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第595部「㦰部」（卷九十七 殸）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
git("add","web/public/cards"); print(git("commit","-m","cards: 595㦰部首批12字")[-60:])
p2=ROOT+r"\intake\20261024-字卡595a.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡595a{it}-2026-10-24","risk":"low","claims":rows},open(p2,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p2,"--format","json")
    if "PLAN_DUPLICATE" not in out: print("ok",len(rows)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",rows[idx]["title"]); rows.pop(idx)
bd=os.path.basename(sorted(glob.glob(ROOT+r"\data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=re.search(r'"content_hash":\s*"([0-9a-f]{64})"',run("bundle-status",bd,"--format","json")).group(1)
print("bundle",bd); run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); print("err",json.loads(run("validate","--format","json")).get("errors"))
git("add","knowledge","data/knowledge","intake/20261024-字卡595a.json"); print(git("commit","-m","knowledge: 595㦰部首批12条")[-60:])