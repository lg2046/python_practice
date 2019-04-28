# # coding:utf-8
#
#
# class Foo(object):
#     price = 50
#
#     def __new__(cls, *args, **kw):
#         print(cls)
#         print(args)
#         print(kw)
#         inst = object.__new__(cls, *args, **kw)
#         print(inst)
#         return inst
#
#     def how_much_of_book(self, n):
#         print(self)
#         return self.price * n
#
#
# foo = Foo(1, 2, 3, a="100")
# print(foo.how_much_of_book(8))
# # <__main__.Foo object at 0x1006f2750>
# # <__main__.Foo object at 0x1006f2750>
# # 400


class Hello(object):
    @staticmethod
    def hello(name='world'):
        print("hello, %s" % name)


# type()函数即可以返回一个对象的类型，也可以创建出新的类型
# 动态创建一个Hello类, 不需要class Hello(object)来声明, 第三个参数是实例方法
def fn(self, name='world'):  # 先定义函数
    print('Hello, %s.' % name)


# 要创建一个class对象，type()函数依次传入3个参数：

# class的名称；
# 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
type('Hello', (object,), dict(hello=fn))

# 通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，
# 仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。

# 具体使用元类:
# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319106919344c4ef8b1e04c48778bb45796e0335839000
