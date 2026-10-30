import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
N="字形：古文字字形库未收。"
N594="【第594部「彡部」】彡＝三丿（或四丿），象細長而多之物（毛髮、皺紋、紗線、紋飾、光線）；《說文》「毛、飾、畫也」，借音同「占」「幵」「林」。"
D=[("繖","sǎn","【第593部「林部」】㪔＝从攴从林，敲擊林木使果葉四散；繖＝从糸散聲，蓋也（《說文》新附），傘蓋。","从糸散聲：蓋也（《說文》「蓋也」），傘蓋，《集韻》或从巾作傘。","s「失收」取「失」：蓋張而收。"),
("䉈","sǎn","【第593部「林部」】㪔族；䉈＝桃枝竹（《博雅》「䈓䉈，桃枝竹也」）。","从竹散聲：桃枝竹，節短而葉如小棕櫚（《桂海虞衡志》）。","s取失收：竹散而收。"),
("鏾","sǎn","【第593部「林部」】㪔族；鏾＝弩機鬆弛（《廣韻》「弩牙緩也」），又閹割。","从金散聲：弩也（《玉篇》），弩牙鬆弛；俗謂去勢曰鏾。","s取失收：機散而收。"),
("撒","sǎ","【第593部「林部」】㪔族；撒＝播撒、散佈（《集韻》引《說文》「䊝𥻦，散之也」）。","从手散聲：播撒、散佈，放開、張開；俗㪔字，撒手、撒潑。","s取失收：手散而收。"),
("潸","shān","【第593部「林部」】㪔族；潸＝涕流皃（《說文》「涕流皃」）。","从水散省聲：淚流皃（《說文》引《詩》「潸焉出涕」）。","sh「失收」取「失」：淚下而收。"),
("霰","xiàn","【第593部「林部」】㪔族；霰＝稷雪，小米般的雪粒（《釋名》「水雪相搏，如星而散」）。","从雨散聲：稷雪也（《說文》），雨雪雜下之粒。","x「续消」取「续」：雪粒續而消。"),
("潵","sàn","【第593部「林部」】㪔族；潵＝水散也（《集韻》），灑水。","从水散聲：水散也（《集韻》），灑水、撒落。","s取失收：水散而收。"),
("𩀼","sàn","【第593部「林部」】㪔族；𩀼＝繳𩀼，弋射（《說文》「繳𩀼也」）。","从隹散聲：繳以取鳥（《說文》），群鳥飛散。","s取失收：鳥散而收。"),
("三","sān",N594,"三＝三根算籌的排列（《說文》「天地人之道也。从三數」），表數三，亦可視「一」之三疊表多、連續。从三數：算籌三劃，數字三；義音同「參」。","s「失收」取「收」：籌三而收。"),
("衫","shān",N594,"从衣彡聲：衣也（《說文》「衣也」），衣服統稱，亦指短袖單衣（《釋名》「芟也」）。","从衣彡聲：衣之通稱，短袖單衣，取彡之細薄。","sh取失收：衣薄而收。"),
("彪","biāo",N594,"从虎彡聲：虎文也（《說文》「虎文也」），虎紋斑斕。","从虎彡聲：虎文，取彡之紋理細多。","b「闭剥」取「剥」：紋剝而闭。"),
("彤","tóng",N594,"从丹彡聲：丹飾也（《說文》「丹飾也」），以丹漆文飾。","从丹彡聲：丹飾，取彡之畫紋。","t「涂突」取「涂」：丹涂而突。")]
for ch,p,F0,*rest in D:
    xp,sm = rest[0], rest[-1]
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"本批分两部：㪔族 繖（蓋）䉈（桃枝竹）鏾（弩弛）撒（播散）潸（淚流）霰（雪粒）潵（水散）𩀼（弋射）皆取「散開、零碎」一面；彡部 三（籌三）衫（衣薄）彪（虎紋）彤（丹飾）皆取「細長而多之紋」一面。只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":594,"name":"彡"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lshan1-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{it[0]}·{it[1]}","statement":f"{it[0]}：{it[-2]}","boundary":"源自《系統漢語》第593部「林部」／第594部「彡部」（卷九十七 殸）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,it in enumerate(D,1)]
p2=r"intake\20261024-字卡594a.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡594a{it}-2026-10-24","risk":"low","claims":cl},open(p2,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p2,"--format","json")
    if "PLAN_DUPLICATE" not in out:
        print("ok claims",len(cl)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",cl[idx]["title"]); cl.pop(idx)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))