---
name: hanzi-card
description: 在「系统汉字」库为一个汉字建卡或补卡（部头、二级字根、三级族字）：定位原稿段落、切字形图、写 JSON 卡、跑全部校验、支持多 agent 并行建整部。当主人说「建某字」「补某部」「把某字加进去」「这字怎么落点」时使用。
whenToUse: 主人要求新增/修订字卡、续建某一部、给族表补字、修落点或释义时；也用于回答「某卡为什么这样写」的溯源，以及把一部拆给多个 agent 并行建卡。
---

# 建汉字卡：可并行的标准产线

目标：原稿怎么写的，卡就怎么落；一步一验，不靠事后补救。
**卡是产物，原稿是唯一真源；任何一栏都不许自己发挥。**

全流程分两段：**单卡手艺**（§1–§7）与**并行产线**（§8 核验、§9 拆单/合并）。
一个人建一张卡只走 §1–§8；建一整部、或要几个 agent 同时做，就加 §9。

## 0. 开工前必读（按序，别跳）

1. `AGENTS.md` —— 硬规则（知识只走 pkc、禁手改 knowledge/、中文、结论先行）。
2. `memory/OPERATING.md` —— 主人授权范围（日常建卡不必再问；删知识、改旧正文/边界、重组主题要先说明）。
3. `memory/CURRENT.md` 顶部 —— 当前进度与最近提交。
4. `memory/HANDOFF.md` §一（产线）、§二（八类错误）、§三（待办）。
5. `prompts/exegesis.md` —— 栏序、引文体例、落点铁律（**与本文冲突时以 exegesis 为准**，改完回来同步本文）。

## 1. 判型与选题：这张卡是几级、属于哪部

### 1.1 部号只认原稿编号标题

- 原稿每个部以 `NNN.某部` 开头（如 `308.㒳部`、`309.面部`）。`NNN` 就是 `bus.num`，`某` 就是 `bus.name`。
- 部头字从紧随其后的字头段取：`（异体…拼音）：` 开头、后面接本義/轉義/辯證/音源/字族衍義的那一段。
- **部名与部头字可以不同**（308 部名「㒳」，部头是「兩」）：`bus.name` 用部名，卡文件名、`char`、页面路由用部头字。
- 卷名进 `suoshujuan`：`{"t":"卷","ch":"卷五十四网","label":"卷五十四网"}`（卷名去空格；卷五十四 网 → 卷五十四网）。

### 1.2 源稿从哪来

- 源稿根目录：`D:/字谱智能体/<卷>.docx`；卷名与文件名对照见 `memory/CURRENT.md` 的「书的结构」一条（卷五十四 = `卷五十四  网.docx`，注意文件名里是两个空格）。
- 纯文本缓存：`web/.cache/txt/<卷>.txt`（如 `web/.cache/txt/卷五十四  网.txt`），一行≈一个 docx 段；**行号≠python-docx 段号**，通常只差几个空段。
- 缓存没有或对不上：`.runtime\python\python.exe tools/docx2txt.py <docx>`（stdlib zipfile+正则）。
- **不要 pip 装 python-docx**：venv 里没有、离线装不上；`load_workspace_dependencies` 在本机会 EPERM。要图/段落就自己用 `zipfile`＋`lxml`/正则解析。
- 控制台 GBK：跑脚本前 `$env:PYTHONIOENCODING='utf-8'`，输出重定向到文件再读，否则 `UnicodeEncodeError`。

### 1.3 三级判据

| 级 | 判据（看原稿段落结构） | JSON |
|---|---|---|
| 1 部头 | `NNN.某部` 后第一个字头段，后接本義/轉義/辯證/音源/字族衍義 | `level:1`，全套栏 |
| 2 二级字根 | 部内另一个独立字头段（起法同部头），有自己的本義、字族表；部头卡的 `erji.links` 要挂它 | `level:2`，`parent`／`rootChain` |
| 3 族字 | 只在别人的族表里出现一行（字（异体）＋拼音＋类属＋引文释义） | `level:3`，`parent`，只有 釋義＋聲母擬態＋所属卷 |

- 二级字根**不并入上级族表**，单独成卡、单独挂 erji。
- 讹字/形近字行：不建新卡，归正字（如 308 𧶪→貴）；该行落点整行照录原文，不加「——」。
- 谐声字（三级、非字根）**只有** 釋義＋聲母擬態＋所属卷；不要加 zizu/zixing。

### 1.4 跨部重复字（先查再建）

建卡前先 `glob web/public/cards/<字>.json`：

- 不存在 → 正常建。
- 已存在且 `parent` 就是本行所属字根 → 直接复用，不要重写（改动旧卡属「改旧正文」，要先向主人说明）。
- 已存在但属别部 → **不要擅自改它的 parent**。在交付说明里单列「跨部重复：X 已在 Y 部（parent=Z）」，由主人裁决；本行可暂不建卡，父卡行先照录。

## 2. 取原文：先定位段，再抄

### 2.1 五栏照录

- 本義/轉義/辯證/音源（以及头卡的 字族衍義 外框）**逐字照录**，只剥行首标签：`^(本義|轉義|辯證|音源|字形|字族衍義|聲母擬態|所属卷|釋義)[：:]`。
- **不得 `split('：')`**：引文里的冒号是内容（`《集韻》：“乘也，匹也，”`）。
- 一栏多段：按段序合并，段间 `\n`；`text` 与 `paras` 同步（新卡可省 `paras`，全库多数卡没有）。
- 抄完做一次机器比对：卡内 text 与 docx 对应段去空白后**逐字相等**，不是「包含」。
- `tools/check-cols.py` **不存在**（HANDOFF 里是旧记载），别再引用；直接写一次性 diff 脚本比对，或跑 §8 的 verify。

### 2.2 多音又音

- `pinyin` 按原稿读音顺序，多个读音用 `、` 分隔（`朷 mù、dāo、tiáo`；`㙙 máng、lǒng`）。
- 聲母擬態只取**与卡内该行释义/桥句相符的那一读**的首字母，不是机械取第一个。写完自查：`shengmu` 首字母必须等于所取读音的首字母。
- 多读各有独立义项时，橋句/释义按原稿整行照录，不拆分、不合并。

### 2.3 异体与繁简

- 字头括注里的异体，进 `aliases`（除非它自己有独立卡）。
- 繁体/异体到简体的映射**只进** `variants.json` 两张表（§7），不要塞进 `aliases` 混用。
- `head` 保留原稿括注全形（`兩（𠓜㒳两両）`），不删不改。

### 2.4 与 pkc 知识库的边界

- **字卡 JSON 不走 `pkc knowledge-plan`**：它是网页字卡数据，不是 Claim。
- 只有主人明确要求「把这个字的释义/音源录进知识库」时，才按 AGENTS.md 走 `knowledge-plan`（preview → 64 位 hash 批准 → bundle-approve/apply）。
- 不要因为建卡顺手改 `knowledge/**/*.md` 或 `data/knowledge/*.json`。

## 3. 图与资产

### 3.1 字形段怎么切

原稿字形段形如 `（异体…拼音）：[图]、[图]。[图][图][图]𠚑。[图]偭。…`。

- 按「。」分段：句号前的图归当前字头；句号后遇到**单个汉字**标签，前一组的图归这个标签字；段末最后一组归该标签。
- 图片按出现顺序存 `web/public/glyphs/<字>/NN.png`，`01` 起；同时写 `web/public/glyphs/index.json` 的 `chars[字] = {doc, variants, files}`。
- 段内括注里的单张图（如 308 P331 㒼 异体后那张）不是字形图，跳过；但**不要丢**：它往往是简化字/异体字的字体渲染图，按 §3.6 归位。
- **抽完必须核对**：`files` 数量 == 段落里该组图数；标签字不是本段字头时，不能把它的图并进本字 `files`（见 §3.2）。

现成抽取器 `tools/extract-glyphs.mjs`（零依赖 node）：

```
node tools/extract-glyphs.mjs --doc "D:/字谱智能体/卷五十四  网.docx" --only 面
```
坑：只认 png/jpg/jpeg/webp/gif（**EMF/WMF 静默丢弃**）；单图 >900KB 静默跳过（`--maxbytes` 可调）；每字最多 6 张照片；index 用单行 JSON 写。抽完看 `chars` 条数与 `files` 数，少了就补抽/转格式，不要假装齐了。

### 3.2 异体图（extra）与參證图（cankao）

- **异体标签**（标签字在本字 `variants` 里，如 兆 的 `涉`）：给该异体单建 `chars[异体] = {doc, variants:"", files:[…]}`，再在本字条目加
  `"extra": [{"char":"涉","label":"字形（涉）"}]`。页面会在本字字形行后按 label 追加这些图，图注数也算进去。
- 异体若同时是「段末只借形对照」的參證字，按下列 cankao 写，**不要再挂 extra**（否则页面同图渲染两次；309 面 的 𠚑 即此例）。
- **參證字**（他部字、或本段只借一两形来对照，如 久 借 氒、䚻 借 䍃、309 面 段末的 顏）：不要覆盖该字自己的 `files`，也不要并进本字 `files`。本段那张图另存 `web/public/glyphs/<本字>/cankao/NN.png`（或 `inline/<本字>/cankao/…`），卡里加一栏：

```json
{"key":"cankao","label":"參證字形（氒）","text":"",
 "cimgs":[{"f":"氒/21.jpg","cap":"01"},{"f":"氒/22.jpg","cap":"02"}]}
```

  `cimgs` 的 `f` 相对 `web/public/glyphs/`；可以是字符串，也可以是 `{f,cap}`（cap 是图注）。位置见下条。
- **本部已建卡的族字，其原稿图归该字自己的字形（`chars[字].files`），不列本部头的 `cankao`**：同一张图不进两个字的序列（主人 2026-11-22 裁：311 丏 部的 沔 不算參證字，删去；沔 的春秋金文即其本字字形）。
- **cankao 固定放在 `bianzheng` 之后、`yinyuan` 之前**（验收时按这个位置看，别拖到 `zixing` 后面）。
- **一栏只放一个 `cankao` 段**（verify 的 E011 拦重复段）：一组多字就合成一段，`cimgs` 按原稿顺序排。
- **`text` 一律留空**：不在參證欄写解释、分组说明或来源考订（主人 2026-11-22 明令「不需要解释，删去」）。分组靠 `cap` 标字名，如 `{"f":"𠚑/01.png","cap":"𠚑 01"}`、`{"f":"面/cankao/02.png","cap":"𬍵"}`、末形 `{"f":"面/cankao/01.png","cap":"顏"}`。
- **字体渲染的楷体单字不是古文字形**：方形画布、边缘像素完美、无出土地/器名（如 面 段末「玉+面」、308 的 㒼/01）都是排版字体直出，**删掉，不入 `files` 也不入 `cimgs`**；确需兜底的稀有字另存 `web/public/glyphs/chars/<code>.png`，不进字形序列。

### 3.3 插图（实物照片）

- **插图**＝独立图片段，下一段以「▲」开头（`▲披馬甲的唐三彩`）。归属只看段落区间：`▲` 图注段属于哪个字头的区间，图就归谁。**不许看图猜、不许按最近字头猜。**
- 文件放 `web/public/glyphs/photos/<字>/NN.jpg`；图注照录 ▲ 后文字；**原文没有 ▲ 就留空 `""`**，不许自造。
- 照片 vs 字形：`max(w,h) >= 200` 的照片进 photos，小图是字形（`tools/extract-photos.py` 的判据；该脚本依赖 python-docx，本机跑不了，逻辑照抄即可）。
- 预处理：四角亮斑水印用 `tools/delogo.py`（只认四角 `mx>=215 & sat<=45` 的亮块，MedianFilter 填充）；白边/黑边要自己裁；EMF/WMF 先转 PNG 再入库。**原稿水印不要大面积擦**（OPERATING）。
- 重复图/错主图：先比 sha256，确认没有第二处引用，再删文件与两处 index 条目。

### 3.4 index.json 的 photos 必须写全路径

`web/public/glyphs/index.json` 有**两处** photos：`chars[字].photos` 与**顶层** `photos` 映射。页面读**顶层**，且会拼 `/glyphs/` 前缀，所以：

```json
"photos": {"兩": [{"file":"photos/兩/01.jpg","caption":""}]}
```

写 `01.jpg` 会 404。`chars[字].photos` 用同形态，保持两处同步。改完**重启服务**（内存缓存 300 秒）。

### 3.5 句中形（inline）

- 引文里嵌的古文字，用占位符 `{{<栏>/NN.png}}` 原样插在文字流位置；文件存 `glyphs/inline/<字>/<栏>/NN.png`；section 加 `"gdir":"inline/<字>"`。
- 验收：卡里必须有 `{{`，页面无残留 `{{`，对应 `<img>` 返回 200。
- 一个栏里有多张时按 run 顺序编号；不要把一个占位符放在段末了事。

### 3.6 括号里的现代字图（2026-11-22 血案）

原稿常把字典里没有的字（多为简化字）用字体渲染成一张小图，塞在字形段或族表行的括号里，例如 `㒼（䓣𦲸<图>mán）` 里的 `<图>` 就是简化字 **𬜯**（29×35、1-bit、240 B），**不是古文字形**。批量抽图只按位置切，会把它排成 01。

- 识别：`max(w,h) ≤ 40` 且 PNG 位深 ≤ 2（或文件 <350 B）→ 几乎一定是字体渲染图；它一旦被写进 `glyphs/index` 的 `files` 或卡的 `gimgs`，`verify-card` 的 **E056** 就告警。
- 处置：
  1. 移到 `web/public/glyphs/chars/<小写hex>.png`（`python -c "print('%x'%ord('𬜯'))"` → `2c72f`），这是服务端 `ext()` 的稀有字兜底，页面 head 的括注会显示成图；
  2. 字符写进 head 括注与 `aliases`（如 `㒼（䓣𦲸𬜯）`）；
  3. 从 `glyphs/index.json` 的 `files` 与卡的 `gimgs` 移除，后面的图**前移重编号**（宁可少一号，不要留空号）；
  4. 简体映射进 `cards/variants.json`（`𬜯→㒼`），重建索引；
  5. 页检：本字字形数减一，`/card/<简体>` 能到本字。
- 同类：`㡭`、`㷉`、`丯`、`弁`、`彻`、`榮`、`毚`、`涅`、`看`、`裼`、`龜`、`𩯋` 等目录里还留着 15 张这种小图（多已不被 `files` 引用）；清理该字时顺带删够不着的小图，别让它们再被索引捡回去。

## 4. 写卡：JSON 骨架

以邻居卡为准抄结构，别自创字段：

- 部头样板：`web/public/cards/兩.json`
- 二级样板：`web/public/cards/㒼.json`
- 族字样板：`web/public/cards/沐.json`（最短）

### 4.1 栏序（全库实际 646:14 的惯例）

`benyi → [erji] → zhuanyi → bianzheng → [cankao] → yinyuan → shengmu → zizu → zixing → suoshujuan`

- `erji` 只在部头卡出现；`cankao` **固定紧跟 `bianzheng`**（主人 2026-11-22 定；老卡此前的 `zixing` 后会判不对）。
- 缺哪栏是原稿没有，不要硬造；全库 335 张 level1 里也有缺 zhuanyi/bianzheng/yinyuan 的——**按原稿**，不要为齐栏补写。

### 4.2 部头/二级

```json
{
 "char": "兩", "head": "兩（𠓜㒳两両）", "pinyin": "liǎng",
 "aliases": ["𠓜","㒳","两","両"],
 "bus": {"num": 308, "name": "㒳"},
 "level": 1,
 "sections": [
  {"key":"benyi","label":"本義","text":"…原稿照录…"},
  {"key":"erji","label":"本部字根","text":"","links":[{"ch":"㒼","label":"㒼（䓣𦲸）"}]},
  {"key":"zhuanyi","label":"轉義","text":"…"},
  {"key":"bianzheng","label":"辯證","text":"…"},
  {"key":"yinyuan","label":"音源","text":"…"},
  {"key":"shengmu","label":"聲母擬態","text":"l「拢离」取「拢」：…（推）。"},
  {"key":"zizu","label":"字族衍義","text":"","groups":[{"title":"①…","rows":[["字（异体）","pinyin","糸","《說文》「…」——短桥",""]]}]},
  {"key":"zixing","label":"字形","text":"","gimgs":["兩/01.png"]},
  {"key":"suoshujuan","label":"所属卷","text":"","links":[{"t":"卷","ch":"卷五十四网","label":"卷五十四网"}]}
 ],
 "photos": [{"file":"01.jpg","caption":""}]
}
```

### 4.3 族字（level 3）

```json
{"char":"緉","head":"緉（䩫）","pinyin":"liǎng","bus":{"num":308,"name":"㒳"},"level":3,"parent":"兩",
 "sections":[
  {"key":"shiyi","label":"釋義","text":"《說文》：“履兩枚也。一曰絞也。从糸从兩，兩亦聲。力讓切。”一雙鞋子。兩股繩帶交合。"},
  {"key":"shengmu","label":"聲母擬態","text":"l「拢离」取「拢」：二縷絞轉，合而為繩（推）。"},
  {"key":"suoshujuan","label":"所属卷","text":"","links":[{"t":"卷","ch":"卷五十四网","label":"卷五十四网"}]}]}
```

**釋義**＝原稿该行去掉「字头＋括注异体＋拼音」后的全文，不缩写、不概括、不补义。
**aliases**＝head 括注里的异体，但**已有独立卡的字不列**（如 滿 有懣卡，就不写 懣）。

### 4.4 `rootChain` / `rootLabel` / `rootLevel`

- 一般省略 `rootLevel`（全库只有 10 张写）。谐声族字**不要**写，免得把谐声字标成字根。
- `rootChain`（可选）：从部头到本字（含本字）的链，如 㒼 `["兩","㒼"]`；族字也可写全链 `["亯","郭","㗥"]`，但不能首尾不符（verify 会 warn）。
- `rootLabel`（可选）：页面上显示的根名；多数卡不写。

## 5. 字族表：四格与桥句（最容易出错）

每行 `[字（异体）, 读音, 类属, 取义落点]`——**新卡四格**。老卡里五格（末格空串）是历史格式，不要模仿、也不要去批量改旧卡。组题与收字**照原稿**，不收空组；两组以上才加 ①②③。

### 5.1 类属

取该字形旁（糸/肉/車/人/口/隹/髟/虫/風/手/衣/木/力/足/目/竹/金/貝/水/心/頁/米/酉/日/土/女/犬/食/魚/禾/毛/玉…）；原稿明写「从X」的以「从X」为准。**不许空、不许 `-`**。

### 5.2 取义落点

格式：`《書名》「原文首句」——短桥`。

1. 引文只到第一个「。」，**句末句号留在「」内**（`「濯髮也。」`）；`从X聲``某切``臣鉉等曰` 删掉。
2. 桥**一句为限，≤12 字（含末尾标点）**；只点「物象↔本组义项」的契合点，**不作释义、不讲因果**。
3. **新卡桥句末尾不加句号**；旧卡已有的句号不动（全库 8017 条带、3702 条不带，不因句号判错，也不为统一去批量改旧卡）。`check-luodian` 的长度上限**含**标点，所以带句号的旧行要按含句号计。
4. 禁用因果/解释连词：`故／所以／因此／因而／從而／可見／這是／稱為／表示`。
5. **不复述**：不与釋義原文连续 ≥5 字重合、不复述组题（≥5 字）、不复述声母栏的动作与用语。
6. 专名（人名/地名/水名/玉名/草名/兽名/国名/姓氏/女字）**只录原文，不搭桥**；音译字只写 `音譯字，只取其音。`
7. 讹字组整行照录原文，**不加「——」**。
8. 不得出现「借聲／借音／借其聲／借其音」（音译外）。
9. 名物无义理可释者，只录原文；不要硬写「取聲」「于義無取」。

正例（307 木部，4–6 字）：`——以水沃髮`、`——小雨如沐`、`——蟬吸樹汁`、`——以刀治木`。
反例（308 初稿，后已改）：
- ✗ `《說文》「履兩枚也。」——履成雙而耦，故以兩計。`（因果＋复述）
- ✓ `《說文》「履兩枚也。」——履必成雙。`
- ✗ `《漢書注》「車一乗曰一兩」——輪轅兩兩相耦，故車以兩計。`
- ✓ `《漢書注》「車一乗曰一兩」——一輿承雙輪。`

## 6. 声母拟态

- 取**今读拼音首字母**；z/c/s 归 zh/ch/sh。零声母写 `零聲母` 或 `y「零聲母」不系：…（照實）`。
- 组名只有两组：`g 隔估 k 口控 h 豁活；j 聚决 q 亲缺 x 续消；b 闭剥 p 拼辟 f 附分 m 蒙末；d 囤动 t 涂突 n 纳弄 r 柔锐 l 拢离；zh/z 凿总 ch/c 刺持 sh/s 失收`。**当前全库用 j「聚决」**，不要自造 j「夹卸」。
- 取项**只能取组名两字之一**（拢离→拢 或 离），不得写「取聚拢」。
- 必须落到该字的物性，句末标 `（推）`；确实无关写 `不系：…（照實）`。
- 格式硬约束（check-bu / verify 的正则）：`^((?:[a-zA-Z]{1,2}|零)「[^」]+」(取「[^」]」：|不系：)|不取義：)`。
- 与桥句分工：桥句讲「物象→本组义」，声母讲「音→物性」，两栏不要用同一句、同一组词。

## 7. 简体索引

每部建完，把该部头字与族字里的**规范简化字**同时写进两份表：`web/public/variants.json` 与 `web/public/cards/variants.json`（`{"简体":"繁体"}`，单行紧凑 JSON，别 pretty-print）。
再跑 `tools/build-card-index.py`，逐个 `/card/<简体>` 验 200 且页头显繁体。没简化字就不加。

## 8. 核验：把错误变成可自修的报告

### 8.1 一条命令跑全

```powershell
$env:PYTHONIOENCODING='utf-8'
# 单卡/多卡
.runtime\python\python.exe tools\verify-card.py 緉 輛 --expect .tmp-expect.json
# 整部（含 zizu 成员）
.runtime\python\python.exe tools\verify-card.py --bu 兩 --expect .tmp-expect.json --page
# 只验文件（试跑/并行工人自检）
.runtime\python\python.exe tools\verify-card.py --file web/public/cards/緉.json
# 机器可读报告
.runtime\python\python.exe tools\verify-card.py --bu 兩 --json .tmp-verify.json
```

- `--expect` = `{字: 原稿整行}`，用来核对族卡釋義是否整行照录；用 `tools/make-charmap.py --bu 兩 --expect .tmp-expect.json` 生成。
- `--page` 需要服务在 8099；`--alias-pages` 会顺带验简体/异体路由。
- 退出码：有 error 为 1，只有 warn 为 0。

### 8.2 报告怎么读

JSON 结构：

```json
{"tool":"verify-card","version":1,"generated":"…",
 "scope":{"bu":"兩","cards":49},"verdict":"pass",
 "counts":{"error":0,"warn":0},
 "issues":[{"code":"E070","severity":"error","card":"緉","where":"shiyi",
            "message":"釋義不是原稿整行","hint":"…","evidence":"…"}]}
```

每条 issue 都有：`code`（稳定可 grep）、`severity`、`card`、`where`、`message`、`hint`（怎么改）、`evidence`（证据片段）。
**自修循环**：跑 → 只按 `hint` 改 → 再跑，直到 `RESULT PASS · error 0`；warn 要么修掉，要么在交付说明里逐条解释。

### 8.3 错误码表（按域分组）

| 段 | 码 | 含义 |
|---|---|---|
| 文件/字段 | E001 | 缺卡或 JSON 坏 |
| | E003 | 顶层字段缺失（char/head/pinyin/bus/level/sections） |
| 栏 | E010 | 栏缺失或栏序不对 |
| | E011 | 栏重复 |
| | E012 | 族卡首栏不是 shiyi |
| | E013 | 族卡带了 zizu/zixing |
| | E014 | 釋義为空 |
| 世系 | E020 | parent 缺失/无卡/链到不了部头 |
| | E021 | rootChain 不像 `[部头,…,本字]`（warn） |
| 别名 | E030 | head 括注字未入 aliases |
| | E031 | alias 自己有卡（抢注，warn） |
| 字族 | E040 | 组题为空 |
| | E041 | 空组/无 groups |
| | E042 | 行不是 4 格 |
| | E043 | 类属为空 |
| | E044 | 首格为空 |
| | E045 | 多组但组题无编号（warn） |
| 图 | E050 | 字形文件缺 |
| | E051 | gimgs 与 index files 数不符 |
| | E052 | inline 占位符指向不存在的文件 |
| | E053 | 插图文件缺 |
| | E054 | chars[].photos 与顶层 photos 不同步 |
| | E055 | 顶层 photos 不是 `photos/<字>/…` 全路径 |
| | E056 | 字形图疑为现代字/符号（≤40px 且 ≤2-bit，或 <350 B；warn） |
| 声母 | E060 | 声母缺失/格式不符 |
| | E061 | 声母首字母与 pinyin 不符 |
| | E062 | 取项不在组名两字内 |
| 释义 | E070 | 釋義不是原稿整行（需 --expect） |
| | E071 | 釋義带字头+拼音（warn） |
| 落点 | E080 | 行内无「——」且不是音译/讹字 |
| | E081 | 讹字组落点带「——」 |
| | E082 | 引文未以」收尾 |
| 页面 | E090 | 页面打不开/非 200 |
| | E091 | 图注数与字形+參證+插图数不符 |
| | E092 | 页面残留 `{{` |
| | E093 | 图片 404 |
| | E094 | 别名页非 200 |

### 8.4 其他校验工具（按需，不要重复跑全库）

| 工具 | 查什么 | 何时跑 |
|---|---|---|
| `check-bu.py <部>` | 部内成员是否都有卡、parent/level/首栏/别名/声母格式 | 整部合并后必跑 |
| `check-ezi.py` | 讹字组是否混入「——」 | 有讹字组时 |
| `check-cardhygiene.py` | 栏文是否残留「本義：」等标签、zizu.text 是否等于组题 | 每次 |
| `check-luodian.py <部…>` | 桥句长度/连词/复述（F1–F8） | 新卡严格模式必跑 |
| `check-shiyi.py` | 全库族卡釋義 vs 原稿（需 `.tmp-charmap.json`） | 整部合并后 |
| `check-aliases.py` / `check-head-alias.py` | 别名缺口/该建未建 | 抽查 |
| `check-family.py` / `check-groups.py` / `check-prefix.py` | 族表/组题/栏文重复前缀单点检查 | 抽查 |
| `check-photos.py` | 有图无注/空图注统计 | 图片批次后 |
| `check-cards.py` | 全库结构总量（有历史欠账，不当新卡闸门） | 只看新卡有无新增类型 |

### 8.5 页面核验

- `/card/<部头>` 的 `<figcaption>` 数 = `chars[本字].files` 数 + `extra[]` 各字 files 数 + `cimgs` 数 + 顶层 `photos` 数。
- `{{` 残留 = 0；照片/字形 `<img>` 全 200；族卡页有「釋義」「聲母擬態」两栏；简体/异体路由 200。
- 服务启动（必须后台 job，`Start-Process` 会被回收）：

```powershell
$env:PORT='8099'; & 'C:\Users\萧磊\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\node\bin\node.exe' web\server.mjs
```

### 8.6 改坏了怎么回滚

- 单文件恢复：`git show HEAD:web/public/cards/兩.json > tmp && mv tmp web/public/cards/兩.json`（或 `git restore --source=HEAD -- <path>`）。
- 新文件写坏：直接删（未 `git add` 前不进库）。
- 大 JSON 被 pretty-print 污染：从 `git show HEAD:<path>` 取原格式，用 Python 在原对象上改，再按原 `separators` 写回；参考 captions.json 事故（§12）。
- 不要 `git checkout -- .`、不要 `git clean -fd`（会连别人的改动一起清）。

## 9. 并行产线：拆单、派工、合并

适用：建整部（>15 行族表）、补多张族卡。单卡不要拆。

### 9.1 三条铁律（2026-11-22 308/309 撞车后定）

1. **共享文件单写者**：`cards/index.json`、`alias-index.json`、`cards/variants.json`（源）、`web/public/variants.json`（生成）、`glyphs/index.json`、`photos/*`、父卡、服务、git —— 只有 lead 写，且只在合并完成后写一次。worker 一律不碰。
2. **工人只写两处**：`<cards-dir>/<字>.json` 和 `<results>/batch-NN.json`。别人批、共享文件、父卡都不碰。
3. **一部一 lead，开工先上锁**：`workplan.py lock`。两个 lead 同时各自重建索引，就是 308/309 互相回退的直接原因。

### 9.2 所有权矩阵

| 产物 | 谁写 | 时机 |
|---|---|---|
| `cards/<族字>.json` | 各 worker（一人一批） | 派工期间 |
| `results/batch-NN.json` | 各 worker | 派工期间 |
| 父卡 `zizu.groups[].rows[3]` | lead | merge |
| `cards/variants.json`（源） | lead | 备料/集成 |
| `web/public/variants.json` | `build-card-index.py` 生成 | 集成（不手改） |
| `cards/index.json`、`alias-index.json` | `build-card-index.py` | 集成 |
| `glyphs/**`、`photos/**` | lead | 派工前备料；集成时补 |
| 服务重启、git、memory | lead | 集成/提交 |

### 9.3 开工前 30 秒

```powershell
tools\git.cmd status --short
.runtime\python\python.exe tools\workplan.py status
.runtime\python\python.exe tools\workplan.py lock --owner <你的名字> --bu <部名>
```

- `status` 显示别人的 lock（12 小时内）→ **停**：换部、或只做只读备料，不要集成；确需接管才 `--force`，并先问主人。
- `git status` 有别人改的共享文件（index/variants/glyphs/index/photos）→ 视为脏：**不重建、不覆盖、不提交这些路径**；先把你的卡做成独立 commit，再协调。
- HEAD 在你干活期间前移 → 提交前重读要改的文件；不要拿开工时的快照写回。

### 9.4 阶段

0. **上锁**（§9.3）。
1. **lead 备料**：判型（§1）、取原文（§2）、抽字形/照片/參證并核数（§3）、补 `cards/variants.json`（§7）。
2. **lead 写 manifest**：族表拆组与行，行带 `quote`（引文到首句）、`shiyi`（原稿整行去字头+拼音）、`cls`、`pinyin`，桥句留空；特殊行标 `kind`（`translit`/`ezi`）与 `notes`（多音取读、声母取项提示）。
3. **lead split**：`workplan.py split` 生成批次、结果模板、README。
4. **worker 并行**：按 §9.6 契书写卡 + 桥句 + 自检。
5. **lead 收单**：`workplan.py check --cards-dir`（覆盖、桥句、釋義逐字一致）；`workplan.py audit` 查有没有人越界写了共享文件。
6. **lead merge**：先 dry-run 再 `--apply`，只写父卡。
7. **lead 集成**：`build-card-index.py` 一次重建 index/alias/root-variants；重启服务。
8. **集成门**：`verify-card --bu`、`check-bu`、`check-ezi`、`check-cardhygiene`、`check-shiyi`、`check-luodian`、页检（§8、§10）。
9. **按路径提交**（§11）；`workplan.py unlock`。

### 9.5 manifest 与命令

```json
{
 "bu": {"num": 309, "name": "面", "head": "面"},
 "volume": {"ch": "卷五十四网", "label": "卷五十四网"},
 "groups": [
  {"title": "①指眼瞼的閉合，表示沉迷、羞愧、勉力", "parent": "面",
   "rows": [
    {"order": 1, "label": "湎（䤄𨟺𩈳）", "char": "湎", "pinyin": "miǎn",
     "cls": "水", "quote": "《說文》「…」", "bridge": "",
     "shiyi": "《說文》：…（原稿整行去掉字头+拼音）", "kind": "normal", "notes": ""}
   ]}
 ]
}
```

```powershell
$env:PYTHONIOENCODING='utf-8'
# 拆：每批 5–6 行；--cards-dir 指定工人写卡目录（生产=web/public/cards，试点=.tmp-pilot/cards）
.runtime\python\python.exe tools\workplan.py split --manifest .tmp-plan\309.json --batch 6 --out .tmp-plan\309 --cards-dir web\public\cards
# 收单：桥句、覆盖、族卡釋義逐字（不写盘）
.runtime\python\python.exe tools\workplan.py check --manifest .tmp-plan\309.json --results .tmp-plan\309\results --cards-dir web\public\cards
# 越界审计：只该有本批卡与结果；共享文件被改会打 OUTSIDE
.runtime\python\python.exe tools\workplan.py audit --manifest .tmp-plan\309.json --results .tmp-plan\309\results --cards-dir web\public\cards
# 合并（先 dry-run，确认后再 --apply）
.runtime\python\python.exe tools\workplan.py merge --manifest .tmp-plan\309.json --results .tmp-plan\309\results --cards-dir web\public\cards --apply
```

- `merge` 用 `[label,pinyin,cls,quote+"——"+bridge]` 重建行，按 `(group,order,char)` 覆盖父卡；有错（缺行、重复、空桥、桥句违规）exit 1 且不写盘。
- `bridge` 以「——」开头、或 `text` 整行给出（音译/名物/讹字）时原样用。
- `kind=translit` 写 `音譯字，只取其音`；`kind=ezi` 用 `text`，无「——」。

### 9.6 worker 契书（派工时原样给）

> 你只做本批 `batch-NN.json` 里的行。
> 1. 先读 `.dsh/skills/hanzi-card/SKILL.md` 的 §4/§5/§6 与 `README.md`。
> 2. 每行一张 `<cards-dir>/<字>.json`：`char/head/pinyin/bus/level:3/parent` 按工单；`shiyi` **逐字**等于工单 `shiyi`；`shengmu` 按 §6 自拟；`aliases` 只列 head 括注里、且无独立卡的字；不加 zizu/zixing。
> 3. 桥句按 §5.2 自拟，填 `results/batch-NN.json`（`{group,order,char,bridge,evidence}`）。
> 4. 自检到 0 error：`verify-card.py --file <cards-dir>/<字>.json --cards-dir <cards-dir>`。
> 5. **只写自己批的卡与结果文件**；禁止改父卡、index、variants、glyphs、服务、git；不要动别人批。
> 6. 交付：RESULT 行、桥句原文、不确定点（工单缺什么、哪条规则最难）。

### 9.7 批次与并行度

- 默认 **5–6 行/批**；有 inline 形、多音、长释义时 3–4 行；纯名物短行可 8 行。
- 同时跑 3–6 个 worker 最稳；每多一个 worker，lead 的合并核对不省。
- 一个 worker 只拿一批；批次之间不共享文件，避免互相看见对方的桥句。

### 9.8 集成门（lead 不能省的手工复核）

- `workplan.py audit` 必须 0 越界；有 OUTSIDE 先查是谁改的，别直接提交。
- 抽 1–2 行**自己重读原稿**，核对 worker 的 `shiyi` 与桥句；机器只拦格式，不判「搭桥是否讲得通」。
- 桥句与声母是否互相复述：同一物象/同一组词出现两次就改。
- 重跑旧部时，父卡已有 gold 桥句会泄题：先把对应行桥句清空或换占位再发单。
- worker 报「不确定」的条目逐条裁决，裁决写进交付说明，不留在聊天里。

### 9.9 冲突处理

| 症状 | 处置 |
|---|---|
| lock 被别人持有 | 等/换部/只做只读准备；不集成、不重建索引 |
| git status 有别人改的 index/variants/glyphs-index/photos | 不碰这些路径；只提交自己的卡与图；请对方先提交，或等其提交后再重建 |
| 提交时 HEAD 已前移 | 重读目标文件；`git diff` 看新改动；只 add 自己路径 |
| 自己的索引条目被整体覆盖 | 不反复重写；在最新文件上只补自己的键，重建一次并立即提交 |
| 两人改了同一张卡 | 后手先读对方版本，人工合并语义；不整文件覆盖 |
| worker 写了父卡/index | `git restore` 该文件，重派该批；audit 会指出越界 |

**绝对禁止**：`git add -A`、`git checkout -- .`、`git clean -fd`、`git reset --hard`。

### 9.10 实测与事故

- 2026-11-22 试点：2 worker × 2 行（緉/輛、倆/𨨄）首轮 PASS；桥句 8 字内。
- 2026-11-22 308/309 并行：309 会话整体重写 `variants.json`/`glyphs/index.json`，把 308 刚加的 7 个简体键与 㒼 的索引条目回退，HEAD 前移两次；靠「按路径提交 + 在对方最新文件上重补」收场。§9.1 由此而来。

## 10. 验收清单（整部交付前逐条打勾）

```powershell
$env:PYTHONIOENCODING='utf-8'
.runtime\python\python.exe tools\make-charmap.py --bu 面 --expect .tmp-expect.json
.runtime\python\python.exe tools\verify-card.py --bu 面 --expect .tmp-expect.json --page --alias-pages   # PASS 0/0
.runtime\python\python.exe tools\check-bu.py 面            # 部 面: 成员 N，二级 M，问题 0
.runtime\python\python.exe tools\check-ezi.py              # bad 0
.runtime\python\python.exe tools\check-cardhygiene.py      # label 0 / dup-zizu 0
.runtime\python\python.exe tools\check-luodian.py 面       # rows N bad 0
.runtime\python\python.exe tools\check-shiyi.py            # checked N violations 0
.runtime\python\python.exe tools\build-card-index.py       # index N / alias M
```

- 页检：`/card/<部头>` 图注数 = 字形+參證+插图；`{{` 残留 0；简体/异体路由 200。
- 字形：`verify-card` 的 E056 = 0（没有现代字混进古文字形序列）；有则按 §3.6 归位。
- 越界：`workplan.py audit ... --allow "tools/*"` 为 0；`git status` 里只该有本次产物与 `tools/` 新工具；`.tmp-*` 临时文件删掉。
- `build-card-index.py` 输出 `index N / alias M / variants K` 三个数（root variants 由它同步，不手改）。
- 最后回主人：结论先行（建成/提交 hash/校验数字/图数），再讲异常与下一步。

## 11. 提交与记忆：分三层，别让单字牵动全局

### 11.1 三层记录

| 改动 | 该写 | 不要写 |
|---|---|---|
| 单字（补卡/改图/改桥句） | 卡 JSON、`glyphs/<字>/`、必要时 `cards/variants.json` | HANDOFF、CURRENT、exegesis、SKILL |
| 整部（部头+族+图+索引） | 上述 + index/alias/root-variants + CURRENT 一条 | HANDOFF 只在部完成/待办变时改 |
| 规则或流程变更 | exegesis（内容规则）或 SKILL（流程）二选一为源 | 另一处只放指针；HANDOFF 只留一行 |

- **单字建卡不写任何 memory 文档**；回主人一句话即可。只有发现「新错误类」才动 HANDOFF/SKILL。
- CURRENT 一部一条：部号、字数、校验数字、页检图数；不写过程。
- HANDOFF 只维护四行（Done when、最新提交、最近一部、待办）+ 错误类标题；细节在 SKILL §12。

### 11.2 单字最小提交面

1. `web/public/cards/<字>.json`
2. `web/public/glyphs/<字>/`（有新图时）
3. `web/public/cards/variants.json`（有简体时；root variants 由 `build-card-index.py` 生成，不手改）
4. `cards/index.json` / `alias-index.json`（动了别名/简体才要，且由脚本重建）

页检：`/card/<字>` 图数对、无 `{{`；`/card/<简体>` 200 或 302。
提交信息：`cards <字>：…`。

### 11.3 整部提交

- 只 `git add` 本次产物；**绝不 `git add -A`**。
- 不删 `debug.log`、`intake/bao/`；不 glob 删 `tools/_tmp_*`。
- 提交信息：`cards <部号> <部名>（<头字> N形/<二级> M形，K 族卡，插图 P；…）`。
- 工具改动单独 `tools: …`，不与 cards 混。
- 提交前 `workplan.py audit --manifest … --allow "tools/*"` 确认没有越界文件。

### 11.4 记忆模板

- HANDOFF 四行 + 待办一项（只写数字与下一部）。
- CURRENT 一条：`- 2026-MM-DD：<部> <字数>；check-bu 0/N、ezi 0、页检 N 图；<异常一句>`。

## 12. 事故库（都是踩过的）

| 症状 | 原因 | 处置 |
|---|---|---|
| 整份 diff 几千行 | 用 `json.dumps(indent=2)` 重写别人 `indent=1`/单行的 JSON | 先 `git show HEAD:<path>` 看格式，按原格式写；大 JSON 用 `separators=(",",":")` |
| 控制台中文乱码 | 控制台 GBK，不是文件坏 | 别据此改文件；用 Python 读 UTF-8 打印或写文件 |
| 照片 404 | 顶层 `photos` 写了 `01.jpg` | 写 `photos/<字>/01.jpg` |
| 页面图数不对 | 图按内容/最近字头归属 | 只按「▲」图注段落区间归属 |
| 图片重复 | 批量抽图把同一张分给两字 | 比 sha256，删错主的那份并清两处 index |
| 落点啰嗦 | 把「搭桥」写成解释句，还带因果 | §5.2；`check-luodian` 严格模式 0 |
| 卡与 build 脚本不一致 | 建完又用补丁脚本改 JSON，脚本没同步 | **建成后 JSON 是唯一真源**；一次性 build 脚本头部加「已过期，勿运行」，或删掉 |
| 释义被改短 | 把引文摘句当释义 | 族卡釋義＝原稿整行；`check-shiyi` |
| 字形图少几张 | 抽取器静默跳过 EMF/WMF 或 >900KB | 抽完数 `files` 对数；转 PNG/调 `--maxbytes` 补抽 |
| 參證图并进本字 | 段落末尾 `N图X` 被当成本字字形 | 按 §3.2 分 `extra`/`cankao`，不要覆盖他字 files |
| 并行时桥句互相打架 | 两个 worker 写同一行/父卡 | 一人一批、父卡只由 lead merge；重派单批 |
| 共享文件被整体回退 | 两个 lead 各自重建 `variants`/`glyphs/index`，后写者用旧快照 | 一部一 lead、开工 lock、只在 merge 后重建一次；提交按路径（§9.1、§9.9） |
| 字形序列混入现代字 | 括号里的字体渲染简图被当古文字形 | E056 告警；按 §3.6 移到 `glyphs/chars/<hex>.png`，重编号并补别名 |
| 单字建卡改了一堆文档 | 把「记录」当成每字必做 | 三层记录（§11.1）：单字不写 HANDOFF/CURRENT/exegesis/SKILL |
| 简体表两份改漏一份 | 手改 root 与 cards 两份 | 只改 `cards/variants.json`；root 由 `build-card-index.py` 生成 |

## 13. 一句话

**原稿照抄，图按段归，桥句一句十二字以内；单字只动卡与图，整部走「lock → manifest → split → 并行 → check → merge → 集成门」，全绿再按路径提交。**
