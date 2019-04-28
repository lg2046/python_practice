from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta, FR
import calendar

a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)

c = a + b
print(c)
print(c.days)
print(c.seconds)  # 除天后的小时的秒数
print(c.total_seconds())  # 将天一起算进去的整个delta秒数

a = datetime(2018, 1, 4)
print(a + timedelta(days=10))

b = datetime(2018, 1, 20)

print(b - a)
print(type(b - a))  # <class 'datetime.timedelta'>

print(datetime.now())

# python-dateutil提供了一些功能的扩展
print(a + relativedelta(months=1))
b = datetime(2018, 3, 21)
print(b - a)
print(relativedelta(b, a))

d = datetime.now()
# 下一下星期五
print(d + relativedelta(weekday=FR))
# 上一下星期五
print(d + relativedelta(weekday=FR(-1)))

# 获取每个月的开始周数与天数  0-6 ~ Mon-Sun
print(calendar.monthrange(2018, 5))
