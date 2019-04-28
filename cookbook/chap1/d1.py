# 任何序列（Iterable)都可以使用=进行同步赋值  字符串 文件  iterator generator都可以
# 只要变量与数据结构的数量一样
import heapq
from collections import namedtuple

from collections import Iterator

a, b, c, *d = (1, 2, 3, (4, 5), 6)

print(a)
print(b)
print(c)
print(d)

a = [1, 2, 3]
print({i: i for i in a})


def a():
    for i in range(1, 10):
        yield i


print(isinstance(a(), Iterator))

print(min(1, 2, 3))
print(max(*a()))

# 最大的三个与最小的三个, 可接key,相当于largestBy
print(heapq.nlargest(3, a(), key=lambda v_x: -v_x))
print(heapq.nsmallest(3, a()))
x = list(a())
heapq.heapify(x)
print(x)
print(heapq.heappop(x))  # 最队列中最小的

# 类似于下面这样，性能高一些
print(sorted(a())[:3])
print(sorted(a())[-3:])


# 直接使用min max找最小最大


# 实现一个优先级队列：
class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        # 让队列以优化级和插入顺序进行排序
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        if self._queue:
            return heapq.heappop(self._queue)[-1]
        else:
            return None


Item = namedtuple('Item', ['name'])
q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)

print(q.pop())
print(q.pop())
# q.push(Item('bar'), 5)
print(q.pop())
print(q.pop())
print(q.pop())

i = Item('google')
print(i._replace(name='baidu'))
print(i)
