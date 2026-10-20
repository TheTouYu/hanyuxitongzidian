# 系统汉字

「系统汉字」知识库本体，基于 [Portable Knowledge Core](https://github.com/TheTouYu/portable-knowledge)（PKC 0.2.0rc5）。
现在有 **48 条知识**（《系统汉语》绪论第一批：六书、声母拟态、字族、汉字系统），4 个节点 / 8 个主题。

## 目录说明

| 路径 | 作用 |
| --- | --- |
| `project-intelligence.json` | 实例配置：身份、路径、记忆角色、评测入口 |
| `data/knowledge/registry.json` | 知识树：节点（Node）与主题（Topic） |
| `knowledge/` | 知识正文，每条知识是一个带稳定 ID 的 Claim 区块 |
| `memory/` | 启动记忆：操作规程、当前状态、决策记录 |
| `intake/` | 知识录入草稿区 |
| `data/knowledge/evaluation/` | 检索回归用例（先空着，知识多了再补） |
| `tools/` | `pkc` 和 `git` 的包装命令 |
| `.runtime/` | 运行环境：便携 Python 3.12.10、PKC 的 venv、便携版 Git、源码副本，不进 git |
| `.local/` | 可丢弃的检索投影，不进 git |

## 当前结构

4 个节点 / 8 个主题 / 48 条 Claim：

- 汉字本源 → 字源与形体演变（0）、六书与造字理据（20）、汉字系统与字根（8）
- 汉字结构 → 部件与偏旁部首（0）
- 汉字音义 → 读音与字义（0）、声母拟态与语音表意（13）、字族、通假与联绵词（7）
- 汉字应用 → 规范与易错辨析（0）

## 日常命令

```powershell
.\tools\pkc.cmd validate       # 自检
.\tools\pkc.cmd tree --format text
.\tools\pkc.cmd knowledge-search "部首" --format json --limit 5
.\tools\pkc.cmd knowledge-check --format text
```

## 怎么录入知识

**推荐**：直接用中文把知识讲出来（口语也行），我会整理成 Claim 草稿、生成预览，等你确认精确哈希后再写进库。

**自己动手**：照着 `intake/README.md` 写一份草稿，然后：

```powershell
.\tools\pkc.cmd knowledge-plan capture --file intake\20261020-人字.json --preview-only   # 只预览
.\tools\pkc.cmd knowledge-plan capture --file intake\20261020-人字.json                  # 定稿，输出哈希
.\tools\pkc.cmd bundle-inspect bnd_xxxxxxxx --format json
.\tools\pkc.cmd bundle-approve bnd_xxxxxxxx --content-hash <64 位哈希> --apply
.\tools\pkc.cmd bundle-apply   bnd_xxxxxxxx --content-hash <64 位哈希> --apply
.\tools\pkc.cmd validate
```

每条 Claim 必填 `node`、`topic_id`、`title`、`statement`、`boundary`、`permission`、`fact_classes`；汉字知识统一 `["evidence_scope"]`。

第一批 48 条已走完整个流程（草稿 → 定稿 → 按哈希批准 → 应用 → `validate` 通过），Bundle 记录在 `data/knowledge/bundles/`。

## 后续对外服务

网页 / 微信只做两件事：把用户问题交给检索，把检索到的 Claim 组织成答案。
服务层永远通过 `pkc` 读库，不直接读 SQLite、也不复制一份知识出去。
