# 操作入口

一句话：这个库的任何内容变动都走 `pkc knowledge-plan`——先预览、**按下面第 0 条的授权自主应用**，最后 `rebuild` + `validate`。

## 0. 授权（2026-10-21 主人定：不要再问，一律允许）

主人已明确「不要再问，一律允许」。以下操作**不必再逐次询问，直接做**，做完在报告里列明 bundle、hash、条数、改动范围：

- 常规录入：判类句、横向对照、声母义、六书/字形补句等**只追加、不改原文与边界**的修订（`clarify`）；
- 草稿 → `preview` → `capture` → `bundle-approve --apply` → `bundle-apply --apply` 全流程；
- 基线变动后重算 hash（正文一字未改）、`rebase`、`abandon` 重做；
- `pkc rebuild`、`pkc validate`、`knowledge-search` 验收，`memory/CURRENT.md` 记录，定向 `git add` 与 `git commit`；
- 起停测试用的网页服务、抽原稿图、生成 `intake/` 下的图与草稿、清理自建临时文件。

仍需先说明、不得擅自动手的三类：**删除知识或主题、改动既有正文与适用边界、调整主题结构**（`move-topic` / 大范围 `revise-claim` 改文）。这三类先讲清方案再动。

## 1. 读的顺序

1. 本文件 → `memory/CURRENT.md` → `memory/DECISIONS.md`
2. `pkc capabilities`：确认运行时可用
3. `pkc validate`：配置和知识树是否自洽
4. `pkc tree --format text`：看结构
5. `pkc knowledge-search "问题关键词" --format json --limit 5`：拿 L2 摘要

## 2. 回答别人的问题（网页 / 微信场景）

- 只用 `lifecycle=active` 且 `permission=public` 的 Claim 内容作答。
- 每条结论都要能对上具体 Claim（标题 + `clm_…` ID）。
- 检索不到、或只有 internal 内容时，直接说「知识库里还没有这个内容」，不要用模型自己的常识补。
- 不要先把 internal 内容改写再对外输出。
- 凡是讲到字根、或讲到某字由某字根得声得义，只要 `web/public/glyphs/<字>/` 下有古文字字形，就必须把图一并列出来（字形比论证更有说服力）；被释字自己没有字形行时，附上声符字根的字形，并说明图下小字是原书标注的出处与分期。
- 要配实物图（动物、器物、场景）时，先从原稿 docx 的 `word/media/` 里找插图——原书正文常在图前一段、图在下一段，按段落顺序定位；`web/public/glyphs/` 只有古文字字形，不是插图库。抽出的图另存 `intake/`，图注写明取自哪一卷哪一部，原图水印不要擦。**凡释到有实物可考的字（器物、动物、舟车、衣冠、建筑等），一律配实物图**（2026-10-21 主人定）：原稿有的，从 docx `word/media` 抽图，登记进 `web/public/glyphs/photos/<繁体字头>/NN.jpg` 与 `web/public/glyphs/index.json` 的 `photos`，`caption` 写原书图注（如「郭店楚墓竹簡（戰國）」）；原稿没有的，可用网络检索配图，但图注必须写明「**文外参考图**」并注明来源。**实物图只留在后端作参考，不进字卡，也不参与分级**（2026-10-21 主人定「配图不分级」「放在后端作参考吧」）——作答时按需贴给主人，字卡里不占版面。用户多用简体提问，而字形库、配图库按原稿繁体字头建键，故简体字须在 `web/public/variants.json` 补一条 简体→繁體 映射（只补确实需要的，宁少勿滥）。
- 凡是讲到字根（`部`），必须带上「声母义」：查「声母义（分部）」主题（`knowledge/hanzi-yinyuan/02z-shengmu-yi.md`，`topic-shengmu-yi`）该部的条目，报声母、部位、绪论拟态义与一致度（强／中／弱）；零声母诸部照实说「不系拟态声母义」。字卡已把它作为第二栏由服务端注入，人工释字同样要写。
- 「声母义」不能只报部内统计：拟态义必须落到本字所指的**物性、制造法、文化用法**上验一遍（如 l「拢离」之于柳：柳条可拢而编、截头平茬留条而不绝、折柳赠别又是离）；部首字今读若为假借音（如「卯」mǎo 之于柳 liǔ），统计口径要指出并以音源本音校正。**古音 zh、ch、sh 从 d、t 分化，齿音与舌音同源**（2026-10-21 主人定），声母义须循分化链贯通，不可因今读部位不同判为异源——例：「屯」tún 为 t「涂突」，芽尖破土；「纯」chún 从屯声，「莼」从纯，故莼仍是屯声，ch 为「刺持」：芽刺土而出、土持芽于内。**声母拟态义要阐释充分，不许轻易说不相关**（2026-10-21 主人再定）：须讲到动作层（谁做、对什么、结果如何）再落到本字所指之物；一致度弱、部内分歧、该部未收只说明统计口径有问题，不是「无关」的理由，确实相违要写明「为何相违」。**拟态义是相对的两面，释字只取合于本字的一面**（2026-10-21 主人三定）：t 涂突、ch 刺持、l 拢离、g 隔估……都是一对反义，一般只讲相合的那面，不必两面都解说——「莼」只取 ch 之「刺」（芽刺破土而出），「持」不必搬；只有引申链确实横跨两面时才写两面（柳：编束为拢、折别为离；遛：牵住为拢、走开为离）。细则见 `memory/HANZI-EXEGESIS.md` 第 1c 步第 6、7、8 条。
- 用字根解释其谐声字的字义时，**优先取字根的本义；本义讲不通，才取转义**（2026-10-21 主人定）。例：「疚」从久，久的本义是灸灼（jiù 读「灼病」），故疚＝灼痛之病；不可取「久」的引申义「时间长」当构形依据。字书「疚，久也」一类是同音声训，不是义源。**声旁取义的方式是比喻，释文读作「象……一样」**（2026-10-21 主人再定）：「疚」＝象被灸灼一样疼痛，「玖」＝象被烧灼一样色黑；形符只定其类与落点（疒→病，玉→美石）。**并不可轻言「象声不取义」**（2026-10-21 主人三定）：声旁几乎都有实义，实义与比喻义两层并存——「轰」＝三车相聚，象意众车，车多行疾而声大，实义是「众车」，比喻义是「声大如众车行驶之声」；只有确实搜不出实义可系的借音字才写「借声」，并说明理由。**比况只加在取本义的这一层**（2026-10-21 主人四定）：声根取**转义**时直接写「取某某的转义」，不再套「象……一样」；象意兼声的字也只说明声旁兼义，不必都加比况。**解释字根时不能作比喻义解**（2026-10-21 主人五定）：字根本身（一、二、三级）、象意兼声字、象形象事会意字，一律**本义直释**——「舆」的本义就是两人对举抬车之状，「追」的本义就是跟在屁股后面跑；比喻义只针对形旁＋声旁、且声旁以相似关系进入的**合成谐声字**（疚＝象被灸灼一样疼痛）。判类句按此写「本义直释，不作比况」或「取本义作比况（象……一样）」，不可泛泛而论。细则见 `HANZI-EXEGESIS.md` 第 3 步 2b、2c、2d、2e、2e-0。
- 释字必须判六书，且用班固名目（象形、象事、象意、象声、转注、假借），不用「形声」一词：先看是独体象形、象形加无义符号（象事）、两个以上独体组合（象意），还是读音摹拟事物之声的音源字（象声）；复合的按绪论六种组合报（如「象意＋象声」），由声根加形旁分化来的说「转注字」。依据见 `knowledge/hanzi-origin/liushu.md`，判决理由写在 `memory/HANZI-EXEGESIS.md` 第 1b 步；原书未直断的要标「据体例推」。
- 释谐声字必须做**横向对照**（2026-10-21 主人定）：取库内至少 3 个同声符兄弟字，按「字｜取义面｜形符｜落到什么义」列表，看同一取义面在不同形符下怎样落到不同字义，再定本字落点。例（吾部）：「梧」＝木＋「相对」→树上下相当；「晤」＝日＋「相对」→人相见；「鯃」＝魚＋「相对」→前后等大；「鼯」＝鼠＋「相对」→**高下相对，只能从高赴下**。兄弟字不足 3 个就写明可对照者仅几字。不许单字孤立立说——没有兄弟字对照，就无法证明此义来自声旁而非形符。**对照要覆盖全族并按义类分表**（2026-10-21 主人扩为通例）：先把全族兄弟字按意义归类（取本义／取转义／只借声），每类一张表，最后总收「声符给义、形符定落点」；只借声的一类不可省。写入 Claim 时表改为分组串写。**同物异声更可互证**（2026-10-21 主人补）：同一动物有异名异体而声符不同者，取义同向即成强证——「鼫」从石（象掷石落石一般），原稿直说「鼫……鼯鼠，滑翔如掷石，不远」，正与「鼯」的高下相对相应。细则见 `HANZI-EXEGESIS.md` 第 3 步第 5、5a、5b 条。

## 3. 录入知识（唯一正规路径）

1. 起草草稿：`intake/xxx.json`（格式见 `intake/README.md`）。每条 Claim 必填 `node`、`topic_id`、`title`、`statement`、`boundary`、`permission`、`fact_classes`
2. 预览（不写任何东西）：`pkc knowledge-plan capture --file intake/xxx.json --preview-only`
3. 定稿：`pkc knowledge-plan capture --file intake/xxx.json`（去掉 `--preview-only` 会自动做 delta 校验并生成 Bundle，输出 `bundle_id` 与 64 位 `content_hash`）
4. 看 Bundle 内容：`pkc bundle-inspect bnd_xxx --format json`
5. 主人批准精确哈希：`pkc bundle-approve bnd_xxx --content-hash <64 位哈希> --apply`
6. 应用同一哈希：`pkc bundle-apply bnd_xxx --content-hash <64 位哈希> --apply`
7. 验收：`pkc rebuild` → `pkc validate` → 一条代表性 `knowledge-search` → `pkc knowledge-check`
8. 提交：`git add` 精确路径 → `git commit`

**哈希因基线变动重算时不必再问**（2026-10-21 主人定）：并行录入推进 commit 会让已批准的 plan 报 `PLAN_STALE_BASELINE`、内容一字未改而 hash 变了。此时若**正文完全相同**，视为已获批准——`knowledge-plan rebase`（或 abandon 后在当前基线上重做）→ 重新 `check --mode delta` + `finalize` → 直接 `bundle-approve` / `bundle-apply`，并在报告里同时注明**旧 hash 与新 hash**、说明只差基线。若正文有任何一个字改动，仍须重新报 hash 请批。plan 卡在 `CLAIM_TOPIC_MISSING` 而 `pkc validate` 通过时，多半是旧快照与并行提交错位，直接 abandon 重做，不要手工改 registry。

**声旁取义判类的批量修订可自主入库**（2026-10-21 主人授权）：凡是在已有 Claim 正文末尾**只追加一句「判类：…」、原枚举与引文一字不改**的批量修订，不必再逐批报 `content_hash` 请批——直接 `finalize` → `bundle-approve --apply` → `bundle-apply --apply` → `rebuild` / `validate` / 一条检索 → 提交，并在批次报告里列出 bundle、hash、条数与判类要点即可。若修订超出「只追加判类句」的范围（改原文、改标题、改边界、合并拆分、增删条目），仍按常规报批。

**族条横向对照可自主入库**（2026-10-21 主人授权）：给已有「字族」条末尾追加一段「横向对照（按义类分 N 组）：…」——只追加、原枚举与边界一字不改——同样不必逐批报 hash；按卷分批（每批 10–15 条族条），直接 finalize → bundle-approve/apply → `pkc rebuild`/`validate`/一条检索 → 写 CURRENT → 定向 `git add` 提交，报告列出 bundle、hash、条数与分组要点。凡改原文、标题、边界或增删条目，仍须报批。

修改已有条目用 `knowledge-plan revise-claim`，移动主题用 `move-topic`，不要手改文件。

**汉字知识的 fact_class 约定**：统一用 `evidence_scope`。PKC 的 Authority Ref 是给代码契约类事实用的（设计意图、实现、文档契约），汉字知识是文献证据型，用 `evidence_scope` 表示「以实际资料为界」；这样无需为每条知识伪造 Authority Ref。需要出处时，把原文摘录放进 `sources/` 并 `register-source` + `add-evidence`，走证据面。

**intent 即计划身份**：同一句 intent 重复提交会被当成旧计划（`PLAN_ABANDONED`），失败重试要换一句新的 intent。

**基线过期**：定稿后如果又提交了别的改动（哪怕只改文档），批准会报 `PLAN_STALE_BASELINE`。处理：`pkc knowledge-plan rebase <pln_…> --reason "…"` 重新贴到当前基线 → `pkc knowledge-plan check <pln_…> --mode delta` → `pkc knowledge-plan finalize <pln_…>`，得到新的 `bundle_id` 和 `content_hash`（知识内容不变，哈希随基线变），再按新哈希批准、应用。

## 4. 禁止

- 不用编辑器直接改 `knowledge/**/*.md` 和 `data/knowledge/*.json`
- 不读、不改 `.local/`（包括 SQLite），那是可以丢弃的检索投影
- 不跳过 `validate`；不用 `bundle-create --manifest`；不跳过批准直接用低层命令写库
- 不擅自改动 `project-intelligence.json` 里的身份、权限与 Authority 语义

## 5. 权限约定

- `public`：可以对外发布给网页 / 微信用户的内容
- `internal`：只给内部看的内容，默认不对外
- 同一条 Claim 的 permission 必须和它所属 Topic 一致
