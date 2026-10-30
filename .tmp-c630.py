import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FH="【第515部「黃部」·黃支】黃＝甲骨文从矢从或（箭杆所在之位），指矯正箭杆的刻槽石器；轉義火烤焦枯→黃色、嵌槽之狀→橫、強行整直→強橫；辯證《說文》从田从炗不確；音源為抽拉聲。"
FG="【第515部「黃部」·廣支】廣＝甲骨文从宀从黃，象四周無壁的大殿（《說文》「殿之大屋也」）；轉義廣大、寬遠；由開闊比喻心胸開闊。"
FG2="【第515部「黃部」·寅支】寅＝甲骨文象矢穿過丙形（丙為整直箭杆的柄形器），本義整直箭杆；轉義矯直則長→拉引、演進；音源借「引」。"
N="字形：古文字字形库未收。"
D=[("黃","huáng",FH,"本部字根：矢在石槽中矯直，引申黃色、橫、強橫。","h「豁活」取「豁」：火烤而豁。"),
("潢","huáng",FH,"从水黃聲：積水池（《說文》），又染潢（染紙）；水深廣貌。","h取豁活：水積而潢。"),
("蟥","huáng",FH,"从虫黃聲：金龜子、螞蟥，色皆黃。","h取豁活：蟲黃而動。"),
("簧","huáng",FH,"从竹黃聲：笙中振動之薄葉（《說文》），《釋名》「簧，橫也」——橫施於管中。","h取豁活：橫鼓而鳴。"),
("璜","huáng",FH,"从玉黃聲：半璧（《說文》），佩下之飾，作牙形相擊。","h取豁活：佩玉相擊。"),
("觥","gōng",FH,"从角黃聲：兕牛角鏤空為大杯（《說文》），取其橫置。","g「隔估」取「隔」：角中空而隔。"),
("橫","héng",FH,"从木黃聲：闌木（《說文》），引申縱橫之橫、不順理。","h取豁活：木橫而攔。"),
("廣","guǎng",FG,"本部二級字根：屋大而空，引申廣闊、擴充。","g「隔估」取「隔」：隔牆而敞。"),
("曠","kuàng",FG,"从日廣聲：明也、空明（《說文》），引申久遠。","k「口控」取「控」：空闊而控。"),
("壙","kuàng",FG,"从土廣聲：墓穴（《說文》「塹穴也」），野外空曠處。","k取口控：土空而穴。"),
("礦","kuàng",FG,"从石廣聲：銅鐵樸石（《說文》），未成器之礦；又粗獷強悍。","k取口控：石堅而控。"),
("獷","guǎng",FG,"从犬廣聲：犬兇悍不可附（《說文》），引申獷悍。","g取隔估：犬悍而隔。"),
("寅","yín",FG2,"本部二級字根：象矢穿丙矯箭，引申拉引、長；借為地支第三位。","y「柔锐」取「锐」：矢銳而引。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同部諧聲字分三面：黃族取「火烤焦黃／橫置」（潢／蟥／簧／璜／觥／橫）、廣族取「空闊／粗獷」（廣／曠／壙／礦／獷）、寅族取「拉引則長」（寅）；只列本部字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":515,"name":"黃"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lhu-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}（{p}）{xp}",
 "boundary":"源自《系統漢語》第515部「黃部」（卷八十五 匚）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡515a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡515a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡515a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))