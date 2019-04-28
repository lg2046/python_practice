from collections import namedtuple, deque, defaultdict, OrderedDict, Counter

# 使用属性而不是索引来引用tuple的某个元素, 具有不变性
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)

print(p)  # Point(x=1, y=2)
print(type(p))  # <class '__main__.Point'>
print(p.x)  # 1
print(p.y)  # 2

print(isinstance(p, Point))  # True
print(isinstance(p, tuple))  # True

# 使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

print(q.pop())  # x
print(q.popleft())  # y

# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：
dd = defaultdict(lambda: 'N/A')
print(dd)
print(dd['key'])  # 返回默认值 同时插入该值
print(dd)  # {'key': 'N/A'}

# 简单的计数器，例如，统计字符出现的个数：
c = defaultdict(lambda: 0)
for ch in 'programming':
    c[ch] = c[ch] + 1

print(c.items())

# 使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
# 如果要保持Key的顺序，可以用OrderedDict：
# 但是按照插入的顺序 不是key本身的顺序
d = dict([('a', 1), ('b', 2), ('c', 3), ('f', 4), ('e', 5)])
print(d)
od = OrderedDict([('a', 1), ('b', 2), ('c', 3), ('f', 4), ('e', 5)])
print(od.keys())

od = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3
print(list(od.keys()))

# OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key：
from collections import OrderedDict


class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)


d = LastUpdatedOrderedDict(2)
d['a'] = 1
d['b'] = 2
print(d)  # [('a', 1), ('b', 2)]
d['c'] = 3
print(d)  # [('b', 2), ('c', 3)]

import base64

base64.b64encode(b'binary\x00string')  # b'YmluYXJ5AHN0cmluZw=='
base64.b64decode(b'YmluYXJ5AHN0cmluZw==')  # b'binary\x00string'

# 由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_：
base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')  # b'abcd++//'
base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')  # b'abcd--__'
base64.urlsafe_b64decode('abcd--__')  # b'i\xb7\x1d\xfb\xef\xff'

# 因为Base64是把3个字节变为4个字节，所以，Base64编码的长度永远是4的倍数，因此，需要加上=把Base64字符串的长度变为4的倍数，就可以正常解码了。

from contextlib import contextmanager, closing
from urllib import request
with closing(request.urlopen("https://www.python.org")) as page:
    print(page)
    print(page.getcode())
    print(page.info())
    print(page.geturl())
    print(type(page))
    # for line in page:
    #     print(line)