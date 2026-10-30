import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
N="字形：古文字字形库未收。"
F="【第593部「林部」】林＝二木並立（《說文》「平土有叢木曰林」），借音同「廩」（聚集）；禁＝从示林聲，對社林神靈的畏忌→禁止（《說文》「吉凶之忌也」）；㪔＝从攴从林，敲擊林木使果葉四散（《玉篇》「分離也、放也」）。"
D=[("噤","jìn",F,"从口禁聲：口閉也（《說文》「口閉也」），寒而口噤。","j「聚决」取「聚」：口聚而决。"),
("䫴","jìn",F,"从頁禁聲：齘也，癢搔之齒䫴齘（《釋名》），閉口切齒。","j取聚决：齒聚而决。"),
("凚","jìn",F,"从冫禁聲：寒極（《玉篇》），寒戰貌。","j取聚决：寒聚而决。"),
("僸","jìn",F,"从人禁聲：仰頭也（《集韻》）；北夷之樂。","j取聚决：仰首而决。"),
("襟","jīn",F,"从衣禁聲：袍襦前袂（《廣韻》），衣的交領→胸懷、前面。","j取聚决：衣交而决。"),
("齽","jìn",F,"从齒禁聲：鉤齒內曲謂之齽（《集韻》），牙齒酸噤。","j取聚决：齒曲而决。"),
("㦗","jìn",F,"从心禁聲：心㦗皃（《廣韻》），心堅固。","j取聚决：心堅而决。"),
("㩒","qín",F,"从手禁聲：持也（《廣韻》），急持衣衿（《說文》捦）。","q「亲缺」取「亲」：手親而缺。"),
("㯲","jìn",F,"从木禁聲：格也（《方言》），竹木格，所以扞門。","j取聚决：木格而决。"),
("䌝","jīn",F,"从糸禁聲：絲也（《玉篇》）；青色，藍染䌝碧所用。","j取聚决：絲聚而决。"),
("散","sàn",F,"从攴从林：敲擊林木，果葉紛墜四散（《玉篇》「分離也、放也」）；轉義 鬆散、細碎、徘徊；音源 㪔、鱻通用。","s「失收」取「失」：擊而失收。"),
("饊","sǎn",F,"从食散聲：熬稻粻䅣（《說文》），糯米煮熟乾煎，分散不黏。","s取失收：食散而收。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"林部同取「禁閉、散開」兩面：噤䫴齽皆口齒之閉、凚寒閉、僸仰首、襟交領、㦗心堅、㩒急持、㯲扞門、䌝絲聚；散與饊則取擊林四散。只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":593,"name":"林"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"llin4-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第593部「林部」（卷九十七 殸）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
p2=r"intake\20261024-字卡593d.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡593d{it}-2026-10-24","risk":"low","claims":cl},open(p2,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p2,"--format","json")
    if "PLAN_DUPLICATE" not in out:
        print("ok claims",len(cl)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",cl[idx]["title"]); cl.pop(idx)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))