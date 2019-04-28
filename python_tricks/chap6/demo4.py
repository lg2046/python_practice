# def integers():
#     for i in range(10):
#         yield i
#
#
# # 接受一个生成器，生成另外一个生成器
# def squared(seq):
#     for i in seq:
#         yield i * i
#
#
# def neg(seq):
#     for i in seq:
#         yield -i
#
#
# # generator链
# print(list(neg(squared(integers()))))


# 使用生成器表达式
import operator
from collections import OrderedDict

integers = range(10)
squared = (i * i for i in integers)
neged = (-i for i in squared)

print(list(neged))

xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}
print(OrderedDict(sorted(xs.items(), key=operator.itemgetter(1), reverse=True)))
