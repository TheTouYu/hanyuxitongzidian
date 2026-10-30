import json,subprocess,os,glob
FA="【443 卝部·乖支】二叠表极深，多指奇异、歪斜、参差。"
FB="【444 雈部】雈（huán）＝甲文象头上有角之鸟，本义当指苍鹭（有毛角、盯水面待鱼、鸣声亮、颈常曲）；辯證：《说文》「鴟屬」存疑（猫头鹰「舊」亦从雈），与草名「萑」形近易混。音源：音源字，源自鹭鸣。"
N="字形：古文字字形库未收。"
D=[("㔞","kuāi",FA,"《廣韻》「劥㔞，人有力也」——力大。","k「口控」取「控」：力聚而控。"),
("㪓","chuái",FA,"《篇海》「災㪓，又邪也」——灾邪不正。","ch「刺持」取「持」：邪曲而持。"),
("䂷","guài",FA,"《集韻》「碎也」；《字彙》「石貌」——石参差。","g「隔估」取「隔」：石碎而隔。"),
("䓙","kuā",FA,"《廣韻》「䓙雜，斜皃」——草斜杂。","k取控：草斜而控。"),
("𡇸","guāi",FA,"《五音篇海》「音乖」，义不详。","g取隔：借声存疑。"),
("𣔪","guāi",FA,"《字彙補》「音未詳，人名」。","g取隔：借声记名。"),
("𨧰","zú",FA,"《字彙》「將沃切，音族，姓也」。","z「凿总」取「总」：借声记姓。"),
("𨵞","wāi",FA,"《搜眞玉鏡》「五乖切」，义不详，疑指门杠。","w「勿问」取「问」：门闩而问。"),
("雈","huán",FB,"《說文》「鴟屬，从隹从𦫳，有毛角」；《爾雅》「雈，老鵵」——有毛角的鸮类，一说苍鹭。","h「豁活」取「活」：羽角而活。"),
("雚","guàn",FB,"《說文》「小爵也，从雈吅聲」；《玉篇》「水鳥也」——雚、鸛古今字。","g「隔估」取「隔」：水鸟而隔。"),
("鸛","guàn",FB,"《說文》「鸛專，如䧿短尾」——大型涉禽，喙粗颈长，叩喙发声。","g取隔：涉水而立。"),
("灌","guàn",FB,"《說文》「水，出廬江雩婁，北入淮」——水名；引申灌注、灌溉、聚。","g取隔：水注而隔。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取本部「乖违／鹭鸟」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lbw-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第443－444部（卷七十四 雈）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡443b2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡443b.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡443b.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))