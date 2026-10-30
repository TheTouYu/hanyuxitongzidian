import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FQ="【第540部「秋部」】秋＝甲骨文象蟋蟀形（促織／紡織娘），入秋入户鳴聲促織；借以代表秋季，另造从禾从炅之「秋」（禾穀成熟，《說文》「禾穀孰也」）；轉義焦枯、光秃、悲愁、時節、聚束、飛騰。"
N="字形：古文字字形库未收。"
D=[("秋","qiū",FQ,"本象蟋蟀（促織），借為秋季；又造从禾之秋表禾穀成熟。","q「亲缺」取「亲」：禾親而熟。"),
("楸","qiū",FQ,"从木秋聲：楸樹，木理如梓，古人植於墓。","q取亲缺：木親而实。"),
("萩","qiū",FQ,"从艸秋聲：萩，蒿類（《說文》「蕭也」）；又菽。","q取亲缺：草秋而凋。"),
("鶖","qiū",FQ,"从鳥秋聲：禿鶖，水鳥，頭禿。","q取亲缺：鳥秋而栖。"),
("䨂","qiū",FQ,"从雨秋聲：雨貌（《集韻》）。","q取亲缺：雨秋而降。"),
("鰍","qiū",FQ,"从魚秋聲：泥鰍，善鑽泥。","q取亲缺：魚秋而潛。"),
("愁","chóu",FQ,"从心秋聲：憂也（《說文》），秋氣蕭瑟而生愁。","ch「刺持」取「持」：心秋而持。"),
("愀","qiǎo",FQ,"从心秋聲：色變也（《說文》），憂懼變容。","q取亲缺：色親而變。"),
("揪","jiū",FQ,"从手秋聲：揫之俗，抓住不放。","j「聚决」取「聚」：手聚而决。"),
("鬮","jiū",FQ,"从鬥龜聲：鬮，取物之紙團（抓鬮）。","j取聚决：取聚而决。"),
("啾","jiū",FQ,"从口秋聲：啾唧，小聲；又啾啾（鳥鳴）。","j取聚决：聲聚而决。"),
("湫","qiū",FQ,"从水秋聲：水潭（《說文》「隘下也」）；又湫隘。","q取亲缺：水聚而缺。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"秋系同取「秋氣收斂、萬物就成」一面：楸言木、萩言草、鶖鰍言鳥魚、愁愀言心；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":540,"name":"秋"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lqiu-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第540部「秋部」（卷九十 秋）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡540a2026-10-24","risk":"low","claims":cl},open(r"intake\20261024-字卡540a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261024-字卡540a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))