"""链接兜底 —— 没有官方链接的活动补一个"按标题搜索"链接,保证每条点开都有有效信息。

统一用百度搜索兜底(国内可达、按活动名一定能搜到新闻/购票/详情):
  · 演出/体育 → 搜 "<标题> 购票"(偏向票务页)
  · 其他(展会等) → 搜 "<标题> 上海"
有些源(猫眼卡片走 JS、部分策展活动)本身没有 href,靠这一步补齐。
(曾用大麦站内搜索,但按完整标题常搜不到 → 改百度更可靠。)
"""
from __future__ import annotations

from typing import List
from urllib.parse import quote

from models import Event


def add_fallback_links(events: List[Event]) -> List[Event]:
    n = 0
    for e in events:
        if e.official_url:
            continue
        if e.type in ("演出", "体育"):
            q = f"{e.title} 购票"
        else:
            q = f"{e.title} 上海"
        e.official_url = f"https://www.baidu.com/s?wd={quote(q)}"
        n += 1
    print(f"[links] 补充百度搜索兜底 {n} 条")
    return events
