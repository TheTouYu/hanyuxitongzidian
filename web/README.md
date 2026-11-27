# 系统汉字 · 知识库问答网页

只做两件事：把用户问题交给 `pkc` 检索，把检索到的 Claim 组织成**带出处**的答案；
以及**字卡模式**：输入一个字，按「分级 → 声母义 → 甲骨文字形图（含原稿实物配图）→ 字根 → 本义 → 转义 → 衍生字义」七栏作答。
服务层只经由 `pkc` 读库，不直接读 `knowledge/**`，也不读 `.local/`、不复制知识出去。

## 结构

```
web/
├── server.mjs          零依赖 Node 服务（HTTP + SSE + 静态文件 + 字卡编排 + 会员闸门）
├── member.mjs          会员 / 试用 / 兑换码 / 订单（零依赖，JSON 单文件存储）
├── pkc-bridge.py       调 pkc 的桥：强制 UTF-8、补 mingit PATH、参数不过 shell
├── public/zigen.json   部/卷/章索引（608 部 / 100 卷 / 12 章，由 tools/zigen-index.mjs 生成）
├── public/index.html   单文件前端（字卡 / 问答两种模式、引用芯片可点开原文、开通会员面板）
├── public/admin.html   后台（生成开通码、会员、订单、收入），地址 `/admin`
├── public/glyphs/      字形图 + 实物配图（5507 字条 / 2502 个有图字 / 20498 图 + 956 张配图 + 1244 条字族表，由 tools/extract-glyphs.mjs 全量生成；每字不设上限，原稿有几张收几张）
├── data/               运行时数据（shop.json 会员/订单、admin.key 管理密码、secret.key 签名密钥）——**不进 git**
├── start.cmd           双击启动：服务 + 隧道
├── bin/cloudflared.exe 隧道的二进制（约 53MB，不入 git）
└── README.md
```

## 启动

```powershell
# 服务（前台）
C:\Users\萧磊\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\node\bin\node.exe D:\系统汉字\web\server.mjs

# 公网隧道（另开一个窗口）
D:\系统汉字\web\bin\cloudflared.exe tunnel --url http://127.0.0.1:8088 --no-autoupdate
```

或直接双击 `start.cmd`，它会启动服务并开隧道，把 `https://xxx.trycloudflare.com` 打进窗口。

隧道地址**每次启动都变**；免费版无 SLA，适合短期演示。长期方案：Cloudflare Named Tunnel + 已备案域名。

### 常驻守护（2026-11-27 装）

计划任务「系统汉字-网页守护」每分钟执行一次 `web\keepalive.ps1`：服务或隧道掉了自动拉起；公网连续 3 次不通（quick tunnel 会被云端回收）就换一条隧道。最新公网地址写在 `web\.cache\当前公网地址.txt`。

任务的启动动作是 `wscript.exe //B //NoLogo "D:\系统汉字\web\keepalive-hidden.vbs"`：由这个 VBS 以窗口样式 0 调起 PowerShell，**所以每次巡检不会弹黑色控制台窗口**（2026-11-27 主人要求「不要再弹」）。不要把动作改回直接跑 `powershell.exe`——`-WindowStyle Hidden` 对控制台程序无效，每分钟仍会闪一个 `C:\WINDOWS\System32\WindowsPowerShell\...` 窗口并抢焦点。

- 查状态：`schtasks /query /tn "系统汉字-网页守护" /fo list`
- 立即巡检一次：`schtasks /run /tn "系统汉字-网页守护"`
- 日志：`web\.cache\keepalive.log`（只在有动作时写）
- 临时停用：`schtasks /change /tn "系统汉字-网页守护" /disable`（恢复用 `/enable`）
- 守护任务在跑时**不要**再双击 `start.cmd`，会多开一条隧道、地址反而乱。

## 配置（环境变量，都有默认值）

| 变量 | 默认 | 说明 |
| --- | --- | --- |
| `PORT` | `8088` | 只监听 127.0.0.1 |
| `DEEPSEEK_API_KEY` | 读 `C:\Users\萧磊\.dsh\secrets\deepseek.key` | 只在服务端使用，日志打掩码 |
| `DEEPSEEK_BASE` | `https://api.deepseek.com` | 换兼容端点时用 |
| `DEEPSEEK_MODEL` | `deepseek-chat` | |
| `SITE_URL` | 空（话术里用 `location.origin`） | 公网地址，如 `https://xitonghanzi.com`，后台「复制开通话术」用它拼链接 |

没有 Key 时自动进入**检索骨架模式**：照样展示命中的 Claim 原文与出处，但不用模型组织答案。

## 接口

| 方法 | 路径 | 说明 |
| --- | --- | --- |
| GET | `/api/health` | `{ok, pkc, claims, mode}`，`mode` 为 `model` / `skeleton` |
| GET | `/api/tree` | 5 节点 / 12 主题 / 各自 Claim 数（缓存 60 秒） |
| GET | `/api/glyph?char=台` | 单字的字形图与配图 `{ok, char, glyph:{doc, variants, files, photos:[{file,caption}]}}` |
| GET | `/api/claim/<clm_id>` | 单条 Claim 全文（引用展开用） |
| POST | `/api/ask` | `{question, mode?}` → SSE |

会员与试用：

| 方法 | 路径 | 说明 |
| --- | --- | --- |
| GET | `/api/pricing` | 三档价格 + 试用额度 `trial_budget_yuan` + `site_url` |
| GET | `/api/me` | 当前会员/试用状态：`trial{used,left,budget_yuan,spent_yuan,remaining_yuan}`、`member`（含 `has_password`） |
| POST | `/api/redeem` | `{code, phone, password}` 开通：设登录密码（≥6 位）、建会员、下发 HttpOnly cookie `sh_mid`；手机号已注册过则报错并提示直接登录 |
| POST | `/api/login` | `{phone, password}` 账号密码登录，下发 `sh_mid`；失败 401「手机号或密码不对」，同一 ip+手机号 10 分钟最多 8 次（429） |
| POST | `/api/logout` | 清 `sh_mid` |
| POST | `/api/password` | 已登录改密码 `{old_password, new_password}` |
| POST | `/api/admin/login` | 管理密码登录（cookie `sh_admin`，7 天） |
| GET | `/api/admin/stats` | 收入 / 会员数 / 码 / 订单 / 试用人数 |
| GET·POST | `/api/admin/codes` | 列出 / 批量生成开通码（`{tier, count, note}`；`free:true` = 补开/赠送，不记收入） |
| GET·POST | `/api/admin/orders` | 列出订单 / 手工登记收款并开通（线下收钱时用） |
| GET | `/api/admin/members` | 会员列表（含 `active`、`used_today`、`spent_today`、`has_password`；**不返回 `pass_hash`**） |
| POST | `/api/admin/rebind` | 给已有会员生成「换设备补发码」（`price: 0`、绑定原会员，兑换不新建会员、不记账） |
| POST | `/api/admin/reset-password` | 主人给会员改密码 `{member_id, password}`（客户忘记密码时用） |
| POST | `/api/admin/revoke`·`/api/admin/gift`·`/api/admin/logout` | 撤销会员 / 标记赠书已寄 / 退出 |

**闸门**：`/api/ask` 先过 `gateAsk()`——会员按当日花费（默认 3 元）与次数（300 次）封顶；非会员按设备记试用（默认 10 次、累计花费 1 元封顶），超出返回 `402 {need_membership:true}`，会员超额返回 `429`。模型调用出错时 `res.on('finish')` 会退掉本次试用次数与花费（不扣用户额度）。

`POST /api/ask` 的两种事件流：

- 问答（`mode:"chat"`，或问题里认不出单字）：`sources` → `delta*` → `done`
- 字卡（`mode:"card"`，或问题里正好有一个汉字）：`card-start` → `sources` → `card` → `done`

`card` 事件里：`sections` 是 `[{key,label,text,cites}]` 或 `[{key,label,missing:true}]`，
`mode` 是 `model`（模型按条目整理）/ `fallback`（模型不可用，直接给条目原文）/ `none`（库里没有这个字的条目）；
`glyph.files` 是 `/glyphs/<字>/01.png` 这类路径；`glyph.photos` 是原稿的实物配图（`/glyphs/photos/<字>/01.jpg`，说明文字同时进索引，前端显示 <40 字的短说明）；
`family` 是原稿字头行冒号后那串字族成员，按原稿顺序：`[{char, photos:[{file,caption}]}]`，前端在字卡末尾列字族表，并把每个成员的配图放在**那个字头后面**。

## 字卡的几栏与防臆造

0. **分级**：由服务端 `levelOf()` 判定，模型不得改动。一级字根 = 609 部的部首字（`zigen.json` 的 `byName`，含部号、卷名、页码；异体或隶变写法如「以」之于「㠯」同按一级）；部内还能滋生新字的为二级、三级字根（`spawnsFrom`：有「X部」条目、自称音源字、或别的字「从 X 声」）；其余为谐声字，并给出声符链（如「始」：㠯 → 台 → 始）。这一栏永远排在第一节，`retrieveForChar` 无直接条目时也照给（如「龍」）。
1. **声母义**：由服务端 `shengmuOf()` 从「声母义（分部）」主题（`knowledge/hanzi-yinyuan/02z-shengmu-yi.md`，`topic-shengmu-yi`）按该字所属部取出，模型不得改写。一条含声母、部位、绪论七组拟态义名与一致度（如「匃部：g（喉牙音），拟态义『隔估』……同部位 42 字，占 71%……一致度强」）；零声母诸部只给一句「读零声母，不系拟态声母义」。这一栏永远排在分级之后。
2. **字形**：`public/glyphs` 里的图就是原稿的甲骨文/金文/戰國字形，图下小字自带出处与分期（如「合 5268 一期」），服务端只负责按字取图。原稿在字形行下面还排了**实物配图**（如「士」下面一张公牛、「里」下面一张土地庙），一并抽出来放在字形图条下方；这个字在原稿里没有独立字形行时（如「仕」只是「士」的字族成员），退一步用它字根的字形与配图，卡片上注明「取自字根“士”」。
   - 字族：原稿字头行冒号后那串（如「士：**牡**（…）**社**（…）**仕**…」）按原稿顺序列在字卡末尾；原稿排在某个字族成员后面的配图（如「里」字族里「鯉」后面的水层示意图），跟着放在**那个字头后面**，而不是笼统堆在字形条下面。
3. **字根**：从条目里的「从人从士」「从口㠯声」找构字成分，再把字根自己的条目取来当第二组证据，说清会意/形声与意义关系（如「士：仕从人从士，士是音源字，本义指雄性……」）。条目自称「X是音源字」或明说「析形不确」的，不设字根。借音字（如「奚」借鸡鸣之声）也不设。
4. **本义 / 转义 / 衍生字义**：由模型从条目里摘，但**每栏末尾必须带 `[clm_…]`，且 id 必须在本次检索到的条目里**；没有有效引用的栏目会被直接丢弃，显示「条目里还没有这一项」。
5. 只有「标题或正文里真的出现这个字」的条目，才算能给它背书的证据（`retrieveForChar` 的 `direct`）；一条都没有时，字卡只给字形图 + 一句「暂不推断」，不拿泛泛的通论条目凑数。

## 会员与收费（2026-10-21 起）

三档（`member.mjs` 的 `TIERS`）：`y6` 50 元 / 6 个月、`y16` 100 元 / 16 个月（页面标「最划算」）、`life` 500 元 / 10 年并送《系统汉语》一套（248 元、2.8 公斤，`gift:true`）。

- 收钱方式：**先线下收款（微信/支付宝/银行），主人核对后生成开通码发给客户**。后台「开通会员」选档 → 生成码（形如 `C16-EMX7-6AZ9`，前缀 C6/C16/TY）→ 点「复制开通话术」把整段说明发给客户 → 客户在页面「开通会员 → 开通·兑换码」里填手机号 + 码 + 自己设的登录密码（≥6 位）即开通。也可用「订单」里的手工登记（`POST /api/admin/orders`）直接建会员记录。
- **账号登录**：开通后，客户在任何设备打开页面 →「开通会员」→「登录」页签 → 手机号 + 密码即可，不再依赖浏览器 cookie。密码用 `scrypt`（N=16384 默认参、16 字节盐）存哈希，`pass_hash`/`pass_salt` 只在 `shop.json` 里，接口不返回。忘记密码 = 后台会员行「重置密码」，把新密码告诉客户。
- 同一手机号只能注册一次；已注册的号码再拿兑换码兑换会被拒（提示直接登录），避免一个客户多份会员记录。
- 会员身份仍靠 HttpOnly cookie `sh_mid`（签名后带 member id），登录/兑换都会重发；cookie 丢了用手机号+密码登回来即可。
- `SITE_URL`（环境变量）用于生成话术里的链接：后台如果不是从公网地址打开的（比如从 `127.0.0.1:8099` 打开），要设 `SITE_URL=https://你的域名`，否则话术里的链接会带 127.0.0.1。
- 试用（未开通的游客）：每台设备 10 次、累计花费上限 1 元（高峰价保守计，实际一人约 0.03–0.08 元）。游客额度靠 cookie `sh_dev` 记，**清 Cookie 就能重置**——正式对外前可再按 IP 限次或要求登录后才算试用。
- 数据：全在 `web/data/shop.json`（会员、码、订单、试用设备、当日花费），原子写；每次保存前当天首次会另存一份 `shop-YYYY-MM-DD.json` 快照（同目录），误删可从快照恢复。管理密码在 `web/data/admin.key`（首次启动自动生成，12 字节 base64url），Cookie 签名密钥在 `web/data/secret.key`。`web/data/` 已进 `.gitignore`，**含客户手机号，绝不入库、要备份**。
- 后台：`/admin`，输 `web/data/admin.key` 里的密码。功能＝统计、生成码（可勾「补开/赠送（不记收入）」）、看码、会员（搜索手机号、看已设密码/待寄书、标记赠书已寄、重置密码、换设备补发码、撤销）、订单、退出登录。
- 金额口径：`PRICE_IN_YUAN_PER_M=2`、`PRICE_OUT_YUAN_PER_M=8`（高峰价），`usageCost()` 按 token 实算计费；`TRIAL_BUDGET_YUAN`、`MEMBER_DAILY_YUAN`、`MAX_ANSWER_TOKENS=600` 都可用环境变量改。
- 服务在跑时**不要直接删/改 `shop.json`**：进程内存里还有旧数据，任何一次写都会把它写回。要清空先停服务。

## 实测记录（2026-10-20）

| 验收项 | 结果 |
| --- | --- |
| `pkc validate` | 通过（193 条 Claim） |
| `/api/health` | `claims=193, mode=model` |
| 「六书」之名最早见于哪部书？ | 答《周礼·地官·保氏》，引 `clm_269C128453E306F1DDE7B94294` |
| 班固和许慎的六书次序有什么不同？ | 分别引 `clm_5C50FFEB1D36EA56956F1AE7E0`、`clm_8328C2C044A52D57D10BCD3CB9`，并说明库里没有次序对比的专门记载 |
| 部首一共多少个？ | 检索命中 0 → 直接回「知识库里还没有这方面的内容。」 |
| 什么是声母拟态？ | 8 条命中，引用七组声母 + 边界说明 |
| 字卡「台」 | 6 张字形图（春秋 / 戰國），分级判**二级字根**（㠯 → 台），字根「㠯」、本义、转义、衍生字义齐全并带引用 |
| 字卡「以」 | 分级判**一级字根**：㠯 的异体或隶变写法，同属第 8 部 |
| 字卡「始」 | 分级判**谐声字**，声符链「㠯」→「台」→「始」 |
| 字卡「士」/「仕」 | 士 = 一级字根（第 9 部，p32）；仕 = 谐声字（士 → 仕） |
| 字卡「仕」 | 字根栏给「士」（仕从人从士，士是音源字，本义指雄性）；字形图退回「士」的 7 张图 + 公牛配图 |
| 字卡「士」 | 7 张字形图 + 公牛配图；自己是音源字，字根栏如实留空 |
| 字卡「雞」 | 22 张字形图（不设上限）；本义、转义如实显示「条目里还没有这一项」 |
| 字卡「龍」（库里没有条目） | 只给字形图 + 「暂不推断」，但分级栏仍判一级字根（第 117 部，卷二十二「雷」） |
| 隧道访问 | 页面 0.5s、问答 2.1s，正常；字卡 2–4s（含一次模型调用） |

## 实现上几个不能省的细节

1. **必须走 `.runtime\venv\Scripts\pkc.exe` 且 PATH 里有 mingit**，否则 `[WinError 2] 系统找不到指定的文件`。
2. **子进程强制 UTF-8**（`PYTHONIOENCODING`/`PYTHONUTF8`），桥自己用 `sys.stdout.buffer` 写字节——否则中文按 GBK 输出，前端全是乱码。
3. **检索必须显式 `--level 2`**：默认 1 只搜节点标题，Claim 搜不到。
4. **不要加 `--status current`**：全库 Claim 的 `authority_status` 是 `not_registered`，加了会过滤成 0 条。
5. 用户问题**只走参数数组、不开 shell**，避免命令注入。

## 回答规则（`server.mjs` 的 `SYSTEM_PROMPT`）

- 只依据本次检索到的条目；每条结论后标 `[clm_…]`。
- 条目全看过才能说「没有记载」；完全不相关才回「知识库里还没有这方面的内容。」
- 《系统汉语》的观点要标明是书的判断，不是学界共识。
- 不复述内部字段，300 字以内。

## 已知边界

- 检索是 PKC 的**词法 BM25**，不是向量检索：同义词、口语化问法可能召不回。库扩到几百条以上，建议补 `data/knowledge/evaluation/retrieval-cases.json` 做回归。
- 单进程内存限流（每 IP 20 次/分钟），重启即清零。
- 试用靠 cookie 设备号，清 Cookie 可重置；域名备案与微信支付商户号没下来前，只能线下收款 + 手工发码。
- 会员状态存 `web/data/shop.json` 单文件，多实例部署要换成数据库或用共享存储；也没有发票、退款、对账的自动化，先靠后台手工处理。

## 改知识库后

网页不用重启（每次提问都现查）；`/api/tree` 有 60 秒缓存。改库仍然只走 `pkc knowledge-plan` 那套流程，见项目根 `AGENTS.md`。
