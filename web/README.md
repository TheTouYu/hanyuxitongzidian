# 系统汉字 · 知识库问答网页

只做两件事：把用户问题交给 `pkc` 检索，把检索到的 Claim 组织成**带出处**的答案；
以及**字卡模式**：输入一个字，按「甲骨文字形图 → 本义 → 转义 → 衍生字义」四段作答。
服务层只经由 `pkc` 读库，不直接读 `knowledge/**`，也不读 `.local/`、不复制知识出去。

## 结构

```
web/
├── server.mjs          零依赖 Node 服务（HTTP + SSE + 静态文件 + 字卡编排）
├── pkc-bridge.py       调 pkc 的桥：强制 UTF-8、补 mingit PATH、参数不过 shell
├── public/index.html   单文件前端（字卡 / 问答两种模式、引用芯片可点开原文）
├── public/glyphs/      字形图库（941 字 / 2070 张，由 tools/extract-glyphs.mjs 生成）
├── start.cmd           双击启动：服务 + 隧道
├── bin/cloudflared.exe 隧道的二进制（约 53MB，不入 git）
└── README.md
```

## 启动

```powershell
# 服务（前台）
C:\Users\萧磊\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\node\bin\node.exe D:\系统汉字\web\server.mjs

# 公网隧道（另开一个窗口）
D:\系统汉字\web\bin\cloudflared.exe tunnel --url http://127.0.0.1:8080 --no-autoupdate
```

或直接双击 `start.cmd`，它会启动服务并开隧道，把 `https://xxx.trycloudflare.com` 打进窗口。

隧道地址**每次启动都变**；免费版无 SLA，适合短期演示。长期方案：Cloudflare Named Tunnel + 已备案域名。

## 配置（环境变量，都有默认值）

| 变量 | 默认 | 说明 |
| --- | --- | --- |
| `PORT` | `8080` | 只监听 127.0.0.1 |
| `DEEPSEEK_API_KEY` | 读 `C:\Users\萧磊\.dsh\secrets\deepseek.key` | 只在服务端使用，日志打掩码 |
| `DEEPSEEK_BASE` | `https://api.deepseek.com` | 换兼容端点时用 |
| `DEEPSEEK_MODEL` | `deepseek-chat` | |

没有 Key 时自动进入**检索骨架模式**：照样展示命中的 Claim 原文与出处，但不用模型组织答案。

## 接口

| 方法 | 路径 | 说明 |
| --- | --- | --- |
| GET | `/api/health` | `{ok, pkc, claims, mode}`，`mode` 为 `model` / `skeleton` |
| GET | `/api/tree` | 5 节点 / 12 主题 / 各自 Claim 数（缓存 60 秒） |
| GET | `/api/glyph?char=台` | 单字的字形图列表 `{ok, char, glyph:{doc, variants, files}}` |
| GET | `/api/claim/<clm_id>` | 单条 Claim 全文（引用展开用） |
| POST | `/api/ask` | `{question, mode?}` → SSE |

`POST /api/ask` 的两种事件流：

- 问答（`mode:"chat"`，或问题里认不出单字）：`sources` → `delta*` → `done`
- 字卡（`mode:"card"`，或问题里正好有一个汉字）：`card-start` → `sources` → `card` → `done`

`card` 事件里：`sections` 是 `[{key,label,text,cites}]` 或 `[{key,label,missing:true}]`，
`mode` 是 `model`（模型按条目整理）/ `fallback`（模型不可用，直接给条目原文）/ `none`（库里没有这个字的条目）；
`glyph.files` 是 `/glyphs/<字>/01.png` 这类路径。

## 字卡的四段与防臆造

1. **字形**：`public/glyphs` 里的图就是原稿的甲骨文/金文/戰國字形，图下小字自带出处与分期（如「合 5268 一期」），服务端只负责按字取图。
2. **本义 / 转义 / 衍生字义**：由模型从检索到的条目里摘，但**每段末尾必须带 `[clm_…]`，且 id 必须在本次检索到的条目里**；没有有效引用的段落会被直接丢弃，显示「条目里还没有这一项」。
3. 只有「标题或正文里真的出现这个字」的条目，才算能给它背书的证据（`retrieveForChar` 的 `direct`）；一条都没有时，字卡只给字形图 + 一句「暂不推断」，不拿泛泛的通论条目凑数。

## 实测记录（2026-10-20）

| 验收项 | 结果 |
| --- | --- |
| `pkc validate` | 通过（193 条 Claim） |
| `/api/health` | `claims=193, mode=model` |
| 「六书」之名最早见于哪部书？ | 答《周礼·地官·保氏》，引 `clm_269C128453E306F1DDE7B94294` |
| 班固和许慎的六书次序有什么不同？ | 分别引 `clm_5C50FFEB1D36EA56956F1AE7E0`、`clm_8328C2C044A52D57D10BCD3CB9`，并说明库里没有次序对比的专门记载 |
| 部首一共多少个？ | 检索命中 0 → 直接回「知识库里还没有这方面的内容。」 |
| 什么是声母拟态？ | 8 条命中，引用七组声母 + 边界说明 |
| 字卡「台」 | 6 张字形图（春秋 / 戰國），本义、转义、衍生字义齐全并带引用 |
| 字卡「雞」 | 8 张字形图；本义、转义如实显示「条目里还没有这一项」 |
| 字卡「龍」（库里没有） | 只给字形图 + 「暂不推断」 |
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
- 云端**没有**登录和权限控制：链接谁拿到谁能用。要限制访问得自己加口令或换 Named Tunnel + Access。

## 改知识库后

网页不用重启（每次提问都现查）；`/api/tree` 有 60 秒缓存。改库仍然只走 `pkc knowledge-plan` 那套流程，见项目根 `AGENTS.md`。
