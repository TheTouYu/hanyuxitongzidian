import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F="【511 心部】心＝象心臟形，本義心臟；轉義心思、感情。部內从心諸字以心為義符，聲符各給一情：慕思、憲法、愆過、懲止，皆由心發。"
N="字形：古文字字形库未收。"
D=[("慕","mù",F,"从心莫聲：習也、思慕（《說文》「習也」），莫有日暮不見之義。","m「蒙末」取「蒙」：心蒙而慕。"),
("憲","xiàn",F,"从心从目，害省聲：敏也（《說文》「敏也」），引申法憲。","x「续消」取「续」：目續而察。"),
("愆","qiān",F,"从心衍聲：過也（《說文》「過也」），衍有漫衍過度之義。","q「亲缺」取「缺」：心缺而過。"),
("懲","chéng",F,"从心徵聲：㣻也、止也（《說文》「㣻也」），懲前毖後。","ch「刺持」取「持」：心刺而止。"),
("憊","bèi",F,"从心備聲：疲極（《說文》「𢢞也」）。","b「闭剥」取「闭」：氣閉而憊。"),
("惕","tì",F,"从心易聲：敬也、懼也（《說文》「敬也」）。","t「涂突」取「突」：心突而惕。"),
("悚","sǒng",F,"从心束聲：懼也（《說文》「懼也」），束而心緊。","s「失收」取「收」：心收而悚。"),
("惋","wǎn",F,"从心宛聲：驚歎、悵恨。","w?零聲母。"),
("懣","mèn",F,"从心滿聲：煩也（《說文》「煩也」），氣滿而懣。","m取蒙末：氣蒙而懣。"),
("懃","qín",F,"从心勤聲：勉也、勞也。","q取亲缺：力勤而心親。"),
("愍","mǐn",F,"从心敃聲：痛也（《說文》「痛也」），同「憫」。","m取蒙末：痛蒙於心。"),
("憫","mǐn",F,"从心閔聲：憐也、憂也，取閔之惜。","m取蒙末：心蒙而憫。"),
("憨","hān",F,"从心敢聲：愚也、癡也。","h「豁活」取「豁」：心豁而憨。"),
("懇","kěn",F,"从心貇聲：誠也、懇切。","k「口控」取「控」：心控而懇。"),
("戀","liàn",F,"从心䜌聲：思也、愛戀（《說文》「思也」）。","l「拢离」取「拢」：心攏而不離。")]
cl=[]
for i,(ch,p,F0,xp,sm) in enumerate(D,1):
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同以心為義符：莫取日暮、衍取漫過、徵取驗止、滿取氣盈。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
    cl.append({"id":f"lde-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}（{p}）{xp}",
      "boundary":"源自《系統漢語》第511部心部（卷八十四 心）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
json.dump({"schema_version":1,"intent":"字卡511d2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡511d.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡511d.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out, "n:", len(cl))
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))