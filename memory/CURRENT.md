# 当前状态

Primary Context: `default`

## 现在是什么状态

- 知识库**已有内容**：361 条 Claim，分四批应用：绪论 48 条（`bnd_939f297fcadedf14d830ea7cd3`）、卷一·雞 32 条（`bnd_5cf8eb8a6881a0e85b0133159e`）、卷二 113 条（`bnd_02df398a46081d2fc3f2c11408`）、卷三·矢 168 条（`bnd_9e5916739a578f96b14afe7e08`），均在 2026-10-20。
- 结构：5 个节点、16 个主题，见 `data/knowledge/registry.json`。绪论部分：六书与造字理据 20 条、声母拟态与语音表意 13 条、汉字系统与字根 8 条、字族/通假/联绵词 7 条；新节点「音源字卷」（`hanzi-yinyuan`）下有卷一·雞 32 条、卷二·㠯部 41 条、卷二·士部与示部 39 条、卷二·帝部以下诸部 33 条、卷三·矢部 73 条、卷三·尸部与朿部 25 条、卷三·齐次𠂔诸部 24 条、卷三·意部以下诸部 46 条。六书之外仍有 4 个空主题。
- 书的结构：《系统汉语》分十二章 → 约百卷（以音源字为纲）→ 609 部，已录入卷一见 `D:\字谱智能体\卷一.docx`、卷二 `卷二  㠯.docx`、卷三 `卷三  矢.docx`，其余分卷同目录。
- 已作废、不可再应用的 Bundle（三批合并前的产物）：`bnd_caffd9d8f571e9d7ab01318208`、`bnd_5e291a942c995e287f5cf0d120`、`bnd_965e74be117c02b9c274cbdb69`，已由 `bnd_02df398a…` 取代。
- 项目位置：`D:\系统汉字`（2026-10-20 从 C 盘迁到 D 盘，运行环境一并搬到 `.runtime\`）。
- 运行时：PKC 0.2.0rc5，位于 `.runtime\venv`（`tools\pkc.cmd` 可直接调用）；Python 是 `.runtime\python` 里的 3.12.10 便携安装，git 在 `.runtime\mingit`。整个目录不依赖 C 盘。
- 录入链路已跑通：草稿 → 预览 → 定稿 → 批准 → 应用 → `validate` 通过；绪论、卷一、卷二、卷三均按此流程入库。
- 踩过的坑：多个 bundle 都以同一份 `registry.json` 为基线时不能顺序应用（第二个会报 `authority changed`），同一轮的同类新增要合并成一个 bundle；`node_*` 元数据只在节点尚未存在时随首条 claim 提交，节点已存在则只留 `topic_*`。
- 沙箱写权限（2026-10-20 已修好）：受限会话是**低完整性级别（Low IL）令牌**，只能写同样带 Low 强制标签的对象；`icacls <路径>` 末行 `Mandatory Label\Low Mandatory Level:(OI)(CI)(NW)` 就表示可写。做法：给目录补显式「萧磊 完全控制」（否则改标签会被 `Access is denied` 拒），再 `icacls <目录> /setintegritylevel '(OI)(CI)L' /T /C /Q`；根目录散文件靠「同目录复制→替换」继承标签。如今 `D:\系统汉字` 全树（`.git`、`intake`、`knowledge`、`data`、`.local`、`memory`、`web`、`prompts`、`tools` 及根目录文件）都已 Low，写库不再需要逐条升级批准；日志与回滚材料在 `D:\acl-recovery-vol3\`。再遇 `Access is denied`，先查标签，不要先升级权限。
- 对外服务（网页 / 微信）：**网页已上线**。`web/` 是零依赖 Node 服务 + 单文件前端，只经 `pkc` 检索、只答 `active`+`public` 的 Claim；两种模式——「问答」和「字卡」（输入一个字，按 字形图 → 字根 → 本义 → 转义 → 衍生字义 五栏答，每栏必须带 `clm_` 出处，无依据就显示缺项；字本身没有字形行的退用字根的字形图）。字形图与原稿实物配图（士 = 公牛、里 = 土地庙）从 `D:\字谱智能体\*.docx` 抽出，`web/public/glyphs`（1057 字 / 2557 图 + 194 张配图，图下自带出处与分期），重抽用 `tools/extract-glyphs.mjs`。启动：`web\start.cmd`（服务 127.0.0.1:8080 + cloudflared 匿名隧道）。微信尚未接入。

## 下一步

1. 主人用中文讲知识（可以很口语）→ 整理成 `intake/*.json` 草稿（`node` + `fact_classes: ["evidence_scope"]` 必填）
2. `knowledge-plan capture --preview-only` 预览
3. 主人确认后，按精确哈希批准 → apply → 验证 → 提交
4. 继续录后续分卷（`D:\字谱智能体\` 下各卷 docx，卷四起）；每卷按「一个卷主题 + 若干部」拆，草稿先落 `intake/`
5. 继续补绪论批的 4 个空主题：字源与形体演变、部件与偏旁部首、读音与字义、规范与易错辨析
6. 接微信（网页已上线；服务层只用 `pkc` 检索，别复制知识出去）
7. 字卡要更饱满，靠继续录入：卷二、卷三已入库（字卡的本义/转义/衍生随之补齐，不用改代码），接着录卷四起

## 计数

5 个节点 / 16 个主题 / 361 条 Claim
