import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F="【511 心部】心＝象心臟形，本義心臟；轉義心思、感情、中心。部內从心諸字皆以心為義符，聲符給具體情狀，故同一心理而有喜怒哀懼之別。"
N="字形：古文字字形库未收。"
D=[("志","zhì",F,"从心之聲：心之所之曰志（《說文》「意也」），引申志向、記述。","zh「凿总」取「凿」：意鑿而定向。"),
("忠","zhōng",F,"从心中聲：中心曰忠（《說文》「敬也」），引申忠誠。","zh取凿：中直如鑿。"),
("忌","jì",F,"从心己聲：憎惡、忌妒（《說文》「憎惡也」），引申禁忌。","j「聚决」取「决」：心決而拒。"),
("忘","wàng",F,"从心亡聲：不識也（《說文》「不識也」），取亡之失。","w?零聲母：取借聲。"),
("忍","rěn",F,"从心刃聲：能也、堪也（《說文》「能也」），引申殘忍。","r「柔锐」取「锐」：刃銳而忍。"),
("忽","hū",F,"从心勿聲：不注意（《說文》「忘也」），引申忽然、迅速。","h「豁活」取「豁」：豁然而過。"),
("怠","dài",F,"从心台聲：慢也、惰也（《說文》「慢也」）。","d「囤动」取「囤」：氣囤而滯。"),
("惟","wéi",F,"从心隹聲：思考（《說文》「凡思也」），借為僅、但是。","w?零聲母。"),
("惰","duò",F,"从心隋聲：不敬、懶（《說文》「不敬也」）。","d取囤：心囤而墮。"),
("意","yì",F,"从心从音：察言而知意（《說文》「志也」），引申意思、意料。","y「柔锐」取「锐」：音銳入心。"),
("愚","yú",F,"从心禺聲：禺即猴，猴之性鈍；本義愚笨（《說文》「戇也」）。","y取柔锐：性柔而鈍。"),
("慈","cí",F,"从心茲聲：愛也（《說文》「愛也」），上愛下曰慈。","c「刺持」取「持」：心持而愛。"),
("慧","huì",F,"从心彗聲：聰也（《說文》「儇也」），取彗之掃除明淨。","h取豁活：心豁而明。"),
("想","xiǎng",F,"从心相聲：冀思也（《說文》「冀思也」），取相之審視。","x「续消」取「续」：思續而相。"),
("愁","chóu",F,"从心秋聲：憂也（《說文》「憂也」），秋氣肅殺故愁。","ch取刺持：秋氣刺心。")]
cl=[]
for i,(ch,p,F0,xp,sm) in enumerate(D,1):
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同以心為義符，聲符各給一情：之定向、中守正、己拒斥、刃堪忍。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
    cl.append({"id":f"ldc-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}（{p}）{xp}",
      "boundary":"源自《系統漢語》第511部心部（卷八十四 心）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
json.dump({"schema_version":1,"intent":"字卡511b2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡511b.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡511b.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out, "n:", len(cl))
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))