import re

# r前缀不转义，直接构造对应的正则表达式字符串
s = r'ABC\-001'

# 匹配成功 返回Match对象，否则返回None
m = re.match(r'^\d{3}-\d{3,8}$', '010-12345')

print(m)

print(re.split(r'\s+', 'a b  c    d'))
print(re.split(r'[\s,]+', 'a b  c  ,,  d'))

m2 = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m2.group(0))  # 全部的匹配
print(m2.group(1))  # 第一个组
print(m2.group(2))  # 第二个组
# print(m2.group(3)) #索引超出报错
print(m2.groups())  # 以元组返回所有组

# 如果一个正则表达式需要被多次使用，最好先编译
re_tel = re.compile(r'^(\d{3})-(\d{3,8})$')
re_tel.match('010-12345').groups()
