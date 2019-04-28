print(hash((1, 2, 3, (4, 5,),)))

# list为可变,非hashable  异常
# print(hash((1, 2, 3, [4, 5, ],)))

# frozenset里面只能容纳可散列类型
# frozenset接seq类型
print(hash((1, 2, 3, frozenset([4, 5, ]),)))

from collections.abc import Sequence, Mapping

print(isinstance(range(10), Sequence))
print(isinstance(range(10), Mapping))
print(isinstance({'a': 1}, Mapping))

# 创建字典的方法
# 1: 关键字参数
print(dict(a=1, b=2, c=3))
# 2: 字面量
print({'a': 1, 'b': 2, 'c': 3})
# 3: kw list
z = zip(['a', 'b', 'c'], [1, 2, 3])
print(z)  # <zip object at 0x1087fc308>
print(dict(zip(['a', 'b', 'c'], [1, 2, 3])))
print(dict(z))
# 4: 对dict再dict无变化
print(dict({'a': 1, 'b': 2, 'c': 3}))
print(dict(dict({'a': 1, 'b': 2, 'c': 3})))
# 5: dict comprehension
print({x: y for x in ['a', 'b', 'c'] for y in range(1, 4)})

print(list(iter({}.fromkeys(range(10), "a"))))

d = dict({'a': 1, 'b': 2, 'c': 3})
print(d.popitem())
print(d)

d.setdefault('a', 2)
print(d)

d.update({'e': 10, 'a': 3})
print(d)
print(d.keys())
print(d.values())

from collections import defaultdict

d2 = defaultdict(list)
d2[1].append(3)
print(d2[1])
print(d2[2])
print(d2.get(3))

# d3 = {}
# print(d3.setdefault(1, [3]))
