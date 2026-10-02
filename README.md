# lhg-ui-review · 网页 UI 专家走查

> **一句话**：给网页做专家级设计走查：截图/代码/链接三种输入，五支柱（可用性/视觉层级/一致性/无障碍/文案）系统找缺点，P0–P2 分级 + 百分制评分，每条意见按"观察→影响→修复"输出可执行指导。
>
> **一键安装**：`npx skills add lhg-skills/lhg-ui-review`


给网页做专家级设计走查的 skill：**截图/代码/链接三种输入，五支柱（可用性/视觉层级/一致性/无障碍/文案）系统找缺点，P0–P2 分级 + 百分制评分，每条意见按"观察→影响→修复"输出可执行指导**（lhg-skills 出品；五阶段评审流程借鉴 duboc/agy-skills 的 design-critique（Apache-2.0），眯眼测试与一致性审计借鉴 black141312/ada 的 ui-review（MIT），"AI 味"反模式清单为独立撰写）。

**流程**：Phase 0 判模式（NOT for 清单）→ Phase 1 输入定级与证据边界（截图确立不了的标"未验证"）→ Phase 2 第一印象扫描（2 秒 + 眯眼测试）→ Phase 3 五支柱走查（可用性/视觉层级/一致性/无障碍/文案 + 中文排版专项 + "AI 味"反模式清单）→ Phase 4 分级与评分（P0/P1/P2 + 百分制，3 个高影响修复置顶）→ Phase 5 输出（每条"观察→影响→修复"三件套，先肯定优点）→ Phase 6 双模式交付（评审报告版 / 可执行修复清单版）。

**触发**：用户说"看看这个页面 / 评审一下这个 UI / 这个设计有什么问题 / 帮我走查一下 / 上线前检查一下"时使用。

## 安装

一键安装：`npx skills add lhg-skills/lhg-ui-review`

- 通用：将本仓库放到各平台的 skill 目录（如 `~/.agents/skills/lhg-ui-review/`，注意 SKILL.md 须在目录根）。
- Coze：在扣子编程（code.coze.cn）→ 导入项目 → 本地上传本仓库 zip 包，平台会识别为 skill 类型。
- Trae：设置 → 技能 → 上传技能，选择本仓库 zip 包（或把目录放到 `~/.trae-cn/skills/`，国区版注意路径）。
- 平台无关：本 skill 写法平台中立（联网搜索/抓取页面/读取图片/代码检索/文件读写），不依赖任何单一生态的专有工具名。

## 自检与反馈

本 skill 每次执行后自动做一次轻量自检（对照输出四铁律 + 证据边界）；只有发现疑似自身缺陷时，才运行 `references/smoke-test.md` 标准用例并输出质检报告。报告经你确认后，可一键向 GitHub 提交 `[QC]` issue（模板见 `.github/ISSUE_TEMPLATE/qc-report.md`）。

## 版本

- 1.0.1（2026-10-01）：补 SkillHub 自定义头像（真人头像单独上传；内容无变化）。
- 1.0.0（2026-10-01）：首版。内化 duboc/agy-skills design-critique（Apache-2.0）五阶段流程 + black141312/ada ui-review（MIT）眯眼测试与一致性审计；升级点：输入保真度三档与证据边界诚实门、中文排版专项、中文语境"AI 味"反模式清单（独立撰写）、百分制评分、双模式交付、自迭代质检协议。

## 许可证

MIT（完整文本见 GitHub 仓库根目录 `LICENSE` 文件）。

## 什么时候用 / 什么时候不用

**用它，当你**：
- 网页上线前，想做一次专家级设计走查
- 想系统性地找 UI 缺点（可用性、视觉层级、一致性、无障碍、文案）
- 需要每条意见按"观察→影响→修复"输出的可执行指导，而不是笼统评价

**别用它，当你**：
- 评审的不是网页（它是为网页设计的：截图/代码/链接三种输入）
- 只想快速看一眼外观，不需要系统化评审报告

---

## lhg-skills 矩阵

刘洪光出品的中文 Agent Skills，全开源：

| Skill | 名称 | 一句话 |
|---|---|---|
| `lhg-writing` | 中文写作 | 风格指纹 → Orwell 六规则 → AI 味诊断，写出有人味的中文 |
| `lhg-slides` | HTML 演示文稿 | 大纲/文档一键生成可编辑的单文件 HTML slides |
| `lhg-trend` | 近30天热点扫描 | 话题火不火、为什么火、还能不能追 |
| `lhg-deep-research` | 深度调研 | 多源检索 → 结构化中文调研报告 |
| `lhg-benchmark-topic-factory` | 对标拆解选题工厂 | 找对标 → 逆向 100 条选题库 → 口播文案 |
| `lhg-net` | 互联网能力层 | 中文优先多平台取数，取不到诚实说 |
| `lhg-craft` | AI 编程工程规范 | 分级澄清 → TDD → 独立评审 → 证据门禁 |
| `lhg-debug` | 系统化调试 | 复现 → 定位 → 修复 → 验证 |
| `lhg-secure` | 代码安全审计 | 九维度扫描 + 对抗验证，分级风险清单 |
| `lhg-finder` | 找 skill 质检门 | 装第三方 skill 前的 blocker 检查 + 六维评分 |
| `lhg-ui-review` | 网页 UI 走查 | 截图/代码/链接三种输入，五支柱系统找缺点，P0–P2 分级 + 百分制评分 |

安装任意一个：`npx skills add lhg-skills/<上表 slug>`

---

## 出品：刘洪光

本 skill 由真人出镜 IP「刘洪光」（安徽合肥）出品，归属 [lhg-skills](https://github.com/lhg-skills)。

- GitHub 主页：https://github.com/lhg-skills —— 全部 skill 开源在此，欢迎 star
- 视频号：搜「刘洪光实名上网」
- 微信：lhgsmsw
