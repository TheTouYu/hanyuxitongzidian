import json,io,os
D=r"web\public\cards"
def S(k,l,t): return {"key":k,"label":l,"text":t,"cites":[]}
SHU=("部頭束：从木从〇，「〇」象捆纏形，象意將散亂木柴捆在一起（《說文》「縛也，从囗木」）。轉義：捆束、聚集、控制；事情結束。辯證「娕、餗」所从實為「索」；「敕」所从為「柬」，形近而訛。音源：源自束縛聲，義音同「索」。字族①捆縛收縮②聚集③結束。")
def card(ch,py,pang,lian,sm):
    return {"char":ch,"pinyin":py,"bus":["372.束部"],"sources":["卷六十三  索.docx 372.束部"],
            "sections":[S("bengen","字根（第372部：束部）",SHU),S("xingpang","形旁·声旁",pang),
                        S("hengxiang","横向比较",lian),S("shengmu","声母义",sm)]}
rows=[
("誎","sù","誎＝言（形旁）＋束（聲旁）。《說文》「餔旋促也」——催促人快吃；《廣雅》「促也」。","③結束：誎（言）催促｜促（人）促｜催（人）催。","心母s，「失收」取「收」。"),
("梀","sù","梀＝木（形旁）＋束（聲旁）。《說文》「短椽也」；《唐韻》「赤梀，木名，可為車輞」。","①收縮：梀（木）短椽｜椽（木）椽｜輞（車）輞。","心母s，「失收」取「收」。"),
("餗","sù","餗（𩱫）＝食（形旁）＋束（聲旁）。《說文》「鼎實，惟葦及蒲」——鼎中食物。","②聚集：餗（食）鼎實｜鼎（鼎）鼎｜食（食）食。","心母s，「失收」取「收」。"),
("踈","shū","踈（疎䟽疏）＝疋（形旁）＋束（聲旁）。《玉篇》「慢也」；《廣韻》「稀踈」——疏而不密。","①收縮：踈（疋）疏稀｜疏（疋）疏｜稀（禾）稀。","審母sh，「失收」取「收」。"),
]
for ch,py,pang,lian,sm in rows:
    io.open(os.path.join(D,ch+".json"),"w",encoding="utf-8",newline="\n").write(json.dumps(card(ch,py,pang,lian,sm),ensure_ascii=False,indent=1))
print("cards",len(rows))