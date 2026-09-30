# 标准冒烟测试（skill 自检用）

> 触发时机：SKILL.md「自检与反馈」命中疑似自身缺陷时运行。
> 说明：`scripts/smoke_test.py` 校验走查报告是否符合本 skill 硬性规则
> （C1 先肯定优点 / C2 每条意见"观察→影响→修复"三要素 / C3 B 档输入的"未验证"证据边界声明 / C4 P0-P2 分级 + 最高杠杆收敛）。
> 被测报告首行用 `<!-- input: screenshot|code|page|text -->` 声明输入保真度。
> 以下全部用例已于 2026-10-01 实测通过。

## S-1 合规报告全绿

- fixture：`references/fixtures/fixture-review-good.md`
- ```bash
  python3 scripts/smoke_test.py references/fixtures/fixture-review-good.md
  ```
  → 退出码 0，`✅ 冒烟测试全绿`

## S-2 缺优点段落被拦截

- fixture：`references/fixtures/fixture-review-no-strengths.md`
- ```bash
  python3 scripts/smoke_test.py references/fixtures/fixture-review-no-strengths.md
  ```
  → 退出码 1，FAIL 含 `C1 缺'做得好的/优点/亮点'段落`

## S-3 条目缺三要素被拦截

- fixture：`references/fixtures/fixture-review-no-triad.md`（P1 条目缺"修复"）
- ```bash
  python3 scripts/smoke_test.py references/fixtures/fixture-review-no-triad.md
  ```
  → 退出码 1，FAIL 含 `C2 条目缺三要素`

## S-4 截图输入缺"未验证"声明被拦截

- fixture：`references/fixtures/fixture-review-no-untested.md`（对键盘可达性下结论却无"未验证"）
- ```bash
  python3 scripts/smoke_test.py references/fixtures/fixture-review-no-untested.md
  ```
  → 退出码 1，FAIL 含 `C3 输入为 screenshot 却无'未验证'声明`
