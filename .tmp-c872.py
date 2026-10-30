import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F="【第587部「幺部」】幺＝象蠶吐絲（兩股相交）；幼支＝从力幺聲（力氣小，指小孩）：少也（《說文》），引申 嫩弱、精微美好、軟曲；字族取「幽暗黑色／聲音細小幽靜／形態柔曲細弱」三面。"
N="字形：古文字字形库未收。"
D=[("𢩃","yòu",F,"从采从幼省：同釉（《漢典》），陶器光澤。","y「续消」取「续」：色光而续。"),
("𤤬","yòu",F,"从玉幼聲：音幼（《龍龕》），玉名。","y取续消：玉細而续。"),
("𤱎","yǒu",F,"从土幼聲：黑壤（《集韻》「音黝，黑壤」）。","y取续消：土黑而续。"),
("𥹱","yāo",F,"从米幼聲：米未熟（《五侯鯖字海》）。","y取续消：米生而续。"),
("鴢","yāo",F,"从鳥幼聲：鳥名（《爾雅》「鴢頭鵁似鳧，足近尾，略不能行」）；《山海經》青要山之鳥，食之宜子。","y取续消：鳥小而续。"),
("䱂","yǒu",F,"从魚幼聲：魚名（《說文》「讀若幽」），鰌類（沙鰍，短闊口、大頭岐尾）。","y取续消：魚潛而续。"),
("𣢜","yǒu",F,"从欠幼聲：愁皃（《說文》）；又呦之或體，鹿鳴。","y取续消：氣出而续。"),
("怮","yòu",F,"从心幼聲：憂皃（《說文》），含怒不言；又心戾。","y取续消：心憂而续。"),
("聈","yǒu",F,"从耳幼聲：幽靜深遠（《字彙》）。","y取续消：耳靜而续。"),
("䬀","yǒu",F,"从風幼聲：䬀𩖴，風聲（《廣韻》），緒風。","y取续消：風微而续。"),
("軪","āo",F,"从車幼聲：軪軋，奇皃（《廣韻》）；又車相戛聲。","a「隔估」取「隔」：車戛而隔。"),
("詏","yào",F,"从言幼聲：言逆也（《集韻》）。","y取续消：言逆而续。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"幼支同取「幽暗、幽靜、柔曲」一面：𢩃釉光、𤤬玉、𤱎黑壤、𥹱生米、鴢鳥、䱂沙鰍、𣢜愁、怮憂、聈幽靜、䬀風聲、軪車聲、詏言逆；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":587,"name":"幺"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lyao2-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第587部「幺部」（卷九十六 雀）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
p=r"intake\20261024-字卡587b.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡587b{it}-2026-10-24","risk":"low","claims":cl},open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p,"--format","json")
    if "PLAN_DUPLICATE" not in out:
        print("ok claims",len(cl)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",cl[idx]["title"]); cl.pop(idx)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))