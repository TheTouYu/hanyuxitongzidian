import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FY="【第525部「昜部」】昜＝从日从丂（丂為脖頸象形），象對日呼喊、日初升，「暘」之初文；《說文》「日出也」。轉義：日飛升→飛舉（《廣韻》「飛也」）；日大→乾旱不生。辨證：金文於丂下添光芒形，遂形近「勿」。音源：本丂聲，源出呼號，故與羊、象通。字族分三面：日烈（熱瘡夭折）／日出（明亮灼熱）／日升（飛揚搖盪）。"
N="字形：古文字字形库未收。"
D=[("昜","yáng",FY,"从日从丂：日初升、對日呼號；引申飛舉、乾旱。","y「圆容」取「圆」：日升而圓。"),
("暘","yáng",FY,"从日昜聲：日出也（《說文》引《虞書》「暘谷」），明、日乾物。","y取圆容：日出而明。"),
("陽","yáng",FY,"从𨸏昜聲：高、明也（《說文》）；山南水北為陽。","y取圆容：向日而暖。"),
("場","cháng",FY,"从土昜聲：祭神之平地，或田不耕、治穀之田（《說文》）。","ch「刺持」取「持」：掘地而持。"),
("湯","tāng",FY,"从水昜聲：熱水、沸水（《說文》）。","t「涂突」取「突」：沸而突。"),
("傷","shāng",FY,"从人𥏻省聲：創傷，皮肉破損（《說文》）；未成人曰殤。","sh「失收」取「失」：皮破而失。"),
("瘍","yáng",FY,"从疒昜聲：頭瘡，盛夏熱毒，先膿後潰（《說文》）。","y取圆容：毒聚成瘡。"),
("殤","shāng",FY,"从歺傷省聲：未成人而死，分長中下殤（《說文》）。","sh取失收：夭折而失。"),
("禓","yáng",FY,"从示昜聲：道上之祭，大約為橫死青壯（《說文》）。","y取圆容：祭於道周。"),
("楊","yáng",FY,"从木昜聲：楊樹，白花成毛球，四處飛散（《說文》）。","y取圆容：絮飛而周。"),
("颺","yáng",FY,"从風昜聲：風所飛揚（《說文》）；舟徐行、簸颺去糠。","y取圆容：風旋而周。"),
("觴","shāng",FY,"从角𥏻省聲：盛滿酒的角杯，「觶實曰觴」（《說文》）。","sh取失收：酒滿而傾。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同部諧聲字分三面：日烈致熱瘡夭折（瘍／傷／殤／禓）、日出明亮灼熱（暘／陽／場／湯）、日升飛揚搖盪（楊／颺／觴），形符各定落點；只列本部字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":525,"name":"昜"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lyang3-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}（{p}）＝{xp}",
 "boundary":"源自《系統漢語》第525部「昜部」（卷八十八 昜）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡525a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡525y.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡525y.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))