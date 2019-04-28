# class MyClass:
#     # 实例方法,  带一个self参数，指向方法的调用者, 后面也可以带其他的参数
#     # 实例方法可以直接访问同对象的实例变量与其他方法
#     # self.__class__可以访问到类来修改类状态
#     def method(self):
#         return 'instance metohd called', self
#
#     # 类方法带cls参数指向调用类, 可以修改类状态，但不能修改实例状态
#     @classmethod
#     def classmethod(cls):
#         return 'class method called', cls
#
#     # 静态方法没有self与cls参数 可以接受任何其他参数 即不能修改类状态也不能修改实例状态
#     # 用户一般是用类来封装一些功能上相近的的一组方法
#     # 只是为方法来提供命名空间的一种方式
#     @staticmethod
#     def staticmethod():
#         return 'static method called'
#
#
# obj = MyClass()
# obj.method()  # 实例方法调用，将self替换为obj
# # 可以忽略上面提供的语法糖，手动传入实例直接调用方法:
# MyClass.method(obj)
#
# MyClass.classmethod()
#
# MyClass.staticmethod()


class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients})'


p = Pizza(['cheese', 'tomatoes'])
print(p)

# 不可变字节数组
# arr = bytes([0, 1, 2, 3])
# print(arr)  # b'\x00\x01\x02\x03'
# print(arr[1])  # 1
# arr2 = b'\x00\x01\x02\x03'
# print(type(arr2))  # <class 'bytes'>
#
# # arr[1] = 2  # 报错 不可变
# print(bytes([0, 300]))  # 报错  bytes must be in range(0, 256)


arr = bytearray([0, 1, 2, 3])
print(arr)  # bytearray(b'\x00\x01\x02\x03')
print(arr[1])  # 1

arr[1] = 3  # 可以修改 del append
print(arr)  # bytearray(b'\x00\x03\x02\x03')
# arr[1] = 300  # 报错


# named tuple
from typing import NamedTuple


# 后面的类型注释只是提示，并没有在初始化时强制检查
class Car(NamedTuple):
    color: str
    mileage: float
    automatic: bool


car1 = Car('red', 3812.4, False)

print(car1)  # Car(color='red', mileage=3812.4, automatic=False)
print(car1.color)
print(car1.automatic)

car1.automatic = True  # 不能赋值
