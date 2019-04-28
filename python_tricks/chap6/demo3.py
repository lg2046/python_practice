def repeater(value, times):
    for _ in range(times):
        yield value
    # 不需要手动raise Stop Interation 来表示结束


for i in repeater("hello", 2):
    print(i)

repeater = repeater("hello", 2)
next(repeater)
next(repeater)
next(repeater)  # StopIteration


# genexpr = (expression for item in collection)
# 等价于
# def genexpr():
#     for item in collection
#         yield expressio

