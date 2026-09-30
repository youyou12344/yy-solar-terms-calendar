吃货的24节气，苹果日历

使用方法：
- 链接： https://youyou12344.github.io/yy-solar-terms-calendar/solar-terms-food.ics
**在苹果日历订阅**
- **Mac**：日历 App → 顶部菜单 **文件 → 新建订阅日历** → 粘贴上面链接
- **iPhone/iPad**：设置 → 日历 → 账户 → 添加账户 → 其他 → **添加已订阅的日历** → 粘贴链接

立春吃春卷
雨水吃春韭
惊蛰吃驴打滚
春分吃雷笋
清明吃菜团
谷雨吃香椿
立夏吃鸭蛋
小满吃苦菜
芒种吃梅子
夏至吃面
小暑吃新米
大暑吃仙草
立秋啃西瓜
处暑吃鸭子
白露喝米酒
秋分吃芋饼
寒露吃芝麻
霜降吃柿子
立冬吃羊肉
小雪腌腊肉
大雪喝养生粥
冬至吃饺子
小寒喝东北酸菜
大寒吃八宝饭



```bash
BEGIN:VCALENDAR          ← 整个文件的根容器（开始）
VERSION:2.0              ← 格式版本（固定写 2.0）
PRODID:...               ← 生成方标识（随便填，证明"这是谁生成的"）
CALSCALE:GREGORIAN       ← 公历
METHOD:PUBLISH           ← 发布类型（订阅日历固定写 PUBLISH）

BEGIN:VEVENT             ← 一个事件的开始
UID:...                  ← 事件的唯一身份证（关键！）
DTSTAMP:...              ← 文件生成时间戳
DTSTART:...              ← 事件开始时间
SUMMARY:寒露 · 吃芝麻    ← 显示在日历上的标题
END:VEVENT               ← 这个事件结束

BEGIN:VEVENT             ← 第二个事件……
END:VEVENT

END:VCALENDAR            ← 根容器结束（文件结尾）
```
