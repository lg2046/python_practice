import functools


# 接受原函数, 返回一个新函数
def log_decorator(func):
    @functools.wraps(func)  # 函数__name__仍然是原名字
    def new_func(*args, **kwargs):
        print("begin")
        result = func(*args, **kwargs)
        print("end")
        return result

    return new_func


def upper_decorator(func):
    @functools.wraps(func)  # 函数__name__仍然是原名字
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()

    return wrapper


def bang_decorator(func):
    @functools.wraps(func)  # 函数__name__仍然是原名字
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + "!bang"

    return wrapper


@upper_decorator
@bang_decorator
def a():
    return "abc"


if __name__ == '__main__':
    print(a())
    print(a.__name__)


    def foo(x, *args, **kwargs):
        from collections.abc import Sequence
        kwargs['name'] = 'Alice'
        new_args = args + ('extra',)
        print(args)
        print(type(args))
        print(isinstance(args, Sequence))
        print(new_args)
        print(kwargs)


    foo(1, 2, 3, 4, a=1)
