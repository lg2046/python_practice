# from collections import Iterator
#
#
# class RepeaterIterator(Iterator):
#     def __init__(self, repeater):
#         self.resp = repeater.resp
#         self.counter = repeater.count
#         self.init_c = 0
#
#     def __next__(self):
#         while self.init_c < self.counter:
#             self.init_c += 1
#             return self.resp
#         raise StopIteration
#
#
# class Repeater:
#     def __init__(self, resp, counter):
#         self.resp = resp
#         self.count = 10
#
#     # for in 的时候返回Iterator, 在for里面不停的调用next(iterator) 直接raise StopIteration结束
#     def __iter__(self):
#         return RepeaterIterator(self)
#
#
# repet = Repeater('Hello', 10)
# for item in repet:
#     print(item)


class Repeater:
    def __init__(self, value, times):
        self.value = value
        self.times = times
        self.init_c = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.init_c < self.times:
            self.init_c += 1
            return self.value

        raise StopIteration


repeater = Repeater('Hello', 2)

for s in repeater:
    print(s)

for s in repeater:
    print(s)
