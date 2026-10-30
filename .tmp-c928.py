import sys,json,subprocess,os
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
ROOT=r"D:\系统汉字"
ENV=dict(os.environ); ENV["PATH"]=ROOT+r"\.runtime\mingit\cmd;"+ENV["PATH"]
def git(*a):
    r=subprocess.run([ROOT+r"\tools\git.cmd"]+list(a),cwd=ROOT,capture_output=True,env=ENV)
    return (r.stdout+b"\n"+r.stderr).decode("utf-8","replace")
N="字形：见字根字形图。"
D=[("鹿","lù",100,"象鹿形（枝角、細腿、四足）：鹿類總名；二疊為麤，表極致。","l「拢离」取「拢」：鹿群拢而离。"),
("彔","lù",101,"象刻木之形：刻木錄錄也（《說文》「刻木錄錄也」），錄之初文；引申記錄、詳錄。","l取拢离：刻攏而離。"),
("角","jiǎo",102,"象獸角形：角獸（《說文》「獸角也」），引申角落、較量。","j「聚决」取「聚」：角聚而决。"),
("爻","yáo",103,"象交叉之算籌：交也（《說文》「交也」），卦爻、交錯。","零聲母借聲：爻交錯。"),
("交","jiāo",105,"象人交脛之形：交脛也（《說文》「交脛也」），交叉、交往。","j取聚决：脛交而决。"),
("黹","zhǐ",106,"象刺繡花紋：箴縷所紩衣（《說文》「箴縷所紩衣」），刺繡、縫紉。","zh「凿总」取「凿」：線凿而聚。"),
("皛","xiǎo",107,"从三白：顯也（《說文》「顯也」），皎潔明亮。","x「续消」取「续」：白续而消。"),
("夭","yāo",108,"象人屈首之形：屈也（《說文》「屈也」），屈曲、夭折；又草木茂盛。","零聲母借聲：夭屈。"),
("方","fāng",109,"象耒形（起土之具）：併船也（《說文》「併船也」），方圓、方向。","f「附分」取「分」：耒分而附。"),
("高","gāo",112,"象臺觀高聳之形：崇也（《說文》「崇也」），高下、高大。","g「隔估」取「隔」：臺隔而高。"),
("天","tiān",115,"人頭頂上加指示符：顛也（《說文》「顛也」），頭頂、天空。","t「涂突」取「突」：頂突而涂。"),
("龍","lóng",117,"象龍形（角、大口、蜿蜒身）：鱗蟲之長（《說文》），引申帝王、雄偉。","l取拢离：龍攏而離。")]
n=0
for ch,p,num,F0,sm in D:
    fp=rf"{ROOT}\web\public\cards\{ch}.json"
    if os.path.exists(fp): print("skip",ch); continue
    sec=[{"key":"bengen","label":"字根本义","text":f"【第{num}部部首字·一級字根】"+F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":"本字为字根，其字族另见各部下列条目。","cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"本部字族与他部交叉者，见各字卡；此处只标本根义。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":num,"name":ch}],"sections":sec},open(fp,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    n+=1
print("added",n)
git("add","web/public/cards"); print(git("commit","-m","cards: 补部首卡12张(鹿彔角爻等)")[-40:])