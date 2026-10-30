import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FZ="【第520部「章部」】章＝甲骨文从〇（玉璧）从辛（刀），象刀形玉璧，為「璋」之初文；轉義憑信之標記→顯明、篇章章程、紅色；辯證與「璧」同源；音源本「辛」聲，彰明義音同「黃」。"
N="字形：古文字字形库未收。"
D=[("章","zhāng",FZ,"本部字根：刀形玉璧，引申標記、篇章。","zh「凿总」取「凿」：刻玉而章。"),
("彰","zhāng",FZ,"从彡从章：錯綜的花紋色彩（《說文》「文彰也」），引申顯明。","zh取凿总：文采昭彰。"),
("璋","zhāng",FZ,"从玉章聲：半圭為璋（《說文》），禮器、憑信。","zh取凿总：玉刻而信。"),
("障","zhàng",FZ,"从𨸏章聲：阻隔（《說文》「隔也」），步障、屏障。","zh取凿总：隔而障。"),
("墇","zhàng",FZ,"从土章聲：壅塞、隔障（《說文》「擁也」）。","zh取凿总：土壅而障。"),
("幛","zhàng",FZ,"从巾章聲：以布帛題字的慶弔禮物，又遮蔽。","zh取凿总：布張而障。"),
("嶂","zhàng",FZ,"从山章聲：高險如屏之山峰（《集韻》）。","zh取凿总：山屏而障。"),
("瘴","zhàng",FZ,"从疒章聲：山林濕熱蒸鬱之癘氣（《玉篇》「瘴癘也」）。","zh取凿总：氣鬱而障。"),
("漳","zhāng",FZ,"从水章聲：漳河（《說文》），清濁二源。","zh取凿总：水分而章。"),
("樟","zhāng",FZ,"从木章聲：樟樹，香氣而木質棕紅（印泥之色）。","zh取凿总：木赤而章。"),
("鱆","zhāng",FZ,"从魚章聲：章魚，八足，能變色，本色紫紅。","zh取凿总：魚變而章。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同部諧聲字分三面：取「憑信顯明」（章／彰／璋）、取「封印阻隔」（障／墇／幛／嶂／瘴）、取「印色棕紅」（漳／樟／鱆）；只列本部字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":520,"name":"章"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lzhang-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}（{p}）{xp}",
 "boundary":"源自《系統漢語》第520部「章部」（卷八十五 匚）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡520a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡520a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡520a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))