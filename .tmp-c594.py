import json,subprocess,os,glob
F="【478 袁部】袁＝甲骨文从衣从又（又指手），象脫衣之狀，如沒有穿衣的人，或在上面加「○」表其頭圓並兼聲；是「猿」的初文（猩猩、長臂猿，體大無頰囊無尾，更像人）。因猿善攀援，引申攀援、遙遠。音源字，取猿猴叫聲。部内「睘」从目袁聲，本指猴面鷹（草鴞）。"
N="字形：古文字字形库未收。"
D=[("袁","yuán",F,"本部部首字：脫衣之人／猿之初文；引申攀援、遙遠、姓氏。","y「续消」取「续」：援引相續。"),
("遠","yuǎn",F,"从辵袁聲：路遥為遠，取猿攀之遠。","y取续：行續而遠。"),
("園","yuán",F,"从囗袁聲：四周有垣的菜果林木之地，取袁之圍合。","y取续：木續成園。"),
("猿","yuán",F,"从犬袁聲：與猴相比體大、無頰囊、無尾，更像人。","y取续：攀續而行。"),
("睘","qióng",F,"从目袁聲：猴面鷹（草鴞），臉盤如猿、目不能轉須轉頸270°；引申驚視、憂愁孤獨。","q「亲缺」取「亲」：轉頸而親。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取袁部「脫衣似猿、攀援致遠」两面：辵取其遠，囗取其圍，犬取其形，目取其驚視。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lcf-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第478部袁部（卷七十八 夒）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡478a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡478a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡478a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))