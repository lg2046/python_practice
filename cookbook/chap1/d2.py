import json
from collections import defaultdict
from collections import OrderedDict
from collections import Counter
from collections import ChainMap
from operator import itemgetter, attrgetter
import time

import itertools

d = defaultdict(list)  # defaultdict接一个无参可调用函数
d['a'].append(1)
d['a'].append(2)
_ = d['b']  # 访问时即创建对象k v
print(d)

# 使用普通dict来进行default
d = {}  # A regular dictionary
d.setdefault('a', []).append(1)

d = OrderedDict()
d['foo'] = 1
d['bar'] = 1
d['spam'] = 1
d['grok'] = 1

print(d)

print(json.dumps(d))  # json输出时会保持顺序

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75,
}

# 将字典KV反向
rev_prices = zip(prices.values(), prices.keys())  # 返回的是iterator,只能被消费一次
print(rev_prices)
print(type(rev_prices))
print(max(zip(prices.values(), prices.keys())))  # (612.78, 'AAPL')
print(min(zip(prices.values(), prices.keys())))  # (10.75, 'FB')
print(sorted(zip(prices.values(), prices.keys())))
# [(10.75, 'FB'), (37.2, 'HPQ'), (45.23, 'ACME'), (205.55, 'IBM'), (612.78, 'AAPL')] 操作的都是二元组
# 所以比较都是基于二元两个元素

# 正常的min(dict)只是比较的key 且只返回key
print(min(prices))
print(prices[min(prices, key=lambda k: prices[k])])

# 删除某些dict的key
print({key: prices[key] for key in prices.keys() - {'ACME'}})

a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(set(a)))
print(list(set(a)))
print(list(set(a)))
print(list(set(a)))


def unique(l, key=None):
    s = set()
    for item in l:
        item_key = item if key is None else key(item)
        if item_key not in s:
            yield item
            s.add(item_key)


with open("./d2.py") as f:
    for line in unique(f):
        print(line)

s = slice(1, -1, 2)
print(a[s])

del a[s]
print(a)

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]


def identity(x):
    return x


g = itertools.groupby(sorted(words, key=identity), key=identity)
for k, v in g:
    print(k, len(list(v)))

a = (1, 2, 3)
b = ('A', 'B', 'C')

for elem in itertools.product(a, b):
    print(elem)

print("self")
for elem in [(xa, xb) for xa in a for xb in b]:
    print(elem)

c1 = Counter(words)
c2 = Counter(words)
print(c1['eyes'])
print(c2['eyes'])
merge = c1 + c2
merge.update(words)  # 不停的加入
print(merge.most_common(3))


def benchmark(func):
    def wrapper(*args, **kw):
        start = time.time()
        result = func(*args, **kw)
        print(f"benchmark: {time.time() - start}")
        return result

    return wrapper


rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003}, {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001}, {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]


@benchmark
def test1():
    for _ in range(1, 5000000):
        sorted(rows, key=itemgetter('lname', 'fname'))


# 比下面的手动要快10%

@benchmark
def test2():
    for i in range(1, 5000000):
        sorted(rows, key=lambda x: (x['lname'], x['fname']))


# 还有attrgetter 构建出函数可以用于其他比如min max函数

# test1()
# test2()

print(list(filter(lambda s: len(s['lname']) > 4, rows)))

addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK'
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]
counts = [0, 3, 10, 4, 1, 7, 6, 1]

print(list(itertools.compress(addresses, [n > 0 for n in counts])))

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75,
}

tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
print({k: v for k, v in prices.items() if k in tech_names})

print(','.join(str(x) for x in range(1, 10)))

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

for i in ChainMap(a, b).items():
    print(i)

a.update(b)
print(a)

x = 123

for x in range(1, 10):
    print(x)

print(x)
