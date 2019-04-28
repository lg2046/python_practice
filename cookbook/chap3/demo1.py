from decimal import Decimal, localcontext
import math
import os
import cmath
from fractions import Fraction
import random

print(round(0.1234, 2))
print(round(2.55, 1))
print(round(1.253, 1))

print(f'{0.1254:-<10.2f}')
# 逗号代表加入千分位符
print(f'{12345.1254:-<10,.2f}')
# f换成e可以显示为科学计数法
print(f'{12345.1254:-<10.2e}')

# 浮点数加法会出现一些溢出
print(4.2 + 2.1)

# decimal使用字符串形式进行初始化
a = Decimal('4.2')
b = Decimal('2.2')
print(a + b)

# 可以使用localcontext来控制精度
with localcontext() as ctx:
    ctx.prec = 5
    print(b / a)

nums = [1.23e+18, 1, -1.23e+18]
print(sum(nums))  # 将大数与小数计算时出现小精度丢失了

# fsum提供更高精度的计算
print(math.fsum(nums))
# 全部转成decimal进行计算
print(float(sum(Decimal(str(i)) for i in [1.23e+18, 1, -1.23e+18])))

x = 1234
print(bin(x))  # 二进制
print(oct(x))  # 八进制
print(hex(x))  # 16进制

os.chmod('./managed_file.py', 0o755)

print(1 + 2j)
print(complex(1, 2))

# cmath提供复数的一些数据操作
print(cmath.sqrt(-1))

# 无穷与NaN
print(float('inf'))
print(float('-inf'))
print(float('nan'))
print(math.isinf(float('inf')))

# Fraction提供乘法
a = Fraction(5, 4)
b = Fraction(7, 16)

print(a + b)
print(a * b)
print(a.numerator)
print(a.denominator)
print(float(a + b))
# 转成分数
print(Fraction(*3.75.as_integer_ratio()))

# 随机模块
a = list(range(1, 10))
print(random.choice(a))
print(random.sample(a, 2))
random.shuffle(a)
print(a)
print(random.randint(0, 10))
print(random.random())
print(random.getrandbits(10))
