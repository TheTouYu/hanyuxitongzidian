import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FH="【第516部「行部」·行支】行＝甲骨文象交叉的十字路，本指四達的大道（《爾雅》「道也」）；轉義行走、行列、行業、行跡；辯證《說文》析為彳、亍二部不確；音源為道上行走聲，由縱橫狀而義音同「黃」。"
FY="【第516部「行部」·延支】延（㢟）＝从止彳聲（沿路前行）與𢓊（从彳止聲，踩出路來，徙之初文）同源兩寫；戰國古文加丿作延；轉義長、遠、伸長、拖延。"
N="字形：古文字字形库未收。"
D=[("行","xíng",FH,"本部字根：四達之大道，引申行走、行列、行業。","x「续消」取「续」：路續而不斷。"),
("彳","chì",FH,"小步（《說文》「象人脛三屬相連」），與亍合而為行。","ch「刺持」取「持」：蹠步而持。"),
("亍","chù",FH,"步止（《說文》从反彳），左步為彳、右步為亍。","ch取刺持：止步而持。"),
("荇","xìng",FH,"从艸杏聲（或从行）：荇菜，葉浮水面，取四處可飄之意。","x取续消：水葉續生。"),
("洐","xíng",FH,"从水从行：溝水暢行（《說文》）。","x取续消：水行不斷。"),
("珩","héng",FH,"从玉行聲：佩上之橫玉（《說文》），所以節行止。","h「豁活」取「豁」：橫玉豁然。"),
("衡","héng",FH,"从角从大、行聲：綁牛角之橫木（《說文》），引申衡量、平衡。","h取豁活：橫木而攔。"),
("桁","héng",FH,"从木行聲：屋樑上橫木（《玉篇》），今稱檁；又加頸之械。","h取豁活：木橫而承。"),
("裄","háng",FH,"从衣行聲：衣之緣邊（《集韻》「緣也」），以針粗縫綴絮。","h取豁活：緣邊而縫。"),
("延","yán",FY,"从㢟加丿：道路延伸，引申長遠、鋪陳、拖延。","y「柔锐」取「锐」：延而銳進。"),
("筵","yán",FY,"从竹延聲：鋪地竹席（《說文》）、席位；言其長。","y取柔锐：席展而平。"),
("誕","dàn",FY,"从言延聲：詞語荒誕誇張（《說文》「詞誕也」），引申誕生。","d「囤动」取「囤」：言漫而囤。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同部諧聲字分二面：行族取「道／橫設」（行／彳／亍／荇／洐／珩／衡／桁／裄）、延族取「長遠／放任」（延／筵／誕）；只列本部字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":516,"name":"行"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lxing-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}（{p}）{xp}",
 "boundary":"源自《系統漢語》第516部「行部」（卷八十五 匚）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡516a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡516a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡516a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))