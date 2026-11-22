---
name: hanzi-card
description: 在「系统汉字」库为一个汉字建卡或补卡（部头、二级字根、三级族字）：定位原稿段落、切字形图、写 JSON 卡、跑全部校验并提交。当主人说「建某字」「补某部」「把某字加进去」「这字怎么落点」时使用。
whenToUse: 主人要求新增/修订字卡、续建某一部、给族表补字、修落点或释义时；也用于回答「某卡为什么这样写」的溯源。
---

# 建一张汉字卡：标准流程

目标：原稿怎么写的，卡就怎么落；一步一验，不靠事后补救。
**卡是产物，原稿是唯一真源；任何一栏都不许自己发挥。**

## 0. 开工前必读（按序，别跳）

1. `AGENTS.md` —— 硬规则（知识只走 pkc、禁手改 knowledge/、中文、结论先行）。
2. `memory/OPERATING.md` —— 主人授权范围（日常建卡不必再问；删知识、改旧正文/边界、重组主题要先说明）。
3. `memory/CURRENT.md` 顶部 —— 当前进度与最近提交。
4. `memory/HANDOFF.md` §一（产线）、§二（七类错误＋本技能第八类）、§三（待办）。
5. `prompts/exegesis.md` —— 栏序、引文体例、落点铁律（**与本文冲突时以 exegesis 为准**）。

## 1. 判型：这张卡是几级

| 级 | 判据（看原稿段落结构） | JSON |
|---|---|---|
| 1 部头 | `NNN.某部` 后第一个带 `（异体…拼音）：` 的字头段，后接 本義/轉義/辯證/音源/字族衍義 | `level:1`，全套栏 |
| 2 二级字根 | 部内另一个独立字头段（起法同部头），有自己的本義、字族表；部头卡的 `erji.links` 要挂它 | `level:2`，`parent`／`rootChain`／`rootLabel` |
| 3 族字 | 只在别人的族表里出现一行（字（异体）＋拼音＋类属＋引文释义） | `level:3`，`parent`，只有 釋義＋聲母擬態＋所属卷 |

- **部名与部头字可以不同**（308 部名「㒳」，部头是「兩」）。`bus.name` 用部名，卡文件名与 `char` 用部头字。
- 二级字根**不并入上级族表**，单独成卡、单独挂 erji。
- 讹字/形近字行：不建新卡，归正字（如 308 𧶪→貴）。

## 2. 取原文：先定位段，再抄

- 缓存纯文本：`web/.cache/txt/卷五十四  网.txt`（一行≈一个 docx 段；**行号≠python-docx 段号**，但通常只差几个空段）。
- 没有缓存时：`.runtime\python\python.exe tools\docx2txt.py <docx>`（stdlib，不依赖 python-docx）。
- **不要试图 pip 装 python-docx**：venv 里没有，离线也装不上；`load_workspace_dependencies` 在本机会 EPERM。解析用 `zipfile`＋正则即可。
- 控制台是 GBK：跑脚本前 `$env:PYTHONIOENCODING='utf-8'`，并把输出重定向到文件再读，否则 `UnicodeEncodeError`。
- 抄写规则：
  - 五栏（本義/轉義/辯證/音源/字族衍義）**逐字照录**，只剥行首标签 `^(本義|轉義|辯證|音源|字形|字族衍義|聲母擬態|所属卷|釋義)[：:]`。
  - **不得 `split('：')`**：引文里的冒号是内容（`《集韻》：“乘也，匹也，”`）。
  - 一栏多段：按段序合并，段间 `\n`；`paras` 与 `text` 同步更新。
  - 改完跑 `tools/check-cols.py` 复核栏文与段数。

## 3. 图：字形、插图、句中形

**字形段**（`（异体…拼音）：` 开头、内含多张图）：
- 按「。」分段：句号前的图归当前字头；句号后遇到**单个汉字**标签，前一组的图归这个标签字；段末最后一组归该标签。
- 图片按出现顺序存 `web/public/glyphs/<字>/NN.png`，`01` 起；同时写 `web/public/glyphs/index.json` 的 `chars[字] = {doc, variants, files}`。
- 段内括注里的单张图（如 308 P331 㒼 异体后那张）不是字形图，跳过。

**插图**（独立图片段，下一段以「▲」开头）：
- 归属只看段落区间，**不许看图猜**：`▲` 图注段属于哪个字头的区间，图就归谁。
- 文件放 `web/public/glyphs/photos/<字>/NN.jpg`；图注照录 ▲ 后文字，**原文没有 ▲ 就留空 `""`，不许自造说明**。
- `glyphs/index.json` 有**两处** photos：`chars[字].photos` 与**顶层** `photos` 映射。页面实际读**顶层**，且 `photoList` 会拼 `/glyphs/` 前缀，所以顶层值必须写全路径：
  `{"file":"photos/兩/01.jpg","caption":""}`（写 `01.jpg` 会 404）。
- 改完 `glyphs/index.json` 要**重启服务**（内存缓存 300 秒）。
- 重复图、错主图要删：先确认同一 sha256 没有第二处引用，再删文件与两处 index 条目。

**句中形**（引文里嵌的古文字）：
- 用占位符 `{{<栏>/NN.png}}` 原样插在文字流位置；文件存 `glyphs/inline/<字>/<栏>/NN.png`；section 加 `"gdir":"inline/<字>"`。
- 验收：卡里必须有 `{{`，页面无残留 `{{`，对应 `<img>` 返回 200。

## 4. 写卡：JSON 骨架

以邻居卡为准抄结构，别自创字段：
- 部头样板：`web/public/cards/兩.json`
- 二级样板：`web/public/cards/㒼.json`
- 族字样板：`web/public/cards/沐.json`（最短）

部头/二级栏序固定：
`benyi → [erji] → zhuanyi → bianzheng → yinyuan → shengmu → zixing → zizu → suoshujuan`

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
  {"key":"zixing","label":"字形","text":"","gimgs":["兩/01.png"]},
  {"key":"zizu","label":"字族衍義","text":"","groups":[{"title":"①…","rows":[["字（异体）","pinyin","糸","《說文》「…」——短桥",""]]}]},
  {"key":"suoshujuan","label":"所属卷","text":"","links":[{"t":"卷","ch":"卷五十四网","label":"卷五十四网"}]}
 ],
 "photos": [{"file":"01.jpg","caption":""}]
}
```

族字卡（level 3）：
```json
{"char":"緉","head":"緉（䩫）","pinyin":"liǎng","bus":{"num":308,"name":"㒳"},"level":3,"parent":"兩",
 "sections":[
  {"key":"shiyi","label":"釋義","text":"《說文》：“履兩枚也。一曰絞也。从糸从兩，兩亦聲。力讓切。”一雙鞋子。兩股繩帶交合。"},
  {"key":"shengmu","label":"聲母擬態","text":"l「拢离」取「拢」：…（推）。"},
  {"key":"suoshujuan","label":"所属卷","text":"","links":[{"t":"卷","ch":"卷五十四网","label":"卷五十四网"}]}]}
```

**釋義**＝原稿该行去掉「字头＋括注异体＋拼音」后的全文，不缩写、不概括、不补义。
**aliases**＝括注里的异体，但**已有独立卡的字不列**（如 滿 有懣卡，就不写 懣）。

## 5. 字族表：四格与桥句（最容易出错）

每行 `[字（异体）, 读音, 类属, 取义落点, ""]`，组题与收字**照原稿**，不收空组；两组以上才加 ①②③。

**类属**：取该字形旁（糸/肉/車/人/口/隹/髟/虫/風/手/衣/木/力/足/目/竹/金/貝/水/心/頁/米/酉/日/土/女/犬/食/魚/禾/毛/玉…）；原稿明写「从X」的以「从X」为准。**不许空、不许 `-`**（check-bu 会报）。

**取义落点**：`《書名》「原文首句」——短桥`。铁律：
1. 引文只到第一个「。」，**句末句号留在「」内**（`「濯髮也。」`），桥句末尾**不加句号**。
2. 删 `从X聲`、`某切`、`臣鉉等曰`。
3. 桥**一句为限，≤12 字**；只点「物象↔本组义项」的契合点，**不作释义、不讲因果**。
4. 禁用因果/解释连词：`故／所以／因此／因而／從而／可見／這是／稱為／表示`。
5. **不复述**：不重复释义原文（≥5 字连续重合即算）、不复述组题、不复述声母栏的动作与用语。
6. 专名（人名/地名/水名/玉名/草名/兽名/国名/姓氏/女字）**只录原文，不搭桥**；音译字只写 `音譯字，只取其音。`
7. 讹字组整行照录原文，**不加「——」**（check-ezi 会报）。
8. 不得出现「借聲／借音／借其聲／借其音」（音译外）。

正例（307 木部，4–6 字）：`——以水沃髮`、`——小雨如沐`、`——蟬吸樹汁`、`——以刀治木`。
反例（308 初稿，后已改）：
- ✗ `《說文》「履兩枚也。」——履成雙而耦，故以兩計。`（因果＋复述「兩」）
- ✓ `《說文》「履兩枚也。」——履必成雙。`
- ✗ `《漢書注》「車一乗曰一兩」——輪轅兩兩相耦，故車以兩計。`
- ✓ `《漢書注》「車一乗曰一兩」——一輿承雙輪。`

## 6. 声母拟态

- 取**今读拼音首字母**；z/c/s 归 zh/ch/sh。零声母写 `零聲母` 或 `w「零聲母」不系：…（照實）`。
- 组名只有两组：`g 隔估 k 口控 h 豁活；j 聚决 q 亲缺 x 续消；b 闭剥 p 拼辟 f 附分 m 蒙末；d 囤动 t 涂突 n 纳弄 r 柔锐 l 拢离；zh/z 凿总 ch/c 刺持 sh/s 失收`。**当前全库用 j「聚决」**，不要自造 j「夹卸」。
- 取项**只能取组名两字之一**（拢离→拢 或 离），不得写「取聚拢」。
- 必须落到该字的物性，句末标 `（推）`；确实无关写 `不系：…（照實）`。
- 格式硬约束（check-bu 正则）：`^((?:[a-zA-Z]{1,2}|零)「[^」]+」(取「[^」]」：|不系：)|不取義：)`。

## 7. 简体索引

每部建完，把该部头字与族字里的**规范简化字**同时写进两份表：`web/public/variants.json` 与 `web/public/cards/variants.json`（`{"简体":"繁体"}`）。
再跑 `tools/build-card-index.py`，逐个 `/card/<简体>` 验 200 且页头显繁体。没简化字就不加。

## 8. 验收（少一步都不算完）

```powershell
$env:PYTHONIOENCODING='utf-8'
.runtime\python\python.exe tools\check-bu.py 兩          # 部 兩: 成员 N，二级 M，问题 0
.runtime\python\python.exe tools\check-ezi.py            # bad 0
.runtime\python\python.exe tools\check-cardhygiene.py    # label 0 / dup-zizu 0
.runtime\python\python.exe tools\check-luodian.py 兩 㒼  # rows N bad 0（新卡严格模式）
.runtime\python\python.exe tools\check-cards.py          # 只看新卡有没有新增问题类型
.runtime\python\python.exe tools\build-card-index.py     # index N / alias M
```

- **释义务必对原稿**：`check-shiyi.py` 需要 `.tmp-charmap.json`（`{字:{txt:整行}}`）；没有就先建，跑完删。`violations` 只允许剩 `{{…}}` 占位条目；若卡里缺 `《》「」“”` 等引号，`rowtail` 会截错，属比对伪差，要人工看。
- **落点逐行读一遍**：长度、连词、复述三条（第 5 节），机器只拦一部分，语义重复要人眼。
- **页面核验**（服务在 8099）：
  - `/card/<部头>` 的 `<figcaption>` 数 = 字形数＋參證数＋插图数；`{{` 残留 = 0；照片 `<img>` = 200。
  - 族卡页有「釋義」「聲母擬態」两栏；`/card/<简体>`、`/card/<异体>` 全 200。
- 服务启动（必须后台 job，`Start-Process` 会被回收）：
  ```powershell
  $env:PORT='8099'; & 'C:\Users\萧磊\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\node\bin\node.exe' web\server.mjs
  ```

## 9. 提交与记忆

- 只 `git add` 本次产物（`web/public/cards`、`web/public/glyphs`、`variants`、`index`、必要的 `tools/*.py`）；**绝不 `git add -A`**。
- 不删 `debug.log`、`intake/bao/`；不 glob 删 `tools/_tmp_*`（里面有已入库文件，误删过一次）。
- 提交信息：`cards <部号> <部名>（<头字> N形/<二级> M形，K 族卡，插图 P；……）`；补简体写「补 X/Y 简体索引」。
- 改 `memory/HANDOFF.md`（Done when、最新提交、最近一部、待办）与 `memory/CURRENT.md`（在日期列表顶部插一条，记数字与校验结果）。
- 最后回主人：结论先行（建成/提交 hash/校验数字/图数），再讲异常与下一步。

## 10. 事故库（都是踩过的）

| 症状 | 原因 | 处置 |
|---|---|---|
| 整份 dif 几千行 | 用 `json.dumps(indent=2)` 重写别人 `indent=1` 的单行/紧凑 JSON | 先 `git show HEAD:<path>` 看格式，按原格式写；大 JSON 用 `separators=(",",":")` |
| 控制台中文乱码 | 控制台 GBK，不是文件坏 | 别据此改文件；用 Python 读 UTF-8 打印或写文件 |
| 照片 404 | 顶层 `photos` 写了 `01.jpg` | 写 `photos/<字>/01.jpg` |
| 页面图数不对 | 图按内容/最近字头归属 | 只按「▲」图注段落区间归属 |
| 图片重复 | 批量抽图把同一张分给两字 | 比 sha256，删错主的那份并清两处 index |
| 落点啰嗦 | 把「搭桥」写成解释句，还带因果 | 见第 5 节；`check-luodian.py` 严格模式跑 0 |
| 卡与 build 脚本不一致 | 建完又用补丁脚本改了 JSON，脚本没同步 | **建成后 JSON 是唯一真源**；一次性 build 脚本头部加「已过期，勿运行」，或删掉 |
| 释义被改短 | 把引文摘句当释义 | 族卡釋義＝原稿整行；`check-shiyi.py` |

## 11. 一句话

**原稿照抄，图按段归，桥句一句十二字以内，四道校验（check-bu / check-ezi / check-cardhygiene / check-luodian）跑到 0，再提交。**
