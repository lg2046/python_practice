# 定义基类
from abc import ABCMeta, abstractmethod


# 声明基类， 此时BaseClass不能实例化，同时子类未实现所有抽象方方法时，实例化子类直接报错
class BaseClass(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass


class ConcretClass(BaseClass):
    def foo(self):
        pass


# b = BaseClass()  # 实例化也会报错
# c = ConcretClass()  # 直接报错

print(issubclass(ConcretClass, BaseClass))  # True
