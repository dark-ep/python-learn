#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from datetime import datetime, timedelta, timezone

# 获取当前日期和时间
now = datetime.now()  # 获取当前datetime
print(now)
print(type(now))

# 获取指定日期和时间
dt = datetime(2015, 4, 19, 12, 20)  # 用指定日期时间创建datetime
print(dt)

# datetime转换为timestamp
print(dt.timestamp())  # 把datetime转换为timestamp

# timestamp转换为datetime
t = 1429417200.0
print(datetime.fromtimestamp(t))  # 本地时间
print(datetime.utcfromtimestamp(t))  # UTC时间

# str转换为datetime
cday = datetime.strptime('2015-04-19 12:20:00',
                         '%Y-%m-%d %H:%M:%S')  # https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
print(cday)

# datetime转换为str
print(now.strftime('%a, %b %d %H:%M'))

# datetime加减
print(now + timedelta(hours=10))
print(now - timedelta(days=1))
print(now + timedelta(days=2, hours=12))

# 本地时间转换为UTC时间
tz_utc_8 = timezone(timedelta(hours=8))  # 创建时区UTC+8:00
dt = now.replace(tzinfo=tz_utc_8)  # 强制设置为UTC+8:00
print(dt)

# 时区转换
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)


def to_timestamp(dt_str, tz_str):
    # 转换时间
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    # 设置时间时区
    m = re.match(r'^UTC([+-]\d+):00$', tz_str)  # 截取时区数字
    tzone = int(m.group(1))
    utc_dt = dt.replace(tzinfo=timezone(timedelta(hours=tzone)))
    # 转换成timestamp
    return utc_dt.timestamp()


t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')
