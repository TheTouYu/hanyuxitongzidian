import json,subprocess,os,glob,re
ROOT=r"D:\系统汉字"
ENV=dict(os.environ); ENV["PATH"]=ROOT+r"\.runtime\mingit\cmd;"+ENV["PATH"]
PY=ROOT+r"\.runtime\venv\Scripts\python.exe"; SH=ROOT+r"\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=ROOT,capture_output=True,env=ENV)
    return (r.stdout+b"\n"+r.stderr).decode("utf-8","replace")
def git(*a):
    r=subprocess.run([ROOT+r"\tools\git.cmd"]+list(a),cwd=ROOT,capture_output=True,env=ENV)
    return (r.stdout+b"\n"+r.stderr).decode("utf-8","replace")
N="字形：古文字字形库未收。"
F0="【第594部「彡部」】㐱（二級字根）＝从人从彡，彡亦聲：从「人」指人身上的毛髮、皺紋、疙瘩、斑點、氣色、脈息等一切細微生理特徵；「診」之初文。《說文》「稠髮也」失之片面——指髮者別為「髟」。轉義 顯明、告示、驗視。"
D=[("㐱","zhěn",F0,"从人从彡，彡亦聲：人身上細微生理特徵；或楷作𠘱，「新生羽而飛」，《說文》所釋亦非；與「尿」从三點形近，或同源。","zh「凿总」取「凿」：細徵而凿。"),
("駗","zhěn","【第594部「彡部」】㐱系；駗＝从馬㐱聲，馬載重難也。","从馬㐱聲：馬載重難也（《說文》「馬載重難也」），負重難行。","zh取凿总：馬重而凿。"),
("䪾","zhěn","【第594部「彡部」】㐱系；䪾＝从頁㐱聲，顏色䪾䫰，慎事也。","从頁㐱聲：顏色䪾䫰，慎事也（《說文》），面容審慎。","zh取凿总：色慎而凿。"),
("袗","zhěn","【第594部「彡部」】㐱系；袗＝从衣㐱聲，玄服也。","从衣㐱聲：玄服也（《說文》「玄服」），單衣、華美之衣。","zh取凿总：衣玄而凿。"),
("飻","tiè","【第594部「彡部」】㐱系；飻＝从食㐱聲，貪食也。","从食㐱聲：貪也（《說文》「貪也」），貪食。","t「涂突」取「涂」：食貪而突。"),
("餮","tiè","【第594部「彡部」】㐱系；餮＝貪食之名，《左傳》「貪財為饕，貪食為餮」。","从食殄省聲：貪食也；饕餮，貪財貪食之獸。","t取涂突：食貪而突。"),
("髟","biāo","【第594部「彡部」】髟＝从長从彡，長髮猋猋，髮部之首。","从長从彡：長髮猋猋也（《說文》「長髮猋猋也」），凡髮屬皆从髟。","b「闭剥」取「闭」：髮長而闭。"),
("髮","fà","【第594部「彡部」】髟系；髮＝从髟犮聲，根也。","从髟犮聲：根也（《說文》「根也」），人髮、毛髮。","f「附分」取「附」：毛附而分。"),
("髴","fú","【第594部「彡部」】髟系；髴＝从髟弗聲，鬕也，髮飾；又仿佛。","从髟弗聲：鬕也（《說文》），首飾；通「仿佛」，隱約相似。","f取附分：飾附而分。"),
("鬢","bìn","【第594部「彡部」】髟系；鬢＝从髟賓聲，頰髮也。","从髟賓聲：頰髮也（《說文》「頰髮也」），耳前之髮。","b取闭剥：髮聚而闭。"),
("鬟","huán","【第594部「彡部」】髟系；鬟＝从髟睘聲，總髮也。","从髟睘聲：總髮也（《說文》「總髮也」），環形髮髻。","h「豁活」取「豁」：髮環而豁。"),
("肜","róng","【第594部「彡部」】肜＝从舟彡聲，商祭名，祭之明日又祭。","从舟彡聲：商祭名（《爾雅》「繹，又祭也」），祭之明日又祭曰肜。","r「柔锐」取「柔」：祭續而柔。")]
rows=[]
for it in D:
    ch,p,F0_,xp,sm=it[0],it[1],it[2],it[3],it[-1]
    sec=[{"key":"bengen","label":"字根本义","text":F0_,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"本部同取「細微之紋」一面：㐱人身細徵、駗馬負重、䪾色慎、袗單衣、飻餮貪食、髟長髮、髮毛根、髴首飾、鬢頰髮、鬟總髮、肜又祭；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":594,"name":"彡"}],"sections":sec},open(rf"{ROOT}\web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
    rows.append({"id":f"lshan4-{len(rows)+1:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第594部「彡部」（卷九十七 殸）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
git("add","web/public/cards"); print(git("commit","-m","cards: 594彡部㐱髟系12字")[-60:])
p2=ROOT+r"\intake\20261024-字卡594d.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡594d{it}-2026-10-24","risk":"low","claims":rows},open(p2,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p2,"--format","json")
    if "PLAN_DUPLICATE" not in out: print("ok",len(rows)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",rows[idx]["title"]); rows.pop(idx)
bd=os.path.basename(sorted(glob.glob(ROOT+r"\data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=re.search(r'"content_hash":\s*"([0-9a-f]{64})"',run("bundle-status",bd,"--format","json")).group(1)
print("bundle",bd); run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); print("err",json.loads(run("validate","--format","json")).get("errors"))
git("add","knowledge","data/knowledge","intake/20261024-字卡594d.json"); print(git("commit","-m","knowledge: 594彡部㐱髟系12条")[-60:])