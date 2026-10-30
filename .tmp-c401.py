import json,subprocess,os,glob
B=("部頭丌（jī）：象低矮平整的托盤形，可獨立為器以端送小物，也可作器皿底座，故多作表示平整的音義符號；《說文》「下基也，薦物之丌」讀若箕。"
   "音源：借音字，義音同「己」（堆疊物體）。字族衍義：①薦物根基 ②同「其」指箕或箕狀物 ③同「其」指紋路交織 ④形近「斤」之訛。")
N="字形：古文字字形庫未收；原稿該部有「▲鎏金麒麟印紐（唐）」「▲《祭神》（清 陳枚）」二圖，可參。"
D=[
("𥾎","qí","从糸亓聲，即綦：《廣韻》「履飾，又蒼白色巾」；jī 為綨，《玉篇》「雜文也」。","③組：絲縷交織成文，以糸定落點。","q「親缺」取「親」：絲相交而親。"),
("𦬟","qí","从艸亓聲，即萁：《說文》「豆莖也」；《廣韻》「菜似蕨」，《集韻》「薌萁，粱也」。","②組：豆莖叢生如箕，以艸定落點。","q「親缺」取「親」：莖葉相依。"),
("𩵧","qí","从魚亓聲，即鯕：《說文》「魚名」，《正字通》「鯿魚」——體側扁如箕。","②組：魚體扁如箕，以魚定落點。","q「親缺」取「親」：群魚相親。"),
("𣍣","qí","从月亓聲，即期：《說文》「會也」，一曰限也、要也。","③組：日月相會為期，正「交會」之落點——以月定類。","q「親缺」取「親」：日月相親而會。"),
("𪊔","qí","从鹿亓聲，即麒：《說文》「仁獸也，麋身牛尾一角」；古通作畁。","②組：麟身有紋，兼「交織」一面；原稿配鎏金麒麟印紐圖。","q「親缺」取「親」：瑞獸相親。"),
("㫅","qí","从㫃亓聲，即旗（旂），《字彙補》「與旗同」。","④組：形近「斤」之訛？實為㫃旁訛——記作讹變借形，不涉丌之取義。","q「親缺」取「親」：旗依風而親。"),
("𪗞","qí","从齒亓聲，即䶞：《集韻》「齧也」，古作𪗞；《正字通》謂譌字（即齗）。","④組：記咬齧一義，形近而讹，不強解取義。","q「親缺」取「親」：齒相親而齧。"),
]
def card(ch,p,a,b,c):
    return {"char":ch,"pinyin":p,"bus":[],"sections":[
      {"key":"bengen","label":"字根本義","text":B,"cites":[]},
      {"key":"zigen","label":"字形","text":N,"cites":[]},
      {"key":"xingpang","label":"形旁声旁","text":a,"cites":[]},
      {"key":"hengxiang","label":"横向对照","text":b,"cites":[]},
      {"key":"shengmu","label":"声母义","text":c,"cites":[]}]}
for ch,p,a,b,c in D:
    json.dump(card(ch,p,a,b,c),open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
BK="源自《系統漢語》第391部「丌部」；字卡五步规程。"
ST={
"𥾎":"即綦，《廣韻》「履飾，又蒼白色巾」；jī 為綨，《玉篇》「雜文也」——絲縷交織成文。",
"𦬟":"即萁，《說文》「豆莖也」；《廣韻》「菜似蕨」，《集韻》「薌萁，粱也」。",
"𩵧":"即鯕，《說文》「魚名」，《正字通》「鯿魚」，體側扁如箕。",
"𣍣":"即期，《說文》「會也」，一曰限也、要也——日月相會為期。",
"𪊔":"即麒，《說文》「仁獸也，麋身牛尾一角」，古通作畁；原稿配「鎏金麒麟印紐（唐）」圖。",
"㫅":"《字彙補》「與旗同」，即旂；㫃旁形近而讹，记作讹变借形。",
"𪗞":"即䶞，《集韻》「齧也」，古作𪗞；《正字通》謂譌字（即齗）。",
}
cl=[{"id":f"bt7-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{d[0]}（字卡）",
     "statement":f"{d[0]}（{d[1]}）：{ST[d[0]]}",
     "boundary":BK,"permission":"public","fact_classes":["evidence_scope"],
     "duplicate_resolution":"create_distinct_with_boundary"} for i,d in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡391丌部尾2026-10-23","risk":"low","claims":cl},
          open(r"intake\20261023-字卡391丌部尾.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡391丌部尾.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    b=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",b,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",b,"--apply","--content-hash",h); run("bundle-apply",b,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",b,"err",v.get("errors"))