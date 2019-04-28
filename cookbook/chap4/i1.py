from collections import Iterable, Iterator
import heapq
import itertools


class A:
    def __iter__(self):
        return iter([1, 2, 3])


for i in A():
    print(i)


def frange(start, end, step):
    x_ = start
    while x_ < end:
        yield x_
        x_ = x_ + step


for i in frange(0, 10, 3):
    print(i)

print(sum(frange(0, 100, 3)))

# generator可以用来next()
# 只要可以被next()的对象都是Iterator, 包括有iter方法获取的或者是generator
# 所有可以被for的都是Iterable
print(isinstance(frange(0, 10, 3), Iterable))
print(isinstance(frange(0, 10, 3), Iterator))
print(isinstance([1, 2, 3], Iterable))
print(isinstance([1, 2, 3], Iterator))

# isslice只截取iterator的一部分
# dropwhile是根据函数式drop
print(list(itertools.islice(frange(0, 10, 0.2), 10, 20)))
print(list(itertools.dropwhile(lambda x: x < 2, frange(0, 10, 0.2))))

print(list(itertools.islice([1, 2, 3, 4, 5], 1, 2)))

# 所有的排列
for i in itertools.permutations([1, 2, 3]):
    print(i)

# 两个的排列
for i in itertools.permutations([1, 2, 3], 2):
    print(i)

# 所有的组合
for i in itertools.combinations([1, 2, 3], 3):
    print(i)

# 两个的组合
for i in itertools.combinations([1, 2, 3], 2):
    print(i)

# 可重复组合
for i in itertools.combinations_with_replacement([1, 2, 3], 2):
    print(i)

print(dict(zip(range(1, 10), range(10, 20))))

for i, j in itertools.zip_longest(range(1, 10), range(10, 20)):
    print(i, j)

for i in itertools.chain(range(1, 10), range(5, 15)):
    print(i)

for i in heapq.merge(range(1, 10), range(5, 15)):
    print(i)

for i in heapq.merge([1, 4, 7, ], [2, 5, 8, ], [3, 6, 9, ]):
    print(i)

s = open("./i1.py", 'r')
for s_p in iter(lambda: s.read(10), ''):
    print(s_p)


def flatten(items):
    for x_ in items:
        if isinstance(x_, Iterable):
            yield from flatten(x_)
        else:
            yield x_


for x in flatten([1, 2, [3, 4, [5, 6], 7], 8]):
    print(x)
