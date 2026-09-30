# -*- coding: utf-8 -*-
events = [
    # 2026 剩余
    ("20261008","寒露 · 吃芝麻"),
    ("20261023","霜降 · 吃柿子"),
    ("20261107","立冬 · 吃羊肉"),
    ("20261122","小雪 · 腌腊肉"),
    ("20261207","大雪 · 喝养生粥"),
    ("20261222","冬至 · 吃饺子"),
    # 2027 全年（含 2028-01 小寒、大寒）
    ("20270204","立春 · 吃春卷"),
    ("20270219","雨水 · 吃春韭"),
    ("20270306","惊蛰 · 吃驴打滚"),
    ("20270321","春分 · 吃雷笋"),
    ("20270405","清明 · 吃菜团"),
    ("20270420","谷雨 · 吃香椿"),
    ("20270506","立夏 · 吃鸭蛋"),
    ("20270521","小满 · 吃苦菜"),
    ("20270606","芒种 · 吃梅子"),
    ("20270621","夏至 · 吃面"),
    ("20270707","小暑 · 吃新米"),
    ("20270723","大暑 · 吃仙草"),
    ("20270808","立秋 · 啃西瓜"),
    ("20270823","处暑 · 吃鸭子"),
    ("20270908","白露 · 喝米酒"),
    ("20270923","秋分 · 吃芋饼"),
    ("20271008","寒露 · 吃芝麻"),
    ("20271023","霜降 · 吃柿子"),
    ("20271107","立冬 · 吃羊肉"),
    ("20271122","小雪 · 腌腊肉"),
    ("20271207","大雪 · 喝养生粥"),
    ("20271222","冬至 · 吃饺子"),
    ("20280105","小寒 · 喝东北酸菜"),
    ("20280120","大寒 · 吃八宝饭"),
]

lines = ["BEGIN:VCALENDAR",
         "VERSION:2.0",
         "PRODID:-//Jieqi Food Calendar//CN",
         "CALSCALE:GREGORIAN",
         "METHOD:PUBLISH"]
for i,(d,title) in enumerate(events,1):
    lines += ["BEGIN:VEVENT",
              f"UID:{d}-jieqi-food-{i}@github.example",
              "DTSTAMP:20260930T000000Z",
              f"DTSTART;VALUE=DATE:{d}",
              f"SUMMARY:{title}",
              "END:VEVENT"]
lines.append("END:VCALENDAR")

path = "/Users/lijing/Doubao/chats/2026-09-30/new-chat/solar-terms-food-2026-2027.ics"
with open(path,"w",encoding="utf-8",newline="\r\n") as f:
    f.write("\n".join(lines)+"\r\n")

print("VEVENT count:", events.__len__())
print("Total lines:", len(lines))
