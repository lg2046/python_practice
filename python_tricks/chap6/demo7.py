def greet(name):
    return 'hello ' + name + '!'


# 任何一个函数都有一个__code__属于 可以获取运行时的指令  常量与变量
print(greet.__code__.co_code)  # b'd\x01|\x00\x17\x00d\x02\x17\x00S\x00'
print(greet.__code__.co_consts)  # (None, 'hello ', '!')
print(greet.__code__.co_varnames)  # ('name',)

# dis友好展示函数的字节码  切割指令流，给每个opcode一个有意义的操作名(比如LOAD_CONST)
import dis

dis.dis(greet)
# 2           0 LOAD_CONST               1 ('hello ')
#             2 LOAD_FAST                0 (name)
#             4 BINARY_ADD
#             6 LOAD_CONST               2 ('!')
#             8 BINARY_ADD
#            10 RETURN_VALUE
