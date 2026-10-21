# 交接文档 · 系统汉字（知识库 + 对外问答网页）

> 交接日期：2026-10-20　交接范围：`D:\系统汉字` 全目录
> 读这份之前先读 `AGENTS.md`（项目契约，23 行，硬规则都在里面），再读 `memory/OPERATING.md`。

---

## 1. 一句话现状

知识库 **193 条 Claim**（5 节点 / 12 主题，含新录入的「音源字卷」145 条）已入库并通过 `pkc validate`；对外问答网页（`web/`）已跑通、公网可访问。**新增「字卡模式」**：输入一个字，按「甲骨文字形图 → 字根 → 本义 → 转义 → 衍生字义」五栏作答（字根栏回答「仕的字根是士」这类问题，并说清两者的构形关系），字形图取自《系统汉语》原稿（1057 字 / 2557 张图 / 194 张实物配图，图内自带出处与分期；字本身没有字形行的，退一步给字根的字形与配图）。代码已提交（`10641b3`），后续字根栏在 `47f25e7` 之后继续改。

## 2. 现在的运行态（接手后先确认这两个进程）

| 进程 | 命令 | 现场 |
| --- | --- | --- |
| 问答服务 | `node web/server.mjs` | 监听 `127.0.0.1:8088`（PID 用 `Get-NetTCPConnection -LocalPort 8080` 查） |
| 公网隧道 | `cloudflared tunnel --url http://127.0.0.1:8088 --no-autoupdate --metrics 127.0.0.1:20243` | 后台作业 `pwsh-73da8eb360424be7` |

对外地址（**临时，重启即换**）：
`https://drop-pilot-scanners-gives.trycloudflare.com`
（2026-10-20 13:16 重启过一次，旧地址 `hide-chicago-fixed-dream` 已失效；日志落在 `web\.cache\tunnel.err`、`web\.cache\server.log`）

实测：公网 `/api/health` 返回 `claims:193`；经隧道问「音源字卷的卷一·雞讲了什么」3.6 秒返回带 `clm_…` 引用的答案。

注意两点：
1. 这两个进程都挂在会话的后台作业里，**会话空闲久了会被回收**——实测上一对进程在空闲约 19 分钟后同时消失，日志里没有任何报错。接手第一件事是双击 `web\start.cmd` 自己起一份，拿到自己的 URL。
2. 启动前先确认 8080 是否已被占用：排查时曾发现机器上同时跑着两个实例（8080 一个、8091 一个），对着错的实例调半天。

## 3. 目录与文件

| 文件 | 大小 | 职责 | 能不能随便改 |
| --- | --- | --- | --- |
| `web\server.mjs` | 24.0 KB / 733 行 | 零依赖 Node 服务：路由、检索编排、字卡编排、SSE、静态文件、限流 | 可以，改完按第 8 节自测 |
| `web\pkc-bridge.py` | 3.7 KB / 123 行 | 调 `pkc` 的桥：强制 UTF-8、补 mingit PATH、参数不过 shell | 谨慎，编码逻辑别动 |
| `web\public\index.html` | 18.6 KB / 483 行 | 单文件前端：字卡、问答、引用芯片、抽屉面板 | 可以，纯前端 |
| `web\public\glyphs\` | 23.9 MB / 1057 字 / 2557 图 | 字形图 + 实物配图：`index.json` + `字/01.png`… + `photos/字/01.jpg`（配图说明在索引里） | **生成物，别手改**，重跑 `tools\extract-glyphs.mjs` |
| `tools\extract-glyphs.mjs` | 14.5 KB / 365 行 | 从 `D:\字谱智能体\*.docx` 抽字形图 → `web\public\glyphs`（零依赖，自带 zip 解析） | 可以 |
| `web\start.cmd` | 0.5 KB | 双击启动：服务 + 隧道 | 可以 |
| `web\bin\cloudflared.exe` | 52.8 MB | 隧道二进制，v2026.10.1 | 不要进 git（已 ignore） |
| `web\README.md` | 4.4 KB | 网页服务的说明（面向使用者） | 可以 |
| `prompts\web-kb.prompt.md` | — | 当初用来生成这套服务的项目级提示词 | 可以，是本项目「再造一个」的模板 |

除此之外**一个文件都没动**：`knowledge/`、`data/`、`memory/`、`project-intelligence.json` 全部原样。

## 4. 启动 / 停止 / 换配置

```powershell
# 一键（推荐）
D:\系统汉字\web\start.cmd

# 或者分开跑
C:\Users\萧磊\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\node\bin\node.exe D:\系统汉字\web\server.mjs
D:\系统汉字\web\bin\cloudflared.exe tunnel --url http://127.0.0.1:8088 --no-autoupdate

# 停：关掉那两个窗口即可（没有守护进程、没有服务注册表项）
```

环境变量（都有默认值，不设也能跑）：

| 变量 | 默认 | 说明 |
| --- | --- | --- |
| `PORT` | `8088` | 只绑 127.0.0.1，不对外 |
| `DEEPSEEK_API_KEY` | 读 `C:\Users\萧磊\.dsh\secrets\deepseek.key` | 当前 Key 掩码 `sk-0c1…71fe` |
| `DEEPSEEK_BASE` | `https://api.deepseek.com` | 换兼容端点时用 |
| `DEEPSEEK_MODEL` | `deepseek-chat` | |

没有 Key 时自动进「检索骨架模式」：照样返回命中的 Claim 原文，但不调模型——不会崩，只是答得生硬。

## 5. 数据流

```
浏览器 --POST /api/ask--> server.mjs
   └─> spawn(python web/pkc-bridge.py query "<问题>" 8)
          └─> pkc query --level 2 --permission public --limit 8   （词法 BM25 检索）
   └─> 对前 8 条逐条 pkc show-claim（取 statement 全文，含「适用边界」）
   └─> DeepSeek chat/completions（stream=true）逐块转发
   └─> SSE: sources → delta* → done
前端：把 [clm_…] 渲染成芯片，点击 --> GET /api/claim/<id> --> 抽屉里显示原文
```

关键取舍（改之前先想清楚为什么）：
- **不装任何依赖**：不 `npm install`，不用框架。理由是这个目录要能整体搬走、离线可跑；48 条规模用不上框架。
- **检索走 `pkc`，不自己写索引**：AGENTS.md 硬规则，也避免知识被复制出第二份。
- **只喂 8 条**：再多会稀释注意力，且 `pkc` 的 BM25 已经排好序；上下文约 2–4k tokens/次。
- **SSE 而不是轮询/WebSocket**：单向流，浏览器原生支持，隧道下也稳。

### 5.1 字卡模式（本轮新增）

提问里能认出单个汉字时（引号里的字、整句只有一个汉字、或「X的本义/字源/衍生字」这类问法），走字卡分支：

```
POST /api/ask {question, mode:"card"|"chat"|"auto"}
  ├─ detectChar(question) → 字
  ├─ glyphInfo(字) → web/public/glyphs/index.json（5 分钟缓存）→ /glyphs/<字>/01.png… + photos/<字>/01.jpg（原稿实物配图，带说明）
  │    └─ 这个字在原稿里没有独立字形行（只是字族成员）时，退一步用字根的字形与配图，卡片上注明 from: 字根
  ├─ retrieveForChar(字) → pkc query 12 条 → 只保留 public+active
  │    └─ direct = 标题或正文真的出现这个字的条目（这才是能给它背书的证据）
  ├─ findRoot(字, direct) → 从「从人从士」「从口㠯声」里找字根
  │    └─ 字根本身的条目再查一遍，作为第二组证据一起喂给模型
  ├─ direct 为空 → mode:"none"，只给字形图 + 「还没有专门条目，暂不推断」
  ├─ direct 非空 → DeepSeek 按 CARD_PROMPT 输出 JSON {"字形","字根","本义","转义","衍生"}
  │    └─ sanitizeSection()：引用不在 allowed 集合里 → 该栏作废（这是防臆造的唯一闸门）
  └─ SSE: card-start(char,glyph) → sources → card{sections,glyph,mode,note,root} → done
```

五栏顺序固定：**字形 → 字根 → 本义 → 转义 → 衍生字义**。字根这一栏专门回答「仕的字根是士」这类问题，并说清字根与这个字的关系（会意/形声、意义怎么进来的）。

九个坑（都实际踩过）：
1. **提示词用中文键、代码用拼音键**：`CARD_SECTIONS[].field` 存中文键，取值 `obj[field] ?? obj[label] ?? obj[key]`，否则每一栏永远 missing。
2. **`id.toUpperCase()` 把 `clm_` 前缀也大写了**：必须 `'clm_' + id.slice(4).toUpperCase()`，否则引用全被当无效丢掉。
3. **模型漏写引用 = 该栏作废**：宁可显示「条目里还没有这一项」，也不接受无出处的话。
4. **字形图按「字族标签组」切分**：卷八里 `虎` 只是 `虍` 的字族成员，图在 `（𧇁hū）：…图…虎` 这一行末尾，解析要按「图片串 + 末尾单字标签」分组（详见 `tools/extract-glyphs.mjs` 的 `LABEL` 与 `flush()`）。
5. **原稿的字形行与字族表是分开排的**：`（shì）：` 这种只写拼音的行认不出主人，要先看分组标签落进谁的字族表，再按「部头里字头出现的顺序，取下一个没用过的」兜底（`PART` + `partHeads` + `usedHeads`）；修好后 `unmatched` 从 41 降到 0，`士` 才拿到自己的 7 张图。
6. **实物配图不是字形图**：原稿里 `[图片]` 紧跟一段 `▲公牛` 才是配图，按定义行 / 字族衍義里的衍生字条目归属，存到 `photos/<字>/`，说明文字进索引。
7. **模型会把上下文里的编号当出处**：`cardContext()` 用 `[1] [2]` 编号，模型就写 `[1]`；`sanitizeSection(raw, allowed, order)` 必须拿编号表把它映射回 `clm_` id，否则整张卡会掉进 fallback。
8. **字根不能乱认**：条目自称「X是音源字」或明说「析形不确」的不设字根（否则「士」会被认成从「一」）；候选多于一个时优先取「知识库里有自己主题（X部）」的那个，`台` 因此得到 `㠯` 而不是 `口`。
9. **清空再重建**：`extract-glyphs.mjs` 每次先 `rmSync(OUT)`，否则上一轮多出来的图会留在磁盘上（索引里已经没有它们），体积和字数对不上。

## 6. 接口

| 方法 | 路径 | 入参 | 出参 |
| --- | --- | --- | --- |
| GET | `/api/health` | — | `{ok, pkc:"0.2.0rc5", claims:193, mode:"model"\|"skeleton"}` |
| GET | `/api/tree` | — | `{ok, nodes:[{id,title,topics:[{id,title,claims}]}], claims}`，缓存 60 秒 |
| GET | `/api/glyph?char=台` | 任意汉字（URL 编码） | `{ok, char, glyph:{doc, variants, files:["/glyphs/台/01.png"…], photos:[{file, caption}]}}`，没有则 `glyph:null` |
| GET | `/api/claim/<clm_id>` | 路径参数须匹配 `^clm_[0-9A-F]{20,40}$` | `{ok, claim:{id,title,statement,node_id,topic_id,permission,lifecycle}}` |
| POST | `/api/ask` | `{question, mode?}`，`mode`=`card`\|`chat`\|`auto`（缺省 auto）；≤64KB 请求体、≤200 字问题 | `text/event-stream`：问答 `sources` → `delta`* → `done`；字卡 `card-start` → `sources` → `card` → `done`；出错 `error` |

前端深链接：`/?q=台` 直接出字卡，`/?q=六书是什么&mode=chat` 直接问答（方便在微信/文档里发链接）。

限流：每 IP 20 次/分钟（进程内 Map，重启清零），超了返回 429。

## 7. 五个必须知道的坑（都是踩过的，别重犯）

1. **中文乱码（最坑）**
   `pkc` 被重定向时按控制台码页（GBK）输出；桥如果再用 `sys.stdout.write` 写，会被二次编成 GBK。
   → 子进程 `env` 里设 `PYTHONIOENCODING=utf-8` + `PYTHONUTF8=1`，并且桥**用 `sys.stdout.buffer.write(text.encode("utf-8"))`** 写字节。两处都要做。

2. **`[WinError 2] 系统找不到指定的文件`**
   直接 spawn `.runtime\venv\Scripts\pkc.exe`，PATH 上缺 `.runtime\mingit\cmd` 就报这个（pkc 内部要调 git）。
   → 桥里把 mingit 目录前置到 `PATH`。

3. **检索永远 0 条**
   早期默认 `--level 1`，只搜节点/主题标题，Claim 根本不可达。
   → `query` 必须显式 `--level 2`。

4. **不要加 `--status current`**
   全库 Claim 的 `authority_status` 都是 `not_registered`，加了直接过滤成 0 条。

5. **用户问题别拼命令行**
   问题来自公网。→ Node 用参数数组 spawn、桥用 `subprocess.run([...])` 不走 shell。任何「拼字符串再执行」的写法都是漏洞。

另外两个已知限制（不是 bug）：`progressive-query` 现在不可用（`relations.context_nodes` 没配，报 `RETRIEVAL_CANDIDATE_UNKNOWN`）；`knowledge-search` 只回标题元数据、没有正文。

## 8. 验收记录（2026-10-20 实测，改完请重跑第 3–5 条）

| 验收项 | 期望 | 实测 |
| --- | --- | --- |
| `.\tools\pkc.cmd validate` | ok，48 条 | ✅ 4 节点 / 8 主题 / 48 Claim，errors 空 |
| `curl 127.0.0.1:8088/api/health` | `claims:193` | ✅ `mode=model` |
| 问「『六书』之名最早见于哪部书？」 | 《周礼·地官·保氏》+ 引用 | ✅ 1.6 s，引 `clm_269C128453E306F1DDE7B94294` |
| 问「班固和许慎的六书次序有什么不同？」 | 分引两条，不混为一谈 | ✅ 2.8 s，引 `clm_5C50…E0` / `clm_8328…B9`，并说明库里没有次序对比 |
| 问「部首一共多少个？」 | 「知识库里还没有这方面的内容。」 | ✅ 0.3 s，命中 0，不调模型（`topic-components` 是空主题） |
| 问「什么是声母拟态？」 | 多引 + 边界说明 | ✅ 3.2 s，8 条命中，七组声母逐个引 |
| 隧道端到端 | 页面/问答可用 | ✅ 页面 0.5 s，问答 2.1 s |
| 问「台」（字卡） | 字形图 + 字根 + 本义/转义/衍生字义，每栏带引用 | ✅ 6 张字形图（春秋/戰國），五栏齐全，字根 = 㠯，引 `clm_FF5E14` / `clm_51B84D` / `clm_D0E442` / `clm_F2B969` |
| 问「仕」（字卡） | 字根是士，并说清关系；仕自己没有字形行，退给士的图 | ✅ 7 张士的字形图 + 1 张公牛配图（注明 `from: 士`），字根栏「士：仕从人从士…」 |
| 问「士」（字卡） | 字形图 + 公牛配图 | ✅ 7 张字形图 + 1 张公牛（`▲公牛`），本义「雄性」 |
| 问「奚」（字卡） | 借音字不编字根 | ✅ `mode:"fallback"`，退回条目原文 |
| 问「雞」（字卡） | 字卡，库里缺的栏如实显示 | ✅ 8 张字形图，本义/转义显示「条目里还没有这一项」 |
| 问「龍」（字卡，库里没有） | 只给字形图 + 说明，不编字义 | ✅ `mode:"none"`，附「暂不推断」 |
| 问「今天天气怎么样」（无单字） | 退回问答 | ✅ 命中 0，答「知识库里还没有这方面的内容。」 |
| `GET /glyphs/台/01.png` | 200 + `image/png` | ✅ 4390 字节 |
| `GET /glyphs/photos/士/01.jpg` | 200 + `image/jpeg` | ✅ 原稿实物配图（公牛） |
| `git status` | 只有 `web/`、`prompts/`、`.gitignore` | ✅ `git diff --check` 干净 |

## 9. 已知边界与风险

- **检索是词法 BM25，不是语义向量**：同义词、口语化问法可能召不回。库到几百条以上要补 `data/knowledge/evaluation/retrieval-cases.json` 做回归。
- **4 个主题是空的**（字源与形体演变、部件与偏旁部首、读音与字义、规范与易错辨析）：问到「部首有多少个」这类问题，系统只会老实说没有——这是设计如此，不是故障。
- **没有鉴权**：拿到链接的人都能问、都能烧 Key 的额度。限流只是每 IP 20 次/分钟的内存计数。
- **隧道没有 SLA**：匿名 `trycloudflare.com` 隧道随时可能断、URL 每次变；Cloudflare 条款也只建议用于试验，不承诺生产。
- **Key 是明文文件**：`C:\Users\萧磊\.dsh\secrets\deepseek.key`，靠本机文件权限保护，不是加密存储。换机器要重新配。
- **单进程、无持久日志**：只打到 stdout，进程没了日志也没了；要排查得自己加落盘。
- **费用**：每次提问 1 次 `deepseek-chat` 调用（约 2–4k 输入 + ≤800 输出 tokens），问答本身不额外计费。

## 10. 排查手册

| 症状 | 先看哪里 | 处理 |
| --- | --- | --- |
| 页面打不开 | 隧道窗口是否还在跑；`/api/health` 本地是否通 | 重启 `start.cmd`，URL 会变，重新发链接 |
| 中文全是乱码 | 是否有人改了 `pkc-bridge.py` 的输出方式 | 回到 `sys.stdout.buffer` 写法（第 7 节第 1 条） |
| 明明库里有，却说「还没有」 | 换一种说法再问；看 `/api/tree` 该主题条数 | 是 BM25 没召回，不是数据丢失；必要时提高 `RETRIEVE_LIMIT` |
| 429 | 同一 IP 提问过密 | 等 1 分钟，或调 `RATE_MAX` |
| 「模型服务连不上」「模型返回 401/402」 | Key 文件是否存在、额度是否用完 | 换 Key 或充值；无 Key 时服务会退化到骨架模式 |
| 点引用 404 | claim id 是否合法、库是否被 rebuild 过 | 正常重建不会让 id 失效；404 多半是手拼了假 id |
| `pkc` 报错 | `.\tools\pkc.cmd validate` | 先跑自检，看 errors 数组 |

## 11. 改动指引

- **改回答口吻/规则** → `web/server.mjs` 的 `SYSTEM_PROMPT`（第 5 节那六条规则）。改完一定要重跑「班固和许慎」那条——它最容易暴露上下文不足。
- **改字卡的填写规则** → 同文件 `CARD_PROMPT`；改完重跑「台」「雞」「龍」三张卡，确认引用没被 `sanitizeSection()` 全部判废。
- **重抽字形图**（换了 Word 原稿才需要）：
  ```powershell
  C:\Users\萧磊\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\node\bin\node.exe D:\系统汉字\tools\extract-glyphs.mjs --src "D:\字谱智能体" --out "D:\系统汉字\web\public\glyphs"
  ```
  输出 `{docs, rows, unmatched, chars, files, bytes}`；当前基线 `24 卷 / 240 字形行 / 0 行未配上字头 / 1057 字 / 2557 图 / 194 张配图 / 23.9 MB`。重抽后服务不用重启（`index.json` 5 分钟缓存会自动过期）。
- **改召回条数** → 同文件 `RETRIEVE_LIMIT`（检索几条）与 `CONTEXT_CLAIMS`（喂几条全文）。当前都是 8；之前设 4 时会误判「库里没有记载」。字卡另走 `retrieveForChar()` 的 12 条。
- **换模型/端点** → 环境变量，别改代码。
- **加缓存** → 建议加在 `retrieve()` 外层，key 用清洗后的问题；注意 `pkc rebuild` 后要能失效。
- **加鉴权** → 在 `createServer` 最前面加一层口令校验，别只在前端做。
- **改前端** → 直接编辑 `web/public/index.html`，服务端不用重启（静态文件每次读盘）。

## 12. 待办（按优先级）

1. **把 `intake/` 里逐字草稿走完 knowledge-plan**：`卷二·㠯部`（41 条）、`卷二·士示`、`卷二·帝等`（33 条）、`卷一·雞`（32 条，目前只 apply 了 3 条）——字卡的四栏全靠这些条目；现在 `台` 能出全四栏，`雞` 只有字形、`奚` 只有衍生，就是条目还没录。
2. **补字形库覆盖**：`extract-glyphs.mjs` 报 `unmatched:41`（41 行字形没配上字头，多半是字头写法特殊或跨页），另有部分字族成员没图；要全覆盖得先人工看这 41 行。
3. **固定域名**：Cloudflare Named Tunnel + 已备案域名（当前匿名隧道不承诺可用性）。
4. **访问口令**：至少加 Basic Auth，避免链接裸奔、额度被刷。
5. **补空主题**：先把「部件与偏旁部首」「字源与形体演变」补起来，最常被问。
6. **更新 `memory/CURRENT.md` 第 12 行**（还写着「对外服务还没开始」），并把 `web/`、`tools/extract-glyphs.mjs`、`prompts/` 提交进 git（现在 `git status` 是 `M .gitignore`、`?? prompts/`、`?? web/`、`?? tools/`）。
7. **检索回归用例**：`data\knowledge\evaluation\retrieval-cases.json` 已有骨架（`cases` 是空的），把第 8 节那几条问题填进去。

## 13. 资产与账号清单

| 资产 | 位置/归属 | 备注 |
| --- | --- | --- |
| 知识库与全部配置 | `D:\系统汉字` | 整个目录可整体搬走：`.runtime/` 自带 Python 3.12.10 + PKC venv + MinGit |
| DeepSeek API Key | `C:\Users\萧磊\.dsh\secrets\deepseek.key` | 掩码 `sk-0c1…71fe`；不在 git 里，也不在项目目录内 |
| Cloudflare 账号 | **没有**，用的是匿名隧道 | 要做固定域名需自备账号 + 域名 |
| 隧道二进制 | `web\bin\cloudflared.exe` v2026.10.1 | 52.8 MB，已在 `.gitignore` |
| 未提交改动 | `web/`、`prompts/`、`.gitignore` | 交接时请确认由谁提交 |

## 14. 接手第一小时清单

1. 读 `AGENTS.md` → `memory/OPERATING.md` → `memory/CURRENT.md`。
2. 跑 `.\tools\pkc.cmd validate`，确认 48 条、errors 空。
3. 双击 `web\start.cmd`，拿到自己的 `trycloudflare.com` 地址，用无痕窗口问一句「什么是声母拟态？」。
4. 问一句库里没有的（比如「部首一共多少个？」），确认它会老实说没有——这是这个系统最重要的性质。
5. 看一遍 `web\server.mjs`（436 行，一个文件读完），特别是 `retrieve()` 和 `SYSTEM_PROMPT`。
6. 决定第 12 节哪一项先做，再动代码。

---

**交接原则一句话**：知识只能通过 `pkc knowledge-plan` 那套流程改，网页只负责「检索 + 组织 + 标注出处」；任何让模型「凭常识补一句」的改动，都是把系统最有价值的部分拆掉。
