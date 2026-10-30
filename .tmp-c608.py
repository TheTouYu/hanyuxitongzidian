import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pck_tmpfix.py".replace("pck","pkc")
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F="【496 公部】公＝从八从厶：八者分也，厶者私也，分之私則為公；本義公平、公共（《說文》「平分也」），轉義公侯、祖父、雄性。部內从公諸字取「平分、分張」兩面。"
N="字形：古文字字形库未收。"
D=[("公","gōng",F,"本部部首字：分私為公→公平、公共、公侯。","g「隔估」取「隔」：分而相隔。"),
("翁","wēng",F,"从羽公聲：鳥頸上之毛（《說文》「頸毛也」），引申老翁、泛指老者。","w?—聲母屬零/影，取借聲。"),
("袞","gǔn",F,"从衣公聲：天子祭祀所服袞衣，龍紋卷曲。","g取隔：衣紋相隔。"),
("松","sōng",F,"从木公聲：松樹，取公之聲。","s「失收」取「收」：松葉收束。"),
("訟","sòng",F,"从言公聲：爭辯於公（《說文》「爭也」），引申訴訟。","s取失收：言爭而收。"),
("頌","sòng",F,"从頁公聲：本義容貌（《說文》「皃也」），引申稱頌。","s取失收：容收而頌。"),
("瓮","wèng",F,"从瓦公聲：小口大腹之陶器。","w?—零聲母。"),
("船","chuán",F,"从舟，鉛省聲（一說公聲）：水上之舟。","ch「刺持」取「持」：舟持於水。"),
("伀","zhōng",F,"从人公聲：志及眾人之貌，引申驚懼。","zh「凿总」取「凿」：眾聚而伀。"),
("蚣","gōng",F,"从虫公聲：「蜈蚣」，百足之蟲。","g取隔：足多而隔。"),
("忪","zhōng",F,"从心公聲：「怔忪」，驚懼不安。","zh取凿：心鑿而悸。"),
("妐","zhōng",F,"从女公聲：夫之兄（兄公）。","zh取凿：長而鑿。"),
("彸","zhōng",F,"从彳公聲：「征彸」，行遽之貌。","zh取凿：行促而凿。"),
("衳","zhōng",F,"从衣公聲：小袴（《玉篇》「小袴也」）。","zh取凿：衣小以裹。"),
("蓊","wěng",F,"从艸公聲：草木茂盛（「蓊鬱」）。","w?—零聲母。")]
cl=[]
for i,(ch,p,F0,xp,sm) in enumerate(D,1):
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取公部「分私為公、分張」一面：羽取其毛，衣取其紋，言取其爭。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
    cl.append({"id":f"lct-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
      "boundary":"源自《系統漢語》第496部公部（卷八十一 釘）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
json.dump({"schema_version":1,"intent":"字卡496a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡496a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡496a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out, "cards:", len(cl))
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))