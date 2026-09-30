#!/usr/bin/env python3
"""lhg-ui-review 冒烟测试：校验走查报告是否符合 skill 硬性规则。

用法：
    python3 scripts/smoke_test.py <review.md>

约定：被测报告首行用 HTML 注释声明输入保真度，例如：
    <!-- input: screenshot -->   # screenshot | code | page | text

检查项：
    C1 先肯定优点：报告必须含"做得好/优点/亮点"段落
    C2 三要素：P0/P1/P2 分级区内每个条目必须含 观察/影响/修复
             （或 Observation/Impact/Recommendation）
    C3 证据边界：screenshot/page 输入必须含"未验证"声明（B 档诚实门）
    C4 分级与收敛：必须含 P0/P1/P2 分级标题，且含"最高杠杆/优先修复/Top 3"
退出码 0=全绿，1=有 FAIL。
"""
import re
import sys
from pathlib import Path

TRIAD_ZH = ("观察", "影响", "修复")
TRIAD_EN = ("observation", "impact", "recommendation")


def check(md: str) -> list:
    fails = []
    m = re.search(r"<!--\s*input:\s*(\w+)\s*-->", md)
    fidelity = m.group(1).lower() if m else "unknown"

    # C1：先肯定优点
    if not re.search(r"(做得好的|优点|亮点)", md):
        fails.append("C1 缺'做得好的/优点/亮点'段落（先肯定再批评）")

    # C2：P0/P1/P2 分级区内每个 ### 条目必须含三要素
    start = md.find("## P0")
    end = md.find("## 下一步")
    region = md[start:end if end > 0 else len(md)] if start >= 0 else ""
    entries = re.split(r"^###\s+", region, flags=re.M)[1:]
    if not entries:
        fails.append("C2 P0/P1/P2 分级区内无条目")
    for e in entries:
        head = e.split("\n", 1)[0].strip()
        body = e[len(head):]
        has_zh = all(k in body for k in TRIAD_ZH)
        has_en = all(k in body.lower() for k in TRIAD_EN)
        if not (has_zh or has_en):
            fails.append("C2 条目缺三要素（观察→影响→修复）：" + head[:30])

    # C3：B 档输入必须有"未验证"声明
    if fidelity in ("screenshot", "page") and "未验证" not in md:
        fails.append("C3 输入为 %s 却无'未验证'声明（证据边界缺失）" % fidelity)

    # C4：分级标题 + 收敛
    if not re.search(r"P0|P1|P2", md):
        fails.append("C4 缺 P0/P1/P2 分级")
    if not re.search(r"(最高杠杆|优先修复|Top 3|top 3)", md):
        fails.append("C4 缺'最高杠杆/优先修复/Top 3'收敛段")

    return fails


def main() -> int:
    if len(sys.argv) < 2:
        print("用法: python3 scripts/smoke_test.py <review.md>")
        return 2
    md = Path(sys.argv[1]).read_text(encoding="utf-8")
    fails = check(md)
    if fails:
        print("❌ 冒烟测试 FAIL：")
        for f in fails:
            print("  - " + f)
        return 1
    print("✅ 冒烟测试全绿")
    return 0


if __name__ == "__main__":
    sys.exit(main())
