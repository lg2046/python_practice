import html
import os
import re
from calendar import month_abbr
from fnmatch import fnmatch

a = 'asdf fjdk; afed, fjek,  asdf, foo '.strip()

# str.split只是按符号简单切割
print(a.split(' '))

# 使用re.split更灵活
# 如果正则里面有组，则匹配的组也会在split里面
# 如果要使用组，但不想包含在结果中，使用(?:[,;]+)
fields = re.split(pattern=r'([,;\s]+)', string=a)

values = fields[::2]
delimiters = fields[1::2]

print(values)
print(delimiters)

# startswith可以接一个tuple来多个检测
print(a.startswith(("sd", "as")))
print(a.endswith("foo"))

dirname = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'chap1')
print(any(f.endswith('.py') for f in os.listdir(dirname)))
print(dirname)

# fnmatch fnmatchcase
# 使用shell中的* ?来匹配

print(fnmatch("abc.txt", "*.txt"))

print('abc'.find('b'))

# match总是从字符串的开头进行匹配
print(re.match(pattern=r'bc', string='abc'))

print(re.findall(pattern=r'bc', string='abc, bc, bbc'))

# 简单替换所有文本
text = 'yeah, but no, but yeah, but no, but yeah'
print(text.replace('no', 'yes'))

text = 'Today is 11/5/2012. PyCon starts 3/11/2013.'
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\2-\1', text))


def change_date(m):
    return f"{m.group(1)}-{month_abbr[int(m.group(2))]}-{m.group(3)}"


# 匹配上一个，使用match调用后面的函数
# subn除了返回替换后的字符串，还会返回替换了几次
print(re.sub(r'(\d+)/(\d+)/(\d+)', change_date, text))

text2 = '''/* this is a
multiline comment */
'''

print(re.findall(r'/\*((?:.|\n)*?)\*/', text2))

print(format('google', '=^20s'))
print('google'.center(20, '='))

print(f'{123:=^10.2f}')
print(f'{123:.>10.2f}')

print(','.join(str(s) for s in ['ACME', 50, 91.1]))

print(1, 2, 3, sep=":")
print(":".join(str(c) for c in [1, 2, 3]))

# format_map可以用于简单的替换模板的功能
s = '{name} has {n} messages.'
d = {"name": "Guido", "n": 10}
print(s.format_map(d))
print(s.format(name='Guido', n=5))

s = 'Elements are written as "<tag>text</tag>".'
print(html.escape(s))
h = html.escape(s, quote=False)
print(html.unescape(h))
