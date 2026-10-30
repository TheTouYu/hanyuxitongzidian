import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F="【495 丁部】丁＝象釘子之形，為「釘」之初文；轉義成年男子（壯丁）、天干第四位、當、遭逢。部內从丁諸字取「釘、當、遭逢」三面。"
N="字形：古文字字形库未收。"
D=[("丁","dīng",F,"本部部首字：象釘形→釘子、壯丁、天干丁、當值。","d「囤动」取「囤」：釘囤入木。"),
("正","zhèng",F,"从止从囗（邑）：象向城邑行進，征伐之「征」初文，引申正當、糾正、端正。","zh「凿总」取「凿」：行止皆中。"),
("定","dìng",F,"从宀从正：居室安定（《說文》「安也」），引申決定、必定。","d取囤：宀下定止。"),
("成","chéng",F,"从戊从一：象斧劈物而使析離，本義成就、完成（《說文》「就也」）。","ch「刺持」取「持」：持斧而成。"),
("城","chéng",F,"从土成聲：築土為牆以成邑，取成之成就義。","ch取持：土持而成垣。"),
("誠","chéng",F,"从言成聲：言實無偽曰誠，取成之實義。","ch取持：言持而實。"),
("頂","dǐng",F,"从頁丁聲：頭之最上（《說文》「顛也」），引申頂戴、頂替。","d取囤：首囤而居上。"),
("訂","dìng",F,"从言丁聲：平議、評議（《說文》「平議也」），引申訂立。","d取囤：言囤而平。"),
("釘","dīng",F,"从金丁聲：丁之加金者，本字作丁，後增金旁。","d取囤：金屬囤入。"),
("叮","dīng",F,"从口丁聲：反覆囑咐，取丁之當值、盯住義。","d取囤：聲囤而繞。"),
("打","dǎ",F,"从手丁聲：擊也（本義撞擊），取丁之當值。","d取囤：手囤而擊。"),
("朾","chéng",F,"从木丁聲：木柱、撞擊（《說文》「撞也」）。","ch取持：木持而撞。"),
("疔","dīng",F,"从疒丁聲：形小而根深如釘之惡瘡。","d取囤：毒囤肉中。"),
("酊","dǐng",F,"从酉丁聲：「酩酊」，醉甚。","d取囤：醉囤而倒。"),
("耵","dīng",F,"从耳丁聲：「耵聹」，耳中垢。","d取囤：垢囤耳道。")]
cl=[]
for i,(ch,p,F0,xp,sm) in enumerate(D,1):
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取丁部「釘子、當值、遭逢」一面：土取其築，言取其平，頁取其顛。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
    cl.append({"id":f"lcs-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
      "boundary":"源自《系統漢語》第495部丁部（卷八十一 釘）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
json.dump({"schema_version":1,"intent":"字卡495a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡495a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡495a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out, "cards:", len(cl))
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))