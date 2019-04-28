from datetime import datetime, timedelta
import time

now = datetime.now()

print(now)
print(type(now))

# 构建时间
dt = datetime(2015, 4, 19, 12, 20, 00)
print(dt)

print(dt.timestamp())  # 转成timestamp  等同于time.time() 小数位表示毫秒数
print(type(dt.timestamp()))

print(datetime.fromtimestamp(time.time()))  # 将timestamp转成datetime

print(datetime.utcfromtimestamp(time.time()))  # 将timestamp转成UTC标准时区的时间，默认是本地时区

# 用输入中抽取时间
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)
print(type(cday))

# 再格式化为字符串
print(datetime.strftime(cday, '%Y-%m-%d %H:%M:%S'))

# datetime加减
print(now + timedelta(hours=10))
print(now - timedelta(days=1))
print(now + timedelta(days=2, hours=12))
print(now.replace(day=1))
print(now.date())  # 2017-12-29
print(type(now.date()))  # <class 'datetime.date'>


# 拿到UTC时间后进行任意转换
