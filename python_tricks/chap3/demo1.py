def yell(text):
    return text.upper() + "!"


print(yell("hello"))

bark = yell
funs = [bark, str.lower, str.capitalize]

print(funs)

# 调用函数
for f in funs:
    print(f("google"))

print(funs[0]("baidu"))


def make_counter(init=0):
    init_holder = [init]

    def ret_f():
        rv = init_holder[0]
        init_holder[0] = init_holder[0] + 1
        return rv

    return ret_f


c = make_counter(10)
print(c())
print(c())
print(c())
print(c())

print(list(map(bark, ["hello", "hey", "hi"])))

yell("google")
del yell

# yell("gogole") #exception
print(bark("google"))
print(bark.__name__)


# def print_msg():
#     # print_msg 是外围函数
#     msg = "zen of python"
#
#     def printer():
#         # printer 是嵌套函数
#         print(msg)
#
#     return printer
#
#
# another = print_msg()
# # 输出 zen of python
# another()


# 对象也可以表现了函数
class Adder:
    def __init__(self, n):
        self.n = n

    def __call__(self):
        ret_v = self.n
        self.n = self.n + 1
        return ret_v


a = Adder(10)
print(callable(a))
print(a())
print(a())
print(a())
print(a())
