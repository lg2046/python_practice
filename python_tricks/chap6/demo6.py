class A:
    pass


xs = {'a': 1, 'b': 2}
ys = {'b': 3, 'c': 4}

# method1
zs = {}

zs.update(xs)
zs.update(ys)

print(zs)

# method2
print(dict(xs, **ys))

# method3 python3.5+
print({**xs, **ys})

# json方式 可以缩进，但只适合一些原语数据类型
import json

mapping = {'a': 23, 'b': 42, 'c': 0xc0ffee, 'd': [1, 2, 3], 'e': {'a': 1, 'b': 2}}
print(json.dumps(mapping, indent=4, sort_keys=True))

# pprint适用一些自定义类型
from pprint import pprint

mapping = {'a': 23, 'b': 42, 'c': 0xc0ffee, 'd': {1, 2, 3}, A(): 3}
pprint(mapping)
