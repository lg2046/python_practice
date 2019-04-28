import random
import types


class Student:
    # 默认情况可以给实例添加任何属性与方法
    # __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称, 但子类无效，只对当前类的实例有作用

    def __init__(self):
        self._score = 0

    @property  # 客户端可以使用student.score进行调用
    def score(self):
        return self._score

    # 上面的@property同时创建了一个@score.setter的装饰器，用来进行setter
    # 不定义setter就是一个只读属性
    @score.setter
    def score(self, value):
        self._score = value

    @classmethod
    def count(cls):
        pass

    def __repr__(self):
        return "Student: score: %s" % self._score

    def __getattr__(self, attr):
        if attr == 'name':
            return random.random()
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)


lisa = Student()

lisa.score = "123"
print(lisa.score)

from enum import Enum

# 定义了一个class类型，同时每个后面的常量都是一个唯一实例
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, member, member.name, member.value)  # value默认从1开始计数
    # Jan Month.Jan Jan 1
    # Feb Month.Feb Feb 2
    # Mar Month.Mar Mar 3
    # ...

# 精确控制value
from enum import Enum, unique


@unique  # @unique装饰器可以帮助我们检查保证没有重复值。
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6



# Weekday.Sun  Weekday['Sun']  Weekday(1) 三种访问方式

# print(lisa.names)
# class Fib:
#     def __init__(self):
#         self.a, self.b = 0, 1  # 初始化两个计数器a，b
#
#     def __iter__(self):
#         return self  # 实例本身就是迭代对象，故返回自己
#
#     def __next__(self):
#         self.a, self.b = self.b, self.a + self.b  # 计算下一个值
#         if self.a > 100000:  # 退出循环的条件
#             raise StopIteration()
#         return self.a  # 返回下一个值
#
#
# for i in Fib():
#     print(i)
#
# # 动态绑定方法
# # lisa.a = "a"
# #
# # print(lisa.a)
# #
# #
# # def set_age(self, age):
# #     self.age = age
# #
# #
# # # 动态绑定方法, 对其他实例不起作用
# # lisa.set_age = types.MethodType(set_age, lisa)
# #
# # lisa.set_age(25)
# #
# # print(lisa.age)
#
# # 给类注入实例方法，可以对所有实现起作用
# # def set_score(self, score):
# #     self.score = score
# #
# #
# # Student.set_score = set_score
# #
# # lisa.set_score(100)
# # print(lisa.score)
#
#
# # print(Student.count())
