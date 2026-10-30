import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F="【第576部「來部」】來（麦）＝甲骨文象麥有穗、莖、葉、根之形；麥秋種夏收，反於他穀，故加夊（倒止）作「麥」。轉義 適時、趕上、勤勞、賜予；音源為借音（義音同里、斤、豈、力）。"
N="字形：古文字字形库未收。"
D=[("來","lái",F,"象麥形（《說文》「周所受瑞麥來麰」），假借為行來之來。","l「拢离」取「离」：行至而离。"),
("麥","mài",F,"从來从夊：芒穀，秋種夏熟（《玉篇》），麥子。","m「蒙末」取「末」：麥熟而末。"),
("猌","yìn",F,"从犬來聲：犬張齦怒也（《說文》），犬怒。","y「远渊」取「远」：犬怒而远。"),
("憖","yìn",F,"从心來聲：問也、敬謹也（《說文》），肯從；又且也。","y取远渊：心謹而远。"),
("猍","lái",F,"从犬來聲：貍之或體（《集韻》），野貓。","l取拢离：獸伏而离。"),
("鶆","lái",F,"从鳥來聲：鶆鳩（《集韻》），鷹類。","l取拢离：鳥飛而离。"),
("婡","lái",F,"从女來聲：女字（《集韻》），女子名用字。","l取拢离：女柔而离。"),
("箂","lái",F,"从竹來聲：竹名（《集韻》）。","l取拢离：竹列而离。"),
("崍","lái",F,"从山來聲：崍山（《集韻》），邛崍山。","l取拢离：山高而离。"),
("淶","lái",F,"从水來聲：淶水（《說文》「淶水，起代郡」），河北淶源。","l取拢离：水流而离。"),
("郲","lái",F,"从邑來聲：地名（《集韻》），萊之或體。","l取拢离：邑分而离。"),
("睞","lài",F,"从目來聲：目瞳子不正也（《說文》），旁視、睞盼。","l取拢离：目側而离。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"來部同取「麥穗披折、行來適時」一面：來行、麥熟、猌犬怒、憖謹、猍貍、鶆鷹、婡女、箂竹、崍山、淶水、郲邑、睞視；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":576,"name":"來"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"llai2-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第576部「來部」（卷九十四 七）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
p=r"intake\20261024-字卡576a.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡576a{it}-2026-10-24","risk":"low","claims":cl},open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p,"--format","json")
    if "PLAN_DUPLICATE" not in out:
        print("ok claims",len(cl)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",cl[idx]["title"]); cl.pop(idx)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))