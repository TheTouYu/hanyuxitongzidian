import json,subprocess,os,glob
B7=("部首启（𢼄啟啓唘𠶶qǐ）：从戶从口，象意門被打開；《說文》「启，開也」。𢼄之甲骨文从戶从又（用手開門）；周代或从戶从攴，本應是「𠶶」，指打門。"
    "轉義：開發開始、教導開導、別與分移、看與白色、跪跽（《爾雅》啓，跪也）。音源：源自開門聲；因有跪跽義，或義音同「己」。字族衍義：指開門，表示打開、開始。")
N="字形：古文字字形庫未收；原稿該部有「▲《瑞應圖》局部（南宋 李嵩）」「▲刹車示意圖」等圖，可參。"
D=[
("綮","qǐ",B7,"从糸𢼄聲，《說文》「㨖繒也；一曰幑幟，信也，有齒」（康禮切），細密絲織品或出入憑信；qìng 肯綮，肋肉結處、比喻關鍵。","主組：絲織細密而分齒如符信，以糸定落點。","q「親缺」取「缺」：齒缺而為信。"),
("䁈","qì",B7,"从目啓省聲，《說文》「省視也」（苦系切）；《玉篇》窺也，同䁉。","主組：開目而視，以目定落點。","q「親缺」取「缺」：目缺而窺。"),
("晵","qǐ",B7,"从日啟省聲，《說文》「雨而晝夝也」（康禮切）——雨後放晴，天開啟之意。","主組之妙：雲開而天啟，正「開門」之喻，以日定落點。","q「親缺」取「缺」：雲缺而見日。"),
("闙","qǐ",B7,"从門啟聲，《集韻》「開門也，通作啓」。","主組之直：以門定落點，開門即闙。","q「親缺」取「缺」：門缺而開。"),
("肁","zhào",B7,"从戶从聿，《說文》「始開也」；《玉篇》始也、謀也。","主組：以手持筆（聿）而戶始開，開端之象。","zh「鑿總」取「鑿」：鑿戶而始。"),
("肇","zhào",B7,"从攴肈省聲，《說文》「擊也」（治小切）；《集韻》通作肈；《爾雅》肈，敏也；《玉篇》長也、戟屬。","主組：打門之擊（攴），與𠶶同源，以攴定落點。","zh「鑿總」取「鑿」：擊而破。"),
("𨌋","qǐ",B7,"从車启聲，《集韻》引《說文》「礙也」，一曰至也——刹車。","主組：車行而止，如門之闔，以車定落點（原稿配刹車示意圖）。","q「親缺」取「缺」：輪缺而止。"),
("𢩙","líng",B7,"《字彙補》「古文靈字」。","主組：古文異體，記其為靈之古字，不強解形。","l「攏離」取「攏」：神攏而靈。"),
("启","qǐ",B7,"部頭本字（已具卡）。","—","—"),
]
D=D[:8]
def card(ch,p,Bx,a,b,c):
    return {"char":ch,"pinyin":p,"bus":[],"sections":[
      {"key":"bengen","label":"字根本義","text":Bx,"cites":[]},
      {"key":"zigen","label":"字形","text":N,"cites":[]},
      {"key":"xingpang","label":"形旁声旁","text":a,"cites":[]},
      {"key":"hengxiang","label":"横向对照","text":b,"cites":[]},
      {"key":"shengmu","label":"声母义","text":c,"cites":[]}]}
for ch,p,Bx,a,b,c in D:
    json.dump(card(ch,p,Bx,a,b,c),open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("写卡",len(D))
ST={"綮":"《说文》「㨖缯也；一曰幑帜，信也，有齿」，细密丝织品或出入凭信；qìng 肯綮，肋肉结处、比喻关键。","䁈":"《说文》「省视也」；《玉篇》窥也，同䁉。","晵":"《说文》「雨而昼夝也」——雨后放晴，天开启之意。","闙":"《集韵》「开门也，通作啓」。","肁":"从户从聿，《说文》「始开也」；《玉篇》始也、谋也。","肇":"从攴肈省声，《说文》「击也」；《集韵》通作肈；《尔雅》肈，敏也。","𨌋":"《集韵》引《说文》「碍也」，一曰至也——刹车。","𢩙":"《字彙补》「古文灵字」。"}
BK="源自《系統漢語》第397部「启部」；字卡五步规程。"
cl=[{"id":f"bte-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{d[0]}（字卡）",
   "statement":f"{d[0]}（{d[1]}）：{ST[d[0]]}","boundary":BK,"permission":"public",
   "fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,d in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡397启部清2026-10-23","risk":"low","claims":cl},
          open(r"intake\20261023-字卡397启部清.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡397启部清.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    b=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",b,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",b,"--apply","--content-hash",h); run("bundle-apply",b,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",b,"err",v.get("errors"))