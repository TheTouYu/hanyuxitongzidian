import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FY="【第523部「羊部」】羊＝象有角的羊頭形，取其角為標誌符號；音源為羊叫聲。字族分六面：多而群處／有角多毛／羊鳴／羊病瘙癢／羊眼假寐／羊味烹煮。"
N="字形：古文字字形库未收。"
D=[("庠","xiáng",FY,"从广羊聲：禮官養老之所，夏校殷庠周序（《說文》），即學校。","x「续消」取「续」：養老而續。"),
("羋","mǐ",FY,"从羊象聲氣上出：羊鳴也（《說文》），與「牟」同意。","m「蒙末」取「蒙」：鳴氣蒙而出。"),
("蛘","yǎng",FY,"从虫羊聲：搔蛘（《說文》），本指叮咬致癢之蟎蝨。","y「圆容」取「圆」：蟲咬而癢。"),
("𩰱","shāng",FY,"从鬲羊聲：烹煮（《說文》「煑也」）。","sh「失收」取「收」：鬲煮而收。"),
("葁","jiāng",FY,"从艸姜聲：生薑（俗䕬字），佐料去羊肉臊味。","j「聚决」取「聚」：辛聚而散。"),
("䭐","yàng",FY,"从食羊聲：餌也、糕餅（《玉篇》）。","y取圆容：食團而圓。"),
("姜","jiāng",FY,"从女羊聲：神農居姜水以為姓（《說文》），借為女子美稱。","j取聚决：姓聚而傳。"),
("垟","yáng",FY,"从土羊聲：土精、墳垟土怪（《玉篇》）。","y取圆容：土聚而圓。"),
("眻","yáng",FY,"从目羊聲：眉間曰眻，一曰目美（《集韻》）。","y取圆容：目美而含。"),
("鴹","yáng",FY,"从鳥羊聲：𪄲鴹一足，舞則天下雨（《字統》）。","y取圆容：鳥舞而圓。"),
("𦭵","yáng",FY,"从艸羊聲：𦭵葲，蜀羊泉，蔓生白毛，漿果紅（藥名）。","y取圆容：蔓引而圓。"),
("㺊","yàng",FY,"从犬羊聲：獸如師子，咋人則疾，即「恙」（《神異經》）。","y取圆容：獸噬而恙。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同部諧聲字分面：取「群處養老」（庠／姜／垟）、取「羊鳴」（羋）、取「羊病瘙癢」（蛘／㺊）、取「羊眼目美」（眻）、取「羊味烹煮」（𩰱／葁／䭐）、取「羊狀有毛」（鴹／𦭵）；只列本部字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":523,"name":"羊"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lyang-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}（{p}）{xp}",
 "boundary":"源自《系統漢語》第523部「羊部」（卷八十七 羊）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡523b2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡523b.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡523b.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))