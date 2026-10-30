import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FH="【第550部「火部」】火＝象火焰上騰之形（《說文》「燬也，南方之行，炎而上，象形」）；轉義燃燒、火氣、怒、急速；字族 耿（光）、煩（熱頭痛）、赤（火色）、焦（火所傷）、麃（火燒）。"
N="字形：古文字字形库未收。"
D=[("火","huǒ",FH,"象火焰上騰之形；引申燃燒、火氣、怒、急速。","h「豁活」取「豁」：火腾而豁。"),
("邩","huǒ",FH,"从火阝聲：地名（《說文》「地名」）。","h取豁活：地熱而豁。"),
("疢","chèn",FH,"从疒火聲：熱病也（《說文》「熱病也」）。","ch「刺持」取「持」：病熱而持。"),
("吙","huō",FH,"从口火聲：吐氣聲（《集韻》）。","h取豁活：氣出而豁。"),
("炅","jiǒng",FH,"从日火聲：見也（《說文》「見也」）；又光也。","j「聚决」取「聚」：光聚而决。"),
("煛","jiǒng",FH,"从目火聲：大目也（《說文》「大目也」）。","j取聚决：目大而聚。"),
("煚","jiǒng",FH,"从火日聲：日光也（《說文》「日光也」）。","j取聚决：日耀而聚。"),
("伙","huǒ",FH,"从人火聲：同伴、伙伴（火之分化，古兵制十人為火）。","h取豁活：人聚而豁。"),
("灶","zào",FH,"从火土聲：炊竈（竈之简化）。","z「凿总」取「凿」：炊實而凿。"),
("鈥","huǒ",FH,"从金火聲：稀土金屬元素（新造字）。","h取豁活：金名而豁。"),
("耿","gěng",FH,"从耳从火：耳著頰也（《說文》「耳箸頰也」），光明、耿直。","g「隔估」取「隔」：光隔而明。"),
("煩","fán",FH,"从頁从火：熱頭痛也（《說文》「熱頭痛也」），煩躁、繁雜。","f「附分」取「附」：熱附而分。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"火系同取「炎上、光熱」一面：炅煚言光、疢煩言熱病、耿言耳著頰之明、焦言火傷；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":550,"name":"火"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lhuo-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第550部「火部」（卷九十一 火）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡550a2026-10-24","risk":"low","claims":cl},open(r"intake\20261024-字卡550a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261024-字卡550a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))