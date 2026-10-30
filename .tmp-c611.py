import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F="【501 夅部】夅＝从夂从午（丰），象二人相承而不敢並行，本義降服、順服（《說文》「服也」）；轉義下降、貶抑。部內从夅諸字取「下降、相承」兩面。"
G="【502 𠬞部】𠬞（廾）＝象兩手竦舉之形，本義拱手、共舉；部內諸字皆从兩手取「捧持、共舉、執持」之義。"
N="字形：古文字字形库未收。"
D=[("夅","jiàng",F,"本部部首字：二人相承→降服、下降、貶抑。","j「聚决」取「决」：相承而决。"),
("降","jiàng",F,"从阜夅聲：从高處下來（《說文》「下也」）。","j取聚决：阜高而决下。"),
("洚","jiàng",F,"从水夅聲：大水泛溢（《說文》「水不遵道」）。","j取聚决：水聚而决。"),
("絳","jiàng",F,"从糸夅聲：大紅之色，取夅之聲。","j取聚决：染聚而深。"),
("隆","lóng",F,"从生降聲：豐大、高起（《說文》「豐大也」）。","l「拢离」取「拢」：土拢而高。"),
("廾","gǒng",G,"本部部首字：兩手竦舉→拱手、共舉。","g「隔估」取「隔」：兩手相隔。"),
("奉","fèng",G,"从廾从丰：兩手承物曰奉（《說文》「承也」），引申奉獻。","f「附分」取「附」：附而承。"),
("弄","nòng",G,"从廾从玉：兩手玩玉曰弄，引申戲弄。","n「纳弄」取「弄」：手持而弄。"),
("具","jù",G,"从廾从貝省：兩手具辦器物（《說文》「共置也」）。","j取聚决：器聚而具。"),
("戒","jiè",G,"从廾持戈：兩手警戒（《說文》「警也」），引申戒除。","j取聚决：執戈而决。"),
("兵","bīng",G,"从廾持斤：兩手執斧，本義兵器、士卒。","b「闭剥」取「剥」：斤剝而兵。"),
("弈","yì",G,"从廾亦聲：兩人對局下棋（「博弈」）。","y「柔锐」取「锐」：爭銳而弈。"),
("弊","bì",G,"从廾敝聲：仆也、困也（《說文》「頓仆也」）。","b取闭剥：敝而敗。"),
("舁","yú",G,"从廾从?：四手共舉（《說文》「共舉也」）。","y取柔锐：共舉而柔。"),
("弃","qì",G,"从廾从?（倒子）：兩手棄子，本義拋棄。","q「亲缺」取「缺」：棄而去。")]
cl=[]
for i,(ch,p,F0,xp,sm) in enumerate(D,1):
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"夅部取「下降相承」一面，𠬞部取「兩手捧持共舉」一面；形符各定落點。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
    cl.append({"id":f"lcw-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
      "boundary":"源自《系統漢語》第501－502部（卷八十二 工）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
json.dump({"schema_version":1,"intent":"字卡502a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡502a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡502a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out, "cards:", len(cl))
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))