import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FH="【第562部「廌部」】廌＝象獨角仙（雙叉犀金龜）形，雄蟲頭生分叉巨角，好鬥，以角挑起對手掀翻定勝負；古人以「神斷」決訟，引申律法；《說文》「解廌獸、觸不直」為後世傳說。"
N="字形：古文字字形库未收。"
D=[("廌","zhì",FH,"象獨角仙形：角鬥掀翻定勝負（《廣雅》「灋也」），引申律法決訟。","zh「凿总」取「凿」：角斗而凿。"),
("薦","jiàn",FH,"从廌从艸：獸之所食艸（《說文》），金文从舁（共舉），引申推舉、進獻。","j「聚决」取「聚」：草聚而决。"),
("𥤆","jiàn",FH,"从禾薦聲：獸之所食草（《集韻》），即黍蓬，草高之貌。","j取聚决：草高而决。"),
("𥴱","jiàn",FH,"从竹薦聲：楚謂筏上居曰𥴱（《集韻》），水上竹筏之屋。","j取聚决：竹筏而决。"),
("𨷓","jiàn",FH,"从門薦聲：門次（《廣韻》「門次」），門閥之等第。","j取聚决：門第而决。"),
("瀳","jiàn",FH,"从水薦聲：水至也（《說文》「水至也」），水涌而至。","j取聚决：水至而决。"),
("韉","jiān",FH,"从革薦聲：鞍也（《說文》「鞍也」），馬鞍之墊。","j取聚决：鞍垫而决。"),
("灋","fǎ",FH,"从水从廌去：刑也（《說文》「刑也。平之如水」），廌觸不直者去之，法之初文。","f「附分」取「分」：平而分。")]
for ch,p,F0,xp,sm in D:
    num=435 if ch=="灋" else 562
    nm="大" if ch=="灋" else "廌"
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"廌系同取「角斗掀翻、推舉進獻」一面：薦草、𥤆黍蓬、𥴱筏居、𨷓門次、瀳水至、韉鞍墊、灋刑法；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":num,"name":nm}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lzhi-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第562部「廌部」（卷九十二 辛）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡562a2026-10-24","risk":"low","claims":cl},open(r"intake\20261024-字卡562a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261024-字卡562a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))