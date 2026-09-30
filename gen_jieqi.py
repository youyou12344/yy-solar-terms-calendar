# -*- coding: utf-8 -*-
"""
自动生成"当年 + 下一年"的 24 节气食物订阅日历（固定文件名 solar-terms-food.ics）。
- 节气日期用 lunar_python 天文库实时计算，无需每年手动改年份。
- 输出 UTF-8 + CRLF 的标准 .ics，可直接被苹果日历订阅。
"""
import datetime

try:
    from lunar_python import Solar
except ImportError as e:
    raise SystemExit("缺少依赖 lunar_python，请先执行: pip install lunar_python") from e

# 节气 -> 食物（用户定义）
FOOD = {
    "立春": "吃春卷", "雨水": "吃春韭", "惊蛰": "吃驴打滚", "春分": "吃雷笋",
    "清明": "吃菜团", "谷雨": "吃香椿", "立夏": "吃鸭蛋", "小满": "吃苦菜",
    "芒种": "吃梅子", "夏至": "吃面", "小暑": "吃新米", "大暑": "吃仙草",
    "立秋": "啃西瓜", "处暑": "吃鸭子", "白露": "喝米酒", "秋分": "吃芋饼",
    "寒露": "吃芝麻", "霜降": "吃柿子", "立冬": "吃羊肉", "小雪": "腌腊肉",
    "大雪": "喝养生粥", "冬至": "吃饺子", "小寒": "喝东北酸菜", "大寒": "吃八宝饭",
}


def solar_terms(year):
    """返回某年(公历1.1~12.31)内落在该年的全部节气: {节气名: 日期}"""
    terms = {}
    d = datetime.date(year, 1, 1)
    end = datetime.date(year + 1, 1, 1)
    while d < end:
        sol = Solar.fromYmd(d.year, d.month, d.day)
        name = sol.getLunar().getJieQi()
        if name and name in FOOD:
            terms.setdefault(name, d)
        d += datetime.timedelta(days=1)
    return terms


def build_ics(events):
    """events: [(节气名, 日期)]，输出标准 .ics 文本"""
    lines = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//Jieqi Food Calendar Auto//CN",
        "CALSCALE:GREGORIAN",
        "METHOD:PUBLISH",
    ]
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    # 按日期排序，并去重（理论上不会重复）
    seen = set()
    ordered = []
    for name, date in sorted(events, key=lambda e: e[1]):
        key = (name, date)
        if key in seen:
            continue
        seen.add(key)
        ordered.append((name, date))
    for name, date in ordered:
        lines += [
            "BEGIN:VEVENT",
            f"UID:{date:%Y%m%d}-jieqi-{name}@github.example",
            f"DTSTAMP:{stamp}",
            f"DTSTART;VALUE=DATE:{date:%Y%m%d}",
            f"SUMMARY:{name} · {FOOD[name]}",
            "END:VEVENT",
        ]
    lines.append("END:VCALENDAR")
    return "\n".join(lines) + "\r\n"


def main():
    now = datetime.date.today()
    years = [now.year, now.year + 1]
    events = []
    for y in years:
        for name, date in solar_terms(y).items():
            events.append((name, date))
    out = build_ics(events)
    with open("solar-terms-food.ics", "w", encoding="utf-8", newline="\r\n") as f:
        f.write(out)
    got = {name for name, _ in events}
    missing = [k for k in FOOD if k not in got]
    print(f"生成 {len(events)} 个节气事件，覆盖年份 {years} -> solar-terms-food.ics")
    if missing:
        print("WARN 未生成的节气:", missing)
    return missing


if __name__ == "__main__":
    main()
