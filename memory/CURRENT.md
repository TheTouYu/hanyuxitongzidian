# 当前状态

Primary Context: `default`

## 现在是什么状态

- 知识库**已有内容**：48 条 Claim（《系统汉语》绪论第一批，2026-10-20 应用，Bundle `bnd_939f297fcadedf14d830ea7cd3`）。
- 结构：4 个节点、8 个主题，见 `data/knowledge/registry.json`。其中六书与造字理据 20 条、声母拟态与语音表意 13 条、汉字系统与字根 8 条、字族/通假/联绵词 7 条；其余 4 个主题仍是空主题。
- 项目位置：`D:\系统汉字`（2026-10-20 从 C 盘迁到 D 盘，运行环境一并搬到 `.runtime\`）。
- 运行时：PKC 0.2.0rc5，位于 `.runtime\venv`（`tools\pkc.cmd` 可直接调用）；Python 是 `.runtime\python` 里的 3.12.10 便携安装，git 在 `.runtime\mingit`。整个目录不依赖 C 盘。
- 录入链路已跑通：草稿 → 预览 → 定稿 → 批准 → 应用 → `validate` 通过；第一批 48 条即按此流程入库。
- 对外服务（网页 / 微信）：还没开始，等知识录入成型后再接。

## 下一步

1. 主人用中文讲知识（可以很口语）→ 整理成 `intake/*.json` 草稿（`node` + `fact_classes: ["evidence_scope"]` 必填）
2. `knowledge-plan capture --preview-only` 预览
3. 主人确认后，按精确哈希批准 → apply → 验证 → 提交
4. 继续补空主题：字源与形体演变、部件与偏旁部首、读音与字义、规范与易错辨析
5. 知识成型后接对外服务（网页 / 微信），服务层只用 `pkc` 检索

## 计数

4 个节点 / 8 个主题 / 48 条 Claim
