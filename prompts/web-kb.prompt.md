# 提示词：把「系统汉字」知识库做成对外网页

> 用法（三选一）
> 1. **贴给代理**：在 `D:\系统汉字` 目录下开一个新会话，把下面「正文」整段贴进去。
> 2. **项目级**：把正文存成 `prompts/web-kb.prompt.md`（本文件），下次说「按 prompts/web-kb.prompt.md 做」即可。
> 3. **让我直接干**：说一句「执行这个提示词」，我按它做完并把验收结果贴给你。
>
> 适用范围：PKC 0.2.0rc5、48 条 Claim（4 节点 / 8 主题）。库扩容后第 2.3 节的数字与第 8 节的测试问题需要同步更新。

---

# 正文（从这里开始交给执行代理）

## 你的角色

你是「系统汉字」仓库的执行代理。任务：在 `D:\系统汉字` 内实现一个**可对外使用的知识库问答网页**——只读检索该库，把 Claim 组织成有出处的答案，短期能跑、能发给别人用。

**你不改知识库内容。** 你的全部产出自包含在新建的 `web/` 目录里。

## 0. 开工前必读（按顺序，不要跳）

1. `AGENTS.md` —— 项目契约与硬规则
2. `memory/OPERATING.md` —— 操作入口，重点第 2 节「回答别人的问题」
3. `memory/CURRENT.md`、`memory/DECISIONS.md`
4. `README.md` —— 库现状：48 条 Claim / 4 节点 / 8 主题

## 1. 不可违反的约束

1. 服务层**只通过 `pkc` 读库**。禁止直接读 SQLite、`.local/`，禁止把 `knowledge/**/*.md` 当数据源，禁止把知识复制一份出去。
2. 对外只输出 `lifecycle=active` 且 `permission=public` 的 Claim。`internal` 内容不得出现，也不得改写后输出。
3. 检索不到就明说「知识库里还没有这方面的内容」，**禁止用模型常识兜底**。
4. 不改 `knowledge/**`、不改 `data/knowledge/*.json`、不动 `project-intelligence.json`；不执行任何写库命令（无 `--apply` 的一律不跑）。
5. 不引第三方运行时依赖：不 `npm install`、不加 `node_modules`。用仓库自带的便携运行时。
6. 只新增 `web/`，外加在 `.gitignore` 里追加 `web/bin/`、`web/.cache/` 这类运行时产物。别的文件一律不动。

## 2. 已验证的 PKC 契约（照抄，别自己试错）

### 2.1 调用方式

- 入口是 `tools\pkc.cmd`：内部 `chcp 65001` + 把 `.runtime\mingit\cmd` 加进 PATH + 调 `.runtime\venv\Scripts\pkc.exe`。
- **不要直接 spawn `pkc.exe`**：PATH 上没有 mingit 时会报 `[WinError 2] 系统找不到指定的文件`（实测）。
- Windows 下把 stdout 重定向到管道/文件时，Python 按本地码页（GBK）输出中文，**必须**给子进程设 `PYTHONIOENCODING=utf-8` 和 `PYTHONUTF8=1`，否则中文全乱（实测）。

### 2.2 推荐桥接（同时解决编码与命令行注入）

新建 `web/pkc-bridge.py`，用仓库自带 Python 执行：

- 解释器：`.runtime\python\python.exe`
- 内部 `subprocess.run([pkc_exe, *args], cwd=<仓库根>, capture_output=True, env=...)`
- `env` 补：`PATH` 前置 `<根>\.runtime\mingit\cmd`、`PYTHONIOENCODING=utf-8`、`PYTHONUTF8=1`
- stdout 按 utf-8 解码后原样写到自己的 stdout；把 pkc 的 `ok:false` 与退出码透传

Node 侧调用：`spawn(pythonExe, ['web/pkc-bridge.py', 'query', question, '--format', 'json', ...])` —— 参数走数组，**绝不拼命令行字符串、绝不开 shell**（用户问题不可信）。

### 2.3 三条命令

**检索（带回 summary，最适合喂模型）**

```
pkc query "<问题>" --format json --level 2 --permission public --limit 5
```

返回：

```json
{ "ok": true, "count": 2, "used_characters": 753, "budget": 8000,
  "results": [ { "kind": "claim", "id": "clm_…", "node_id": "hanzi-origin",
                 "topic_id": "topic-liushu", "title": "…", "summary": "…",
                 "lifecycle": "active", "permission": "public",
                 "score": -3.75, "conflict": "none" } ] }
```

- `summary` 是 statement 的截断版，含「适用边界」开头；`score` 越小越相关（BM25 类负分）。
- **`--level 2` 必须显式给**：历史上默认 1，只搜节点/主题标题，Claim 根本不可达。

**取全文（引用展开、边界原文）**

```
pkc show-claim <clm_…> --format json --permission public
```

返回 `claim.statement`（含 `### 标题` 与 `#### 适用边界` 的完整 markdown）、`claim.path`、`content_hash`、`lifecycle`、`permission`。

**结构（侧栏 / 健康检查）**

```
pkc tree --format text
```

返回 4 节点 8 主题及各自 Claim 数（当前 20 / 8 / 0 / 0 / 13 / 7 / 0 / 0，合计 48）。

### 2.4 三个坑（都实测过）

1. `--status current` 会把全库过滤成 0 条——这批 Claim 的 `authority_status` 是 `not_registered`。**不要加 `--status`**，用默认。
2. `progressive-query` 现在不可用：`RETRIEVAL_CANDIDATE_UNKNOWN / context has no linked knowledge nodes: default`（`relations.context_nodes` 未配置）。别用它，用 `query`。
3. `knowledge-search` 只回标题与元数据、**没有正文**，做问答不能只用它。

## 3. 技术方案（照这个做，别换栈）

- 服务端：零依赖 Node，`web/server.mjs`，只绑 `127.0.0.1:8080`。Node 用仓库外那套便携版：`C:\Users\萧磊\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\node\bin\node.exe`（v24，自带 `fetch`/`ReadableStream`）。
- 前端：`web/public/index.html` 单文件（内联 CSS/JS），中文界面，手机可用。
- 模型：DeepSeek，`https://api.deepseek.com/chat/completions`，模型 `deepseek-chat`，`stream:true`。
- Key 来源顺序：`DEEPSEEK_API_KEY` 环境变量 → `C:\Users\萧磊\.dsh\secrets\deepseek.key`。**只在服务端**持有，日志一律打掩码。
- 没有 Key 时自动降级为「检索骨架模式」：照常展示命中的 Claim 原文与出处，但不用模型编答案。

## 4. 接口契约

| 方法 | 路径 | 说明 |
| --- | --- | --- |
| GET | `/api/health` | `{ ok, pkc: "0.2.0rc5", claims: 48, mode: "model"\|"skeleton" }` |
| GET | `/api/tree` | 节点 / 主题 / Claim 数，给侧栏 |
| POST | `/api/ask` | `{question, history?}` → `text/event-stream` |

`/api/ask` 的事件：

```
data: {"type":"sources","items":[{"id":"clm_…","title":"…","topic_id":"…","node_id":"…","score":-3.75}]}
data: {"type":"delta","text":"…"}
data: {"type":"done"}
data: {"type":"error","message":"…"}
```

## 5. 回答规则（写进 system prompt）

1. 只依据本次检索到的 Claim 回答；每条结论后用 `[clm_XXXXXXXX]` 标出处，**id 必须真实存在**。
2. 检索为空或与问题无关 → 只回「知识库里还没有这方面的内容。」可补一句已收录范围（六书、声母拟态、字族通假……），**不得展开猜测**。
3. 观点类 Claim 要带上「适用边界」的意思：说明这是《系统汉语》的判断，不是文献学界共识。
4. 不复述 internal 内容，不合并、不改写知识原文。
5. 简体中文，先结论后说明，300 字以内。

## 6. 安全与运维

- Key 不进前端、不进 git、不进日志明文。
- 限流：每 IP 20 次/分钟（内存计数即可）。
- 请求体上限 64KB，问题长度上限 200 字。
- 只监听 `127.0.0.1`，对外靠隧道（第 7 节）。
- 错误页不暴露绝对路径与堆栈。

## 7. 上线（短期）

```powershell
.\web\bin\cloudflared.exe tunnel --url http://127.0.0.1:8080 --no-autoupdate
```

- 二进制放 `web\bin\cloudflared.exe`（约 55MB，从 GitHub Releases 取，`--version` 应显示 2026.10.1）。
- 每次启动得到新的 `https://*.trycloudflare.com`：免域名、免备案、够短期演示。
- 长期方案另议：Cloudflare Named Tunnel + 已备案域名；境内服务器自建域名需备案。

## 8. 验收（必须自己跑一遍，把结果贴出来）

1. `.\tools\pkc.cmd validate` → 通过。
2. `curl 127.0.0.1:8080/api/health` → `claims: 48`。
3. 问「『六书』之名最早见于哪部书？」→ 答《周礼·地官·保氏》，带 `[clm_269C128453E306F1DDE7B94294]`。
4. 问「班固和许慎的六书次序有什么不同？」→ 分别引用两条不同 Claim，不混为一谈。
5. 问「部首一共多少个？」→ `topic-components` 是空主题，检索为空 → 必须回「知识库里还没有」。
6. 用隧道地址在无痕窗口问答一次，引用可展开看原文与边界。
7. `git status`：除 `web/` 与 `.gitignore` 追加外无改动；`git diff --check` 干净。

## 9. 交付

- `web/README.md`：启动方式、换 Key、换端口、已知边界（检索是词法 BM25 不是向量；库扩到几百条以上要补 `data/knowledge/evaluation/retrieval-cases.json` 做回归）。
- 一段汇报：跑了哪些验收、结果如何、还差什么。

# 正文结束
